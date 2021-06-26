#Design Patterns with the First-Class Functions

#Ecommerce Discount Scheme Design Patter
# Order(Context) -> Promotion (Strategy)
#                     ->FidelityPromo     Concrete
#                     ->LargeOrderPromo   Strategies
#                     ->BulkItemPromo     for abc Promotion

from abc import ABC, abstractmethod
from collections import namedtuple
from math import dist, prod

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    
    def total(self):
        return self.price*self.quantity
    
class Order: #Context
    def __init__ (self, customer, cart, promotion = None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    
    def total(self):
        """"This method creates the total iff it is not created"""
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion == None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__ (self):
        fmt = "Order total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())

#Abstract Base Class - Since it does not have a meaning in itself
class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """Return Discount as an amount"""

class FidelityPromo (Promotion):
    """5% discount for customers with > 1000 pts"""
    def discount(self, order):
        return order.total()*.05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo (Promotion):
    """10% discount for each LineItem with 20 or more units"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount == item.total()*.1
        return discount

class LargeOrderPromo(Promotion):
    """7% discount for orders with 10 or more distinct items"""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total()*.07
        return 0

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5),
                                LineItem('watermellon', 5, 5.0)]
print(Order(joe, cart, FidelityPromo()))

#The better way to do it in Python will be to have No Abstract Class
#we can just pass in the promo (like bulk_item_promo, fidelity_promo etc)
#as in the funtion call when initializing objects.
#We can just pass the promotion function as an argument 

#For choosing the best out of them all
promos = [FidelityPromo, BulkItemPromo, LargeOrderPromo]
def best_promo(order):
    return max(promo(order) for promo in promos)
#print(Order(joe, cart, best_promo))

#To make the application scalable, we need the best_promo to be filled
#from the list of all available promos

promos = [globals()[name] for name in globals()
            if name.endswith('_promo')
            and name != 'best_promo']
#def best_promo(order): ---snip---

#Command Design Patterns
