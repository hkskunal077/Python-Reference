#Interfaces: Protocols to ABCs
class Vector:
    typecode = 'd'
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
    #This decorator helps calling the x by creating the interface
    @property
    def x(self):
        return self.__x
    #y creating the interface for calling it as a method
    #this provides a method, for accessing variables
    @property
    def y(self):
        return self.__y
    def __iter__(self):
        return (i for i in (self.x, self.y))

vector = Vector(3.8, 4.4)
print(vector.x, vector.y)
#These vector.x and vector.y are not callable because they are passed on 
#to the Decorator function <@property>, so we also pass that function to 
#return only as the name of the function and not being callable itself

#French Deck is an example of Duck Typing
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FD:
    ranks = [str(n) for n in range(2, 11)] +  list("JQKA")
    suits = "spades diamonds clubs heards".split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
    def __setitem__(self, position, card):
        self._cards[position] = card
fd = FD()
print(fd.__len__, "\n", fd.__getitem__(10))

#Monkey Patching to Implement a Protocol at Runtime
#If Duck Typing is intact, we do not need methods for Duck
from random import randint, shuffle
l = list(range(10))
shuffle(l); print(l)

from random import shuffle
deck = FD(); shuffle(deck)
print(deck._cards)

#Instead of hardcoding to take only list in argument with class initiation
#We can take any iterable and convert that into list when and as required 
#if it behaves like a duck it probably is a duck - Duck Typing
def tryfield(field_names):
    try:
        field_names = field_names.replace(',', ' ').split()
    except:
        pass
    field_names = tuple(field_names)
    return field_names, len(field_names)
tup, _ = tryfield("A lot more than this, this is mine"); print(tup)

#Goose Typing - Subclassin on Abstract Base Class
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
    def __setitem__(self, position, value):
        self._cards[position] = value
    def __delitem__(self, position):
        del self._cards[position]
    def insert(self, position, value):
        self._cards.insert(position, value)
    
#__setitem__ is the required method for implementing the shuffle method
#ABCs in the standard library, Building an ad manangement framework called ADAM, User provided
#non-repeating random-picking classes. We will have total 4 methods in the ABC
# .load() and .pick() as abstract methods, .loaded() and .inspect() as conrete methods
import abc
class Tombola(abc.ABC):
    #We do not know yet how to pick and load, because that will dependent upon the content
    @abc.abstractclassmethod
    def load(self, iterable):
        """Add items from an iterable"""
    @abc.abstractclassmethod
    def pick(self):
        """Removing item at random and returning it
        Lookup Error when there is nothing in there"""
    def loaded(self):
        return bool(self.inspet())
    def inspect(self):
        """We are not having any definition of the pick() and the load() methods so we are using, Concrete
        methods and emptying it, moreover conrete methods in ABCs can use other concrete and abstact methods """
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))

#Now we are going to use the abstact base class created above
import random
class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)
    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from Empty BingoCage')
    def __call__(self):
        self.pick()
    


