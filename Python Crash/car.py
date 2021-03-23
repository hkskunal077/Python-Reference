""" A Class that can be used to represent a car"""
from carcolor import Color
#This color funtionaity was not defined here so we need to import 

class Car():
	"""Modeling a Car"""

	def __init__(self,make,model,year):
		"""initialise attributes to describe a car"""
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0 #setting a default valur for an attribute
		self.petrol=4


	def get_description(self):
		"""Formatted Descriptive Name"""
		long_name = str(self.year)+' '+self.make+' '+self.model
		return long_name.title()

	def read_odometer(self):
		print("This Car has "+ str(self.odometer_reading)+" miles on it")

	def update_tank(self,petrol):
		"""Updating the amt of petrol"""
		self.petrol+=petrol # we could have assigned the complete new value or do a logical expression
	
	def update_odometer(self,mileage):
		if mileage>=self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("U cannot roll back bruh")	



# my_go = Car('renault','duster','2015')
# print(my_go.get_description())


class Battery():
	"""modelling an electric car battery"""

	def __init__(self,battery_size=70):
		self.battery_size= battery_size

	def describe_battery(self):
		print("This car has a "+ str(self.battery_size)+"-kwh battery")

	def get_range(self):
		if self.battery_size==70:
			range = 240  
		elif self.battery_size==90:
			range = 350
		else:
			range==400			

		message = "This car after complete charge can go "+ str(range)
		message += "km approximately"	
		print(message)
##############################################################################
class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles."""
	def __init__(self,make,model,year): # To have similarity have defined this__init__
		super().__init__(make,model,year)# After that we have derived __init__() def from super()
		self.battery = Battery()
		self.color= Color()
		#This means that when we use battery in Electric Cat it refers to battery class's
		#ATTRIBUTES AND FUNCTIONS		

	def petrol_refilling(self,petrol): #This means whatver i want to inherit 
		super().update_tank(petrol) # petrol_refilling is equivalent to update_tank method of Superclass
	#We have to separately define all those attr, methods() to be derived in subclass 