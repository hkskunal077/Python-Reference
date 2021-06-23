#Variables
name = "python dev"
#name.lower() -- for storing data as common
print(name.lower(), name.upper(), name.title())

last_name = " is OOPS derived"
print(name+last_name)

#rstrip(), lstrip() method for clearing out extra space in the end of the line
prog_lang = "pythonic thinking "
prog_lang.rstrip()
print(prog_lang)

#Lists Data Structure
#Dynamic, modifying is same as accessing element
#append, remove, del [], pop, insert, reverse
cars = ["bmw","audi","toyota","subaru"]
#Permanent Sorting using Method of Cars implemented class in the backend
cars.sort()
print(cars)
#Last element is -1
#Temporary Method using parameters
print(sorted(cars), len(cars))

#List Comprehensions
#generating list using single line of code
squares = [value**2 for value in range(1, 11)]; print(squares)

#Slicing of lists
print(squares[:4], squares[:-1], squares[-3:])
squaresCopy = squares[:]

#Tuple
#Immutable List that cannot be changed once created
dimesions = (200, 50)

#if statements
requested_toppings = ["mushrooms","green peppers","extra cheese"]
if not requested_toppings:
    print(requested_toppings[:])

requested_toppings_order = ["cheese", "green peppers"]
for topping in requested_toppings:
    if topping in requested_toppings_order:
        print(requested_toppings[:])

#Dictionary
#Key-Value Pair 
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['points'])
alien_0['x+position'] = 0
alien_0['y+position'] = 25
print(alien_0)

#del method for removing
del alien_0['points']
print(alien_0)

#Looping through a dict
for k, v in alien_0.items():
    print(k, v)
#items(), keys(), values()

#User inputs and while loops
# message = input("somth")
# print(message)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

#Functions
def describe_pet(animal_type, pet_name):
    print(animal_type+" "+pet_name)
describe_pet(pet_name="tomy", animal_type="dog")

#*args, **kwargs
def make_pizza(size, *toppings):
    print(toppings)
make_pizza("123", requested_toppings[0], requested_toppings[1])
#args=list, kwargs=dict

class Car():
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make; self.model = model; self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        return str(self.make)+str(self.year)+str(self.model)
    
    def read_odometer(self):
        print(str(self.odometer_reading))

    def update_odommeter(self, mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("no roll back!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
#inherited class
class ElectricCar(Car):
    """Represt aspect of a car, specific to electric vehicle"""
    def __init__ (self, make, model, year):
        #Derive and initialize everything from the super class of this inherited class
        super().__init__(make, model, year)
        self.batterySize = 70

myTesla = ElectricCar('tesla','model s', 2016)
print(myTesla.get_descriptive_name())
#We can override the methods from the parent class by redefining it in the child

#The Python Standard Libarary
#using import, from this import that etc method
#pip installations

#Files and Exceptions
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())

    pi_strings = ""
    lines = file_object.readlines()
    for line in lines:
        pi_strings += line.strip()
    
    print(pi_strings, len(pi_strings))
#with open(filePath) as fileObj:

filename = "programming.txt"
with open(filename, 'w') as file_object:
    file_object.write("tiswsaProgramming")
    file_object.close()

with open(filename, 'a') as obj:
    obj.write("terimappailelu")
    obj.close()

#try-except blocks
try:
    print(5/0)
except ZeroDivisionError:
    pass
else:
    print("fio")
#after trying something risky we can use the ELSE statement for furhter work 

#JSON module
#we can use this module to store information that user has entered
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as file_obj:
    json.dump(numbers, file_obj)
    file_obj.close()

with open(filename) as file_obj_read:
    print(json.load(file_obj_read))
    file_obj_read.close
    
