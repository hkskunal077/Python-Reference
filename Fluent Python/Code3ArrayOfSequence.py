#built in - list, tuple, collections - referentials
#flat sequences - str, bytes, array - memory flat

#List Comprehensions and Generator Expressions
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    #ord to check the unicodes
    codes.append(ord(symbol))
print(codes)
#LC - only one use - To Build List
codeslc = [ord(symbol) for symbol in symbols]
print(codeslc)

# (ListComps) vs (Map and Filter)
beyond_ascii = [ord(s) for s in symbols if ord(s)>127]
#Map and Filter
#<createList>(filter(<lambda expression>, map(func_for_all_item_of_list, data_list)))
beyond_ascii = list(filter(lambda c: c>127, map(ord, symbols)))
new_list = list(filter(lambda a: a<222, map(ord, symbols)))
print(beyond_ascii, new_list)

# Cartesian Products using LC
colors = ['black', 'white']
sizes = ['S','M','L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

#List Comprehensions can help us build list only
#For building other containers and built in, flats we use <genexps>

#Generator Expressions
#To init Tuple, Arrays, sequence and other types of sequences 
#genexps saves  memory bt yielding items one by one using iterator protocol
#instead of building while list just to feed another constructor
genexpTuple = tuple(ord(symbol) for symbol in symbols)
print(genexpTuple)
import array
from this import s
from typing import ChainMap
#We needed the first parameter as the <storageType> and () for calling genexp 
genexpArray = array.array('I', (ord(symbol) for symbol in symbols))
print(genexpArray[0], genexpArray[1], genexpArray)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s'%(c,s) for c in colors for s in sizes):
    print(tshirt)
#Tuples can work as Records because of its unpacking mechanism
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    #Tuple Unpacking
    print('%s/%s'%passport)

import os
_, filename = os.path.split('/home/kunal/idrsa.pub')
print(filename)

#Nested Tuple Unpacking
#Undone, still formatting needs to be learned

#Named Tuples
from collections import namedtuple
#We can use + and * with tuples, they multiply the strings along length

board = [['_']*3 for i in range(3)]
board[1][2] = 'X'; print(board)

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits, reverse=True, key=len))
#Functions that change an object must return None to the Python

import bisect
import random
SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list) 

#all builtins live in __builits__.__dict__
#Python uses hash tables implementation for high performing dictionaries 
from collections import abc
my_dict = {}
print(isinstance(my_dict, abc.Mapping))
# ABC - Abstract Base Class for all container types
#in collections.abc - test whether a class provides
#a particular interface, hashable or mapping.
#Something is hashable if it has a hash value that never changes during its
#lifetime (needs a __hash__()), for comparison __eq__() method
tt = (1,2,(30,40))
tt2 = (1,2,[20, 40])
print(hash(tt)); 
tt2 = (1,2, frozenset([30, 40]))
print(hash(tt2))

a = dict(one=1, two=2, three=3)
names = ["one", "two", "three"]
nums = [1, 2, 3]
b = dict(zip(names, nums))
print(a==b) #Same Dictionaries

#Dict Comprehensions
DIAL_CODES = [(86, 'China'),(91, 'India'),(1, 'United States'),(62, 'Indonesia'),(55, 'Brazil'),(92, 'Pakistan'),(880, 'Bangladesh'),(234, 'Nigeria'),(7, 'Russia'),(81, 'Japan')]
#For comps we need corresponding <braces> and <ops>
country_code = {country:code for code, country in DIAL_CODES}
print(country_code)

country_code = {code:country.upper() for country, code in country_code.items()}
print(country_code)

import builtins
pylookup = ChainMap(locals(), globals(), vars(builtins))
print(len(pylookup))

#Mapping that holds integer count for each key
import collections
ct = collections.Counter('Extended Survival Analytic Model in Finance')
print(ct.most_common(1))
#To count the occurence just use collections Counter which keeps Integer Count

#Subclassing User Dictionaries
# Set Theory
#Mutable Sets are there in Python and Immutable frozenSets are also there
#Collection of unique objects
largeInfo = ['Spamming', 'Spamming', 'Non-Spamming']
#print(set(largeInfo)); print(list(set(largeInfo)))
largeInfo = list(set(largeInfo))
print(hash(largeInfo[0]), hash(largeInfo[1]))

largeInfo = ['Spamming', 'Spamming', 'Non-Spamming']
largeInfo = set(largeInfo)
# All Set Theoretic Notation
print(largeInfo | largeInfo, largeInfo & largeInfo, largeInfo - largeInfo)
found = len(set(largeInfo) & set(largeInfo)); print(found)

# Set Comprehensions
from unicodedata import name
setcomps = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(setcomps, type(setcomps))

#Funtions and methods additional functionalities, OOPS terminologies       





