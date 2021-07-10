#Building custome Types that behave like Python Immutable type itself
#The best practice for a sequence constructor is to take data as iterable
from array import array
import reprlib
import math

class Vector:
    #Every input will be a double
    typecode = 'd'

    def __init__(self, components):
        #We are using _var instead of var for data protection
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)
    
    def __repr__(self):
        components = reprlib.repr(self._components)
        #By now the _components and components
        #were holding the type of the data in sequence
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        #We have overloaded the + operator for adding 
        #Unicode representation to a bytes() data structure
        return (bytes([ord(self.typecode)])+
                bytes(self._components))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        #Cartesian Distance sqrt(a2 + b2 + c2 + ...)
        return math.sqrt(sum(x*x for x in self))
    
    def __bool__(self):
        return bool(abs(self))
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

#Protocols and Duck Typing
#Sequence Protocol - __len__ and __getitem__
#are entailed for it, any class that implements such 
#can be used anywhere where a sequence is expected.
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    #Way of initializing the list from a string
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        #Because they are inited everytime we start a class
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

fd = FrenchDeck()
print(fd[2])
