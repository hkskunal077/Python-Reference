#Introducing Lists 
#A list is a collection of items in a particular order
bicycle= ['trek', 'cannondale', 'redline','specialised']
print(bicycle)
#py interprets lists and prints as list too
print(bicycle[0].upper())
#ofc we can use index to access but we can also use other way of indexing 
print(bicycle[-1].upper())
print(bicycle[-2].upper())
message= "My first bicycle was a "+ str(bicycle[1].upper())+" type of bicycle"
print(message)
#the elements of list were already str() type so no need

bike=['honda', 'yamaha', 'suzuki']
print(bike)
bike[0]='ducati'
print(bike)
#we can add elements in a list at the end

bike.append('BMW')
print(bike)
#elem appended at the EOL
#instead of appending we can do isnertion by specifying indexes
bike.insert(2, 'Honda')
print(bike)
#This shifts other values to the right
#For deleting use del
del bike[1]
print(bike)
#elem shifts back 1 place 
#This actually deletess that elem and now u canot work with that elem

#instead we sometimes use pop() so we can remove elem form list and work upon it
popelem_bike=bike.pop()
print(bike)
print(popelem_bike)
# we can also pop elem in at a specific position
first_owned=bike.pop(1)
print(first_owned)
print(bike)
#pop() function takes arguement the index which is to be popped
bike.append('KTM')
print(bike)
bike.remove('KTM')
print(bike)

#Organising a List
cars= ['bmw', 'audi', 'toyota', 'subaru']
#assuming all small case
cars.sort()
print(cars)
#for reverse sortng
cars.sort(reverse=True)
print(cars)

#sorted() function lets u display ur order of a list but does not actually 
#change it 
cars= ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print("Sorted temp list:")
print(sorted(cars))
print("Og list again:")
print(cars)
cars.reverse()
print(cars)
#using length os list
print(len(cars))
#avoiding index errors when working with lists

