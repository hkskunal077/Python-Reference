#if statements
#logical constraints
cars= ['bmw', 'audi', 'toyota', 'subaru']

for car in cars:
	if car=='bmw':
		print(car.upper())
	else:
		print(car.lower())

#if case does matter then by default 
#if case does not matter then 

car2='Audi'
print(int(car.lower()=='audi'))
	
#checking fot inequality
requested_topping= 'mushrooms'			

if (requested_topping!='anchovies'):
	print("Hold the anchovies!!")

#We can also check multiple condition
age_1= 23
age_2=29
print(age_1>=20 and age_2<=30)
#we can use (and) statements as it is
new_topping=['pineapple', 'tomato', 'mushroom']
print(int('tomato' in new_topping))
# tomato exists in new_toppings 
topping='onion'
if topping not in new_topping:
	print("heya")

#not in is a vaild keyword in py3

#boolean expr
#they are efficient and used for state of a program
requested_toppings= ['mushrooms', 'green peppers', 'extra cheese']

#requested_toppings=[]

if requested_toppings:

	for reqtop in requested_toppings:
		if reqtop=='green peppers':
			print("Sorry we are out of "+reqtop+"\n")
		else:	
			print("Adding "+reqtop)

	print("\nFinished making ur Pizza")
else:
	print("You sure u want a plain pizz")

#To check if list is empty or not
# we do if list_name:  (This is true if it non-empty)
print("\n")

available_top=['mushroom','olives','green peppers',
			  'pepperoni','pineapple','extra cheese']

requested_top=['mushroom', 'french fries', 'extra cheese']	

for top in requested_top:
	if requested_top in available_top:
		print("Adding "+top+".")
	else:
		print("Sorry!! We ran out of "+ top +".")

print("Pizza Completed")


for requested_top in available_top:
	print("e")