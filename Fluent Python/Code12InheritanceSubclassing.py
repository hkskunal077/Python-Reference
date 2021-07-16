#Inheritance: For Good or For Worse
#Subclassing Built-In Types is tricky
class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value]*2)

#Default action taken by DICT parent class
dd = DoppelDict(one=1); print(dd)
#Overriding of the __setitem__ method by the parent class 
dd['two'] = 2; print(dd)
#Here it wont be overriddena and the dictionary default works
dd.update(three=3); print(dd)
#So we cannot always override the built-in types

class AnswerDict(dict):
    def __getitem__(self, key):
        return 42
#AnswerDict's __getitem__ method overrides the default dicts
ad = AnswerDict(a='foo');print(ad['a'])
#Dict.update method ignored our AnswerDict.__getitem__
d= {}; d.update(ad); print(d['a'])

#Subclassing of built-in types is generally error prone 
#should be avoided mostly, instead we can use their alternatives
#from collections we can import User Dicts
#Method Delegation in C programming language
#Should use <UserDict> and <MutableMapping>
import collections
class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(self, key, [value]*2)

class AnswerDict2(collections.UserDict):
    def __getitem__(self, key):
        return 42

#Naming Conflicts in Multiple Inheritance and Resolution Order
class A:
    def ping(self):
        print('ping:', self)
class B(A):
    def pong(self):
        print('pong:', self)
class C(A):
    def pong(self):
        print('PONG:', self)
class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping:', self)
    
    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)
#Method Resoultion Order (MRO)
d=D(); d.pong(); C.pong(d)
print(D.__mro__)
print(dict.__mro__)

def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))

import tkinter
print_mro(tkinter.Text)

#Multiple Inheritance in the Real Wor\ld
#Tkinter GUI toolkit uses Multiple Inheritance 
import tkinter; print()
print_mro(tkinter.Toplevel)
print_mro(tkinter.Widget)
print_mro(tkinter.Button)
print_mro(tkinter.Text)
