#Dictionaries 
#dictionaries help in modelling the real world code
#For stroing details abt an object(somewhat like struct)

alien_0={'color': 'green', 'point': 5}

print(alien_0['color'])
print(alien_0['point'])

#dictionary is a collection of KEY_VALUE PAIRS

total_points= alien_0['point']
print("U just earned "+str(total_points)+" points!")

print(alien_0)

alien_0['xposition']=0
alien_0['yposition']=0
#asigning the same way as accessing it 
print(alien_0)


alien_1={}
alien_1['color']='green'
alien_1['point']=10
alien_1['xposition']=20
alien_1['yposition']=30
print(alien_1)

alien_0['speed']='medium'
print(alien_0)
print("Og x position: "+str(alien_0['xposition']))

if alien_0['speed']=='slow':
	x_increment=1

elif alien_0['speed']=='medium':
	x_increment=2
else:
	x_increment=3


alien_0['xposition']+=x_increment
print("New position is: "+str(alien_0['xposition']))
	 

del alien_0['point']
print(alien_0)

#we can use poll to store information on simple polls

favourite_lang={'jen':'C','paul':'C++','Phil':'Ruby','Drake':'Python'}
print(favourite_lang)

print("Paul's favourite language is "+ favourite_lang['paul'].upper()+".")

#looping through a dictionary 
#looping through key-value pairs
for key,value in alien_0.items():
#item() return key-value pairs
	print("Key "+ key)
	print("value "+ str(value))
#we implicit convert int to str() type 


#Looping through keys only
friends = ['Phil','sarah']
for name in favourite_lang.keys():
	print(name.upper())

	if name in friends:
		print("Hi "+name.upper()+", I see ur favourite language is "+
		      favourite_lang[name].upper())

if 'erin' not in favourite_lang.keys():
	print("Erin please enroll in our poll")


for name in sorted(favourite_lang.values()):
	print("These are some favourite languages of people "+name.upper())


#Nesting 

#a set of dictionary in a list or a list of items as a value in dictionary
print(alien_0)
print(alien_1)

alien_3= {'color':'green', 'point': 20, 'speed':'fast'}
alien_3['xposition']=50
alien_3['yposition']= 50
print(alien_3)


#we have 3 aliens ready 
alien = [alien_0,alien_1,alien_3]
print("\n")
for name in alien:
	print(name)

