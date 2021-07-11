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

####################################################################################################################
####################################################################################################################

#Building custome Types that behave like Python Immutable type itself
#The best practice for a sequence constructor is to take data as iterable
from array import array
import reprlib
import math
from typing import Type
import functools, operator

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
        #We are basically slicing accordingly
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
    
    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        """Method operating on class but not with decorators"""
        cls = type(self)
        #if argument passed is a slice object of the class Slice
        if isinstance(index, slice):
            return cls(self._components[index])
        #if the argument passed is an integer
        elif isinstance(index, int):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls = cls))
    
    # This just the comparison of repr() 
    # def __eq__(self, other):
    #     return type(self) == type(other)

    #Better Comparison - Termwise
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        # Zip produces a generator of Tuples 
        for a, b in zip(self, other):
            if a != b:
                return False
        return True
    
    def __eq__(self, other):
        return len(self) == len(other) and all(a==b for a, b in zip(self, other))
    
    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        # hashes = map(hash, self._components) 
        # Works like a generator expression, lazy code 
        return functools.reduce(operator.xor, hashes, 0)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

vector = Vector([1, 2, 4])
print(abs(vector) is vector.__abs__())
#vector.__func__ is a function object in memory
#vector.__func__() /  func(vector) is the call to the function
print(type(abs(vector)) is type(vector.__abs__()), abs(vector))
print(vector.__abs__(), type(vector.__abs__()), bool(vector), vector.__bool__())
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

# The slice of a built-in needs to be of the same data type
# Since we need to follow the Sequqence Protocol we need 
# to analyze __getitem__, writing arguments 

class MySeq:
    def __getitem__(self, index):
        """receives a Tuple of the data internally and not the list"""
        return index
s = MySeq()
print(s[1], s[1, 2, 3], s[1:4:2, 7:9])
#Slice __getitem__ functionality 
print(slice, dir(slice)) # Slice is an object of the Slice class '
print(slice(None, 10, 2).indices(5))    

#With __getitem__ slicing, sequence protocols
smallVector = Vector(range(7))
print(smallVector[-1], smallVector[:], type(smallVector) is type(smallVector[2:4]))

# Vector 3 Operatot and Hash
import operator, functools
fVal = functools.reduce(operator.xor, range(6)); print(fVal)
print(hash(smallVector[2:5]))
print(smallVector is smallVector[:], smallVector == smallVector[:])

