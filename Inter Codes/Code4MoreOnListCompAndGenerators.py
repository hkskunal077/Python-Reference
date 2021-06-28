

temp = [i for i in range(1000)]
print('Done')
#This assigns the value into memory

new_temp = (i for i in range(1000))
print('DoneDone')
#generator Doesn't store


input_list = [5,6,2,10,15,20,5,2,1,3]

def div_by_five(num):
	if num%5==0:
		return True
	else:
		return False


xyz = (i for i in input_list if div_by_five(i)) 
#Generator
#Logic Working
# xyz= []
# for i in input_list:
# 	if div_by_five(i):
# 		xyz.append(i)
# #Explicit Assigning of values		

# for i in xyz:
# 	print(i) 
#Passing from generators it becomes itself an ITERABLE ITEM
[print(i) for i in xyz]
#LC
[print(i**2) for i in range(10)]
#LC
#We can directly issue commands from LIST COMPREHENSIONS 
#List compehension are one_liners for loops
xyz = (i for i in input_list if div_by_five(i)!=True)
[print("Hola Amigos") for i in xyz]
#We will check if we can use same generator multiple times


[[print(i,ii) for ii in range(5)] for i  in range(5)]
#comes form outer to inner 
#Nested List comprehensions
#u can in a way look it as BACKWARDS

new_list = [[[i,ii] for ii in range(5)] for i in range(5)]
print(new_list)
#U can make the assigned value either a list or a tuple
new_temp_list = ([[i,ii] for ii in range(5)] for i in range(5))
print(new_temp_list)
#no printing just a generator expr

[print(i) for i in new_temp_list]

# [print(i**2) for i in new_temp_list]
#This does not do anything it 
#beacuse the generator has been used first


