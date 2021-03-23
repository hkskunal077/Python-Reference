import unittest
from name_function import get_formatted_name 
#first we import unittest and the function we want


#this is just a random name for the testing class 
class NamesTestCases(unittest.TestCase):
	"""Tests for 'name_function.py'."""

	def test_first_last_name(self):
		#this is a method, single test case (unit test )
		formatted_name = get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')
		#These tests were for the people with two worded names

	def test_first_last_middle_name(self):
		#for people with middle names 
		formatted_name = get_formatted_name('Wolfganfg','Mozart','Amadeus')
		self.assertEqual(formatted_name, 'Wolfganfg Amadeus Mozart')		


#Any method that starts with test_ will run automatically
#for function func.py use test_func.py


unittest.main() 	
#This tells python to test the unit test in this file only

