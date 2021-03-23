#Storing Data
#We use JSON module 
#jAVAsCRIPT oBJECT nOTATION (json)
# it helps dump DS into a file and load the data from that file 
#the next time programme runs 
#To preserve some cchoice of data

#Using json.dump() and json.load() 

import json

# numbers = [2,3,5,7,11,13,17,19]

# file_name = 'numbers.json'
# with open(file_name,'w') as new_file_object:
# 	json.dump(numbers,new_file_object)
# #parameters are DS and aliased FileName 
# new_file_name = 'numbers.json'
# with open(new_file_name) as f_obj:
# 	primes=json.load(f_obj)
# #parameters are D only the aliased FileName	
# #print(primes)

# # saving and generating user data

username  = input("\nWhat is your username: ")

temp_file_name='username.json'
with open(temp_file_name,'w') as nf_obj:
	json.dump(username,nf_obj)
	print("\nWe will remember your user ID")


file = 'username.json'
with open (file) as temp_obj :
	username = json.load(temp_obj)
	print("\n\nWelcome back!! "+ username)

#json.load() and json.dump() 

#remember kind of function 

try:
	with open(file) as obj:
		username  = json.load(obj)
except FileNotFoundError:
	prompt="\nPlease provide ur username for authenticated user's list"
	username = input(prompt)

	with open(file, 'w') as obj:
		json.dump(username,obj)
		print("\nU are added to authenticated users!!")		
else:
	print("\n nWelcome back authenticated user "+ username +" for LOGIN")		