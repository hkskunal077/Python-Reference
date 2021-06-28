#Zip function 
#Takes multiple iterables to one iterable
x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c', 'd']

for a,b in zip(x,y):
	print(a,b)
#Pairwise bonding 
#For zipping x,y

for a,b,c in zip(z,x,y):
	print(a,b,c)
#In a way this fetches individual values a,b,c	
#Groupwise Indexed bonding across all lists
print(zip(x,y,z))
#It is a zip object not something that can be printed over 
for i in zip(x,y,z):
	print(i)	
#This fetches not the individual value but the iterable as all
#as a one set of obj

print(list(zip(x,y,z)))
#list from generator
print(dict(zip(x,z)))
#dict from a generator
 
 #for loops stores values if accessed with same variable name 
 #as the og
 #values might get over-written
 #Do not use same name for variables as well as iterables

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 

mapped = zip(name, roll_no, marks)
mapped =list(mapped)
print(mapped)


#unzipping
namez, roll_noz, marksz = zip(*mapped)
print(namez)
print(roll_noz)
print(marksz)
#we make the list of zipped structure and then just take 
#some new variables and unzip it with zip(*zipped_list)

