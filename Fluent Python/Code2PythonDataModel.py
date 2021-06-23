#Data Model-Python Framework, sequences, iterators, functions
#classes, context managers, special methods are invoked inside
#__getitem__, my_collection[key] = my_collection.__getitem__(key)
#OO, Strings, Blocks, Attribute access and collections etc
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    #Better way of init a list of elements using string and calling the split method
    suits = 'spades diamonds clubs hearts'.split()

    def __init__ (self):
        self._cards = [Card(rank, suit) for suit in self.suits 
                                        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')
print(len(beer_card))

deck = FrenchDeck()
print(len(deck), deck[34:-1])
print(deck[1],"\n", deck._cards)
#._cards they are a list of all the elements
#Using namedtuple, each ind is tuple, when collected they are part of a class 

from math import hypot
class Vector:
    def __init__ (self, x=0, y=0):
        self.x = x; self.y = y
    
    def __repr__ (self):
        return 'Vector(%r, %r)'%(self.x, self.y)
    
    def __abs__ (self):
        return hypot(self.x, self.y)
    
    def __add__(self, other):
        x = self.x + other.x
        y= self.y + other.y
        return Vector(x, y)
    
    def __mul__ (self, scalar):
        return Vector(self.x*scalar, self.y*scalar)

#__repr__ method is used to get to know about repr built in to get string representations
#if we not implement that, they would be shown like the memory locations like 0x100 type

