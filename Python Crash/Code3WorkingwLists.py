#Working with Lists
magic=['alice', 'david', 'carolina']
for word in magic:
	print(word.upper()+", that is a cool trick")
	print("I can not wait for another trick "+word.upper()+"\n")
#here the iterator 'word' works as ref, we can use any of it
print("That was a great magic show")
#logic error is when syntax is correct but code does not
#produce desired result

#making numerical lists
#range() function helps in generation of series of number 
for value in range(1,5):
	print(value)
#off-by-one behviour
num_list=list(range(1,11))#jump by one 	
print(num_list)
num_list2=list(range(1,11,2))#jump by two
print(num_list2)

cube_list=[]
for value in range(11,21):
	cube = value**3
	cube_list.append(cube)
print(cube_list)	 
#one by one filling 
four_list=[]
for x in range(21,31):
	four_list.append(x**4)
print(four_list)

#for the list of numbers 
print(min(four_list))
print(max(four_list))
print(sum(four_list))
#min,max,sum are simple stat methods

#List Comprehensions allows us to generate list 
#and perform looping and creation of new elem in one line of code
five_list= [num**5 for num in range(2,11,2)]
print(five_list)
#This is list comprehension

#Workking with part of a List 
#Slicing 
players=['charles', 'bobby', 'david', 'morris', 'gatsby']
print(players[1:4])
print(players[:5])
print(players[0:])
print(players[:])

#the silce will create a shorter form of players
#an instance where we an loop through that

for val in players[1:4]:
	print(val.upper())
#we can omit the slice if we want from beginning to the end

best_players= players[:]
print(best_players)
#Copying list
#if we have done 
#best_players = players
#it would mean that both players and best_players 
#point to the same thing 
#like an alias

#TUPLES
# An immutable list is called a TUPLE
#just like alist except that we use ()
#instead of []

dimensions=(200,50)
#This is an IMMUTABLE LIST
#or a TUPLE

print(dimensions[0])
print(dimensions[1])
#id we try to change

#dimensions[0]= 100
#Tuple objects does not support assignment

#Looping through values in a tuple
for  dim in dimensions:
	print(dim)

#Writing over a tuple
#We can overwrite the complete variable 
#but not modify og values

dimensions=(300,100)	
for dim in dimensions:
	print(dim)

#we need common Styling for understandibility etc.
#Python Enhancement propoasal(PEP)
#TABS: 4 understand as spaces 

