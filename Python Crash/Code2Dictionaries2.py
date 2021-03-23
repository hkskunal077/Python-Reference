#Code that generates aliens
aliens = [ ]

for x in range(1,31):
	new_alien = {'color':'green', 'points':5, 'speed': 'fast'}
	aliens.append(new_alien)

for name in aliens[:]:
	print(name)

print("\nNumber of Aliens are "+ str(len(aliens))+ "\n")

for alien in aliens[:3]:
	if alien['color']=='green':
		alien['color']='yellow'
		alien['speed']='fast'
		alien['points']= 10

for name in aliens[:]:
	print(name)

#We have dictionaries in a list


# A list in a Dictionary
#Store information abt Pizza being made

pizza= {'crust':'thick',
		'toppings': ['mushroom','extra cheese'] }

#summarizing the order 
print("You ordered a "+ pizza['crust']+"-crust pizza"+ 
	   " with the following toppings:")

for topping in pizza['toppings']:
	print(topping)

#If we need more than ONE value associated with ONE key, then use list in the
#very defintion

fav_lang = {
	
	'jen': ['python','ruby'],
	'sarah': ['C'],
	'edward': ['ruby','go'],
	'phil': ['python','haskell']
	}

for name,lang in fav_lang.items():# .items() because we need both name and lang 
	print("\n" + name.title()+"'s favourite computer languages are:")
	for value in lang:  #iterator for an iterator
		print("\t"+ value.upper())



#A dictionary with a Dictionary 
#e.g. A dictionary of usernames containing info abt each user
print("\n")
print("\n")
users = {
	
	'aeinstein': {

		'first': 'albert',
		'second': 'einstein',
		'location': 'princeton'},


	'mcurie': {

		'first':'marie',
		'second':'curie',
		'location':'paris'}
}

for username,userinfo in users.items():
	print("\nUSERNAME: "+ username)
	full_name  = userinfo['first'] + " " + userinfo['second']
	location= userinfo['location']

	print("Full_Name: "+ full_name.upper())
	print("\tLocation: "+ location.upper())
	










