#Object Oriented Designs 
#Objects, References, Mutability and Recycling

#Variables are not boxes 
a = [1, 2, 3]
b = a
a.append(4)
print(b)
#They are not boxes but Sticky Label attached 
#Variable is assigned to an object, after the object is created
class Gizmo:
    def __init__(self):
        print('Gizmo id: %d'%id(self))
x = Gizmo()
print(x)
# <-<-<-<-
#y = Gizmo()*10
#print(y), The left side is only a label, right side is an Object

#Identiy, Equality and Aliases
charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print("\n", id(charles), id(lewis))
lewis['key'] = 99
print(lewis, "\n", lewis is charles, "\n", charles)
# As long the two objects have Same ID, operations happen simultaneously 

alex = {'name': 'Charles L. Dodgson', 'born': 1832}
print(alex == charles)
print(alex is not charles)
print(type(alex) is type(charles), id(charles) is id(alex))

#Choosing between == and is
#The ==operator compares the values of objects (the data they hold), while is comparestheir identities
#The limitation of shallow copy is they may show arbitrary behaviour when going down

class Bus:

    def __init__ (self, passengers= None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    
    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)
    

import copy
print(copy.__doc__)
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
print(bus1 is not bus2)
bus3 = copy.deepcopy(bus1)
print(bus1 is not bus3)
print(id(bus1), id(bus2), id(bus3))
bus1.drop('Bill')
#See the effect of shallow copies
print(bus2.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
print(bus3.passengers)

#Cyclic References
a = [10, 20]
b = [a, 30]
#Simple appending enters into an infinite loop
a.append(b)
print(a, "\n", len(a))
#__copy()__, __deepcopy()__

#Function Parameters as References
#Parameter passing is done by Call By Sharing
#Mutable Types as paramter defaults : Bad Idea

class HauntedBus:
    def __init__ (self, passengers = []):
        self.passengers = passengers
    
    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

#The Default Value might change and cause problems 
#Thats why if there is nothing start or init with <None>

#Defensive Programming with Mutable Parameters
import weakref
s1 = {1, 2, 3}
s2 = s1
def bye():
    print("Gone with the wind...")

ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1
print(ender.alive)

s2 = 'spam'
print(s2)
print(ender.alive)
#Basically It is alive even after deleting REFERNCES to it
#But it can be only deleted after Mutating or rebinding the refernce
