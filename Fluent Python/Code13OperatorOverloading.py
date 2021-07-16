#Operator Overloading
#Operators cannot be overloaded for the built-in types
#Can only overload existing operators
from array import array
import fractions
import re
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
        # hashes = map(hash, self._components) 
        # Works like a generator expression, lazy code 
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__ (self):
        return math.sqrt(sum(x*x for x in self))

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self) 
    
    #overlaoding the + operator for the vector
    def __add__(self, other):
        import itertools
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(a+b for a, b in pairs)
        #Return type must be of the same type
    
    def __radd__(self, other):
        return self + other
    
    def __mul__(self, scalar):
        import numbers
        if isinstance(scalar, numbers.Real):
            return Vector(n*scalar for n in self)
        else:
            return NotImplemented
            
    def __rmul__(self, scalar):
        return self*scalar

    def __eq__(self, other):
        if isinstance(other, Vector):
            return (len(self) == len(other) and 
                all(a==b for a, b in zip(self, other)))
        else:
            return NotImplemented

    @classmethod
    def frombytes(cls, octets):
        cls_object = cls 
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

vector= Vector((1, 2, 3))
print(vector, "\n", vector.__str__())
#Operator Overloaded expressions
print(vector.__neg__(), "\n", vector.__neg__().__neg__())
from fractions import Fraction
v1 =Vector((20, 24, 28))
print(v1*Fraction(1, 4))
va = Vector([1.0, 2.0, 3.0])
#vb = Vector((1.0, 2.0, 3.0))
vb = Vector(range(1, 4))
print(va is vb, "\n", va == vb)
#Augmented Assignment Operators

