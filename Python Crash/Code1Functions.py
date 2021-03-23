# We will go through functions and creating modules to  organise main program files
#use the DocString to define what function does
#formal: parameter
#actual: argument

#positional arguments
#order of arguments

def describe_pet(animal_type, pet_name):
	"""Display info about a pet."""
	print(" I have a "+ animal_type)
	print("\nIt's name is "+ pet_name)

describe_pet('hamster','harry')	
#1-1 matching of parameter type and argument type 
describe_pet('çat','lucy')


#keyword argument 
#it is a name-value pair 
#frees from STRICT ordering in functional calls
#Here we explicitly tell python which argument i am passing 

describe_pet(animal_type='dog',pet_name='bruno')
describe_pet(pet_name='missi',animal_type='cat')
#the NAME-VALUE binding, for easy approach
#use the exact names of the parameters always\

#Default values
#if provided then use that otw use default value

def describe_lang(lang_name,lang_type='Compiled Language'):
	"""Display info abt computer languages"""
	print("The language is "+ lang_name)
	print("It is a "+ lang_type)


describe_lang('C++')
describe_lang('Python', 'Interpreted Language')
describe_lang(lang_type='Interpreted Language',lang_name='PHP')
#Default arguments working 

print("\n")
#Return Values 	 
def getfname(firstname,lastname):
	fullname= firstname+" "+ lastname
	return fullname.upper()

musician = getfname('Michael','Jackson')
print(musician)


#Returning a Dictionary 
def build_person(fname,lname,age=''):
	person = {'first':fname, 'last':lname}
	if age:
		person['age']=age
	return person

dancer = build_person('Tobey','Maguire')
print(dancer)	
dancer2 = build_person('Jimmy','Rocko',34)
print(dancer2)
#returnign a dictionary as usual
#with default arguments


while True:
	print("Tell me ur name: ")
	print("type 'quit' to exit")

	namefirst = input("What is ur first name\n")
	if namefirst == 'quit':
		break

	namelast = input("What is ur last name: \n")
	if namelast == 'quit':
		break

	print(getfname(namefirst,namelast))







