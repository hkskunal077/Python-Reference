#Iterables, Iterators and Generators 
#Building Iterators Patterns
from abc import abstractmethod
import re
import reprlib
from typing import NewType
RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    #__getitem__ automatically creates an iterator inside
    def __getitem__(self, index):
        return self.words[index]
    def __len__(self):
        return len(self.words)
    def __repr__(self):
        """"Showing as part of the sentence class within"""
        return 'Sentence(%s)'% reprlib.repr(self.text)

sentence = Sentence("self.words holds the result of .findall, so we simply return the word at the given index")
print(sentence.__len__(), "\n", sentence.__repr__(), "\n", sentence[10])
print(sentence.words, "\n", globals(), "\n\n")
print([str(globals()[name])+" " for name in globals()])
#Since the getitem protocol is implemented, that automatically creates
#__iter__ instances

class iterable:
    """Built-In Iterator defined function"""
    def __iter__ (self):
        pass
iter = iterable()
from collections import abc 
print(issubclass(iterable, abc.Iterable), isinstance(iter, abc.Iterable))

#Iterable = Any object from which the iter built-in function
#can obtain an iterator. __iter__ special methods 
#The standard interface for an object is __next__
from collections.abc import Iterable
class Iterator(Iterable):
    __slots__ = ()
    @abstractmethod
    def __next__(self):
        raise StopIteration
    def __iter__(self):
        return self
    @classmethod
    def __subclasshook__(cls, C):
        """This default method helps us in using isinstance and abc.Iterator"""
        if cls is Iterator:
            if (any("__next__" in B.__dict__ for B in C.__mro__) and
                any("__iter__" in B.__dict__ for B in C.__mro__)):
                return True
        return NotImplemented
    
s3 = Sentence('AppData and Locales')
#it = iter(s3); print(it)
#Iterator is any Python object that implements __next__ method
#with jumptt and raise property and iterator has __iter__ itself
import re
import reprlib
RE_WORD = re.compile('\w+')
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    def __repr__(self):
        return 'Sentence(%s)'%reprlib.repr(self.text)
    def __iter__(self):
        return SentenceIterator(self.words)

class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0
    def __next__(self):
        try:
            #We used the defaul list.__iter__ to construct
            #SentenceIteator.__next__ method in class
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word
    def __iter__(self):
        return self

#Key Difference is ITERABLE has __iter__ method
#and the corresponding ITERATOR has __next__ 
#and __iter__ method alongside 
print(issubclass(SentenceIterator, abc.Iterator), 
isinstance(SentenceIterator, abc.Iterator), 
isinstance(Sentence, abc.Iterable),
issubclass(Sentence, abc.Iterator))
#Only SentenceIterator having the __next__ and __iter__ method works.
#We should implement the iterator as separate class iter(my_iterable)
#An Iterable should never act as an iterator over itself.

import re
import reprlib
RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    def __repr__(self):
        return 'Sentence(%s)'%reprlib.repr(self.text)
    def __iter__(self):
        """finishes when done providing values"""
        for word in self.words:
            yield word
        return
sentence = Sentence('Appdata and Locales')
print(sentence.__iter__.__doc__, sentence.__iter__)

#Lazy Evaluation of Sentence Take
import re
import reprlib
RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
    def __repr__(self):
        return 'Sentence(%s)'%reprlib.repr(self.text)
    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


#Generator Expression 
import re
import reprlib
RE_WORD = re.compile('\w+')

class Sentence:
    #Since the generator Expression yeilds it using Lazy Evaluation
    #It is better to use GexExps instead of ListComps
    def __init__(self, text):
        self.text = text
    def __repr__(self):
        return 'Sentence(%s)'%reprlib.repr(self.text)
    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))
print(Sentence('AppFiles and Disc').__iter__())

#Arithmetic Progression Generator
#When items are produced at fly, instead of retrieving from a collection
class ArtihmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end #None -> "infinite" series
    def __iter__(self):
        #Typecasted the type of step to begin
        result = type(self.begin+self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result<self.end:
            yield result
            index += 1
            result = self.begin + self.step*index
print(ArtihmeticProgression(1, 2, 3).__iter__.__dir__())
print(ArtihmeticProgression(1, 2, 3))
print(tuple(list(ArtihmeticProgression(1, 2, 10))))
from fractions import Fraction
print(tuple(ArtihmeticProgression(0, Fraction(1, 3), 2)))

#Corresponding Generator Expression 
def arithprog_gen(begin, step, end=None):
    result = type(begin+step)(begin)
    forever = end is None
    index = 0
    while forever or result<end:
        yield result
        index += 1
        result = begin + step*index
print(tuple(list(arithprog_gen(1, Fraction(1, 3), 2))))

import itertools
gen = itertools.takewhile(lambda n: n<2, itertools.count(1, .2))
print(tuple(list(gen)))
