import math
from array import array
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
