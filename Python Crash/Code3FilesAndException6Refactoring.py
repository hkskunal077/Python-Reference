#making one code into series of functions for better usability 
#making differenet function for returning username and greeting 
import json

def get_stored_name():
	"""GET stored name from username.json file"""
	filename = 'username.json'
	try:
		with open(filename) as file_object:
			username = json.load(file_object)
	except:
		return None
	else:
		return username

	


def greet_user():
	"""Greet the coming user by name"""
	username = get_stored_name()
	if username:
		print("Welcome Back "+ username+ " user")
	else:
		username = input("\nWhat is your UserName")
		filename = 'username.json'
		with open(filename,'w') as new_object:
			json.dump(username,new_object)
			print("\nAdded to authenticated Users")		



greet_user()
#This is for one user, we can save his/her info like this

#Each function has a single clear purpose
#After code completion use CODE REFACTORING for bettter understandability

