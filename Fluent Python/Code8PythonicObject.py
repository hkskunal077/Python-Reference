#From the Python Data Model
#Implementing Special Types
#Support BuiltIns, mini-lang, __slots__, read_only attrs
#Pythonic Objects
#User Defined Classes that can work as a Real Python Object 
#Duck Typing, Type/Class is less important as compared to the
#methods of the that Object

#Object Representation
#String Representation from an object (Standard Dynamic Lang)
#repr() - Developer wants to see
#str() - User wants to see

#Vector Class Redux
import math
from array import array, typecodes
class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    
    #This is done for making UNPACKING functions 
    #now outside the class we can write <x, y = my_vector>
    def __iter__(self):
        #We use a <GENEXP> for unpacking 
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        #It is coded in a way to represent a constructor call
        #Which gets pared in python as {className}{param1, param2}}
        class_name = type(self).__name__
        msg = '{}({!r},{!r})'.format(class_name, *self)
        #!r helps in calling the intrinsic repr method, *self feeds values
        return msg
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)])+
                bytes(array(self.typecode, self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))

    #Classmethod operates on the class and not the instances
    #Class itself is the argument, then the memory locations
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        #Since it is of variable length, it using *args
        return cls(*memv)

v1 = Vector2d(3, 4)
print(v1.x, v1.y)
x, y = v1; print(x, y)
#Unpacking by overriding the default methods 

v1_clone = eval(repr(v1))
print (v1 == v1_clone)
octets = bytes(v1); print(octets)

#An Alternative Constructive 
# Decorators @classmethod vs @staticmethod
class Demo:
    
    @classmethod
    def klassmeth(*args):
        return args
    
    @staticmethod
    def statmeth(*args):
        return args

print(Demo.klassmeth())
print(Demo.klassmeth('spam'))
print(Demo.statmeth())
print(Demo.statmeth('spam'))

#Formatted Display 
brl = 1/2.43
print(brl)
#Formats the way we want to format it and it truncates
print(format(brl, '0.4f'))
#We can pass the value to be formatted as the value from
#some other predefined values above the same
msg = '1 BRL = {rate: 0.2f} USD'.format(rate = brl)
print(msg) # <rate = brl> is not for formatting but values passes
#We use the concepts of <name mangling>, so if we have the variable
#as __name_ or __name it will become variable for the instance and not cls
print(v1.__dict__)

