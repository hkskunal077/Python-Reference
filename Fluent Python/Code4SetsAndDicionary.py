#First-CLass Functions - Created at runtime
#assigned to a var in DS - passed as argument to functions
def factorial(n):
    """returns n!"""
    return 1 if n<2 else  n*factorial(n-1)

#Referncing Function as Object
print(factorial(42))
print(factorial.__doc__)
print(type(factorial))

fact10 = list(map(factorial, range(11)))
print(fact10)

#Higher-Order Functions
#Returns function, gets passed a function
frus = ["alpha", "beta", "gamma"]
print(sorted(frus, key=len, reverse=True))

#ListComps and Genexps > Map and Filter
print(list(map(factorial, range(6))))
print([factorial(n) for n in range(6)])
print(list(map(factorial, filter(lambda n: n%2, range(6)))))
print([factorial(n) for n in range(6) if n%2!=0])

#Reduce builtin function
from functools import reduce
from operator import add
import operator
print(reduce(add, range(100)))
#Preferred Way
print(sum(range(100)))

#Anonymous Functions
frus = frus
print(sorted(frus, key=lambda word: word[::-1]))

#The Call operator (), other than User Defined Functions 
#All types of Functions, Methods, Classes and Instances
print([callable(obj) for obj in (abs, str, 12)])

#UserDefined Callables
import random
class BingoCage:
    def __init__ (self, items):
        self._items = list(items)
        random.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from Empty BingoCage')
    
    def __call__ (self):
        """"This function tells us that now without accessing any 
        function we have made class callable from outside by  __call__ method"""
        return self.pick()

bcg = BingoCage([1,2,4])
print(bcg.__call__().__doc__)
print(bcg.pick(), callable(bcg))
print(dir(factorial), factorial.__init__)

#From positional to Keyword Only Parameters
#Keyword Only Argument, if cls is not mentioned it will never be capture
def tag(name, *content, cls = None, **attrs):
    """Generates one or more HTML Tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join('%s="%s"'%(attr, value) for attr, value in sorted(attrs.items()))
    
    else:
        attr_str = ''
    
    if content:
        return '\n'.join('<%s%s>%s</%s>'%(name, attr_str,c , name) for c in content)
    else:
        return '<%s%s />'%(name, attr_str)

print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
#This Functions exhausts all posible way of calling the HTML tags from Python

#Packages for Functional Programming
#Not a FPP, but FP guiding style can be used 
#operator module
from functools import reduce
def reduce_fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

from operator import mul
def fact(n):
    return reduce(mul, range(1, n+1))

#itemgetter and attrgetter
metro_data = [
            ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
            ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
            ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
            ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
            ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
            ]

from operator import itemgetter
#Here also we pass indices
for city in sorted(metro_data, key=itemgetter(2)):
    print(city)

cc_name = itemgetter(1, 0)
#creates a custom function that can take out specificity
for city in metro_data:
    print(cc_name(city))

from collections import namedtuple
Latlong = namedtuple('Latlong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
#coord = Latlong(lat=lat, long=long)
metro_areas = [Metropolis(name, cc, pop, Latlong(lat, long)) 
                for name, cc, pop, (lat, long) in metro_data]
print("\n\n",metro_areas)
print(metro_areas[0].coord.lat)

from operator import attrgetter
name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))
#List Comprehension created 
lc = [name for name in dir(operator) if not name.startswith('_')]
print("\n", lc)

from operator import methodcaller
s = "Code 4 Sets And Dictionary"
upcase = methodcaller('upper')
print(upcase(s))
hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))

from operator import mul
from functools import partial
triple = partial(mul, 3)
print(list(map(triple, range(100,104))))
