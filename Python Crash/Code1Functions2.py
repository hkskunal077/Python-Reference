#Passing a list in a function
def print_models(unprinted_designs,completed_models):
	"""Prints the unprinted designs"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing Model: "+ current_design)
		completed_models.append(current_design)
def show_completed_models(completed_models):
	print("\nThe following models have been printed")
	for d in completed_models:
		print(d)	
	print("\n")	

unprinted_designs = ['iphonecase','tetrahedron','pendant']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

unprinted_new_designs = ['necklace','ring']
comleted_new_models = []

print_models(unprinted_new_designs,comleted_new_models)
show_completed_models(comleted_new_models)

#Split function's functionality into many functions
#instead of using one comlex shitty function


#Preventing a function from modifying a list
#we use [:] complete SLICE ops for preventing a change in OG function
# we do print_models(unprinted_design[:], completed_models)




#Sometimes we initially do not know how many arguments to be passed onto a function
#So we use (*PARAMETER) and it collects any no. of arguments during 
#Calls of function of similar types
#In a way it is DYNAMIC

def make_pizza(size,*toppings):
	print("Making a " + str(size)+ " Pizza with the following toppings ")
	for top in toppings:
		print("----"+ top)


make_pizza(12,'pepporoni')	
make_pizza(10,'cheese','vosdaw')
make_pizza(15,'butter','pineapple','light cheese')

#Here the py interprets arguments as UNCHANGEABLE LISTS or TUPLES
#we have made now TUPLE accessible 
#we can also mix, positional and arbitrary arguments
#If u want several arguments but dynamic like this 
#put *PARAMETER at the last position




#When we need dynamic argument within dynamic argument as key -value pair
def build_profile(fname, lname, **user_info):
	profile= {}
	profile['first_name']=fname
	profile['last_name']=lname
	for key,value in user_info.items():
		profile[key]=value #The same way we use  dictionary for modification
	return profile


new_user_profile = build_profile('albert','eisntein',location='princeton',field='physics')
new_next_user_profile = build_profile('dennis','richie',location='AT&T',field='Software and Language Engineering')

print("\n")
print(new_user_profile)
print(new_next_user_profile)	
#Dynamic functional input and storage in as a Dictionary 




