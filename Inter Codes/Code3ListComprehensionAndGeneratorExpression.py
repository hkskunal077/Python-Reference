xyz = [i for i in range(5)]
print(xyz)
#Take values os i for i in range(5)

xyz = [i**2 for i in range(5)]
print(xyz)
#it takes value based on a function with domain i

xyz = []
for i in range(5):
 	xyz.append(i)
print(xyz)	 
#Explicit  loading of list



#Generators   
xyz = (i for i in range(5))
print(xyz)
#It is not actually making and storing our list
#Rather it is just a resource available for all of us 
#xyz is now an iterable shit

for num in xyz:
	print(num)



temp = [i for i in range(1000000000)]
print('Done')

new_temp = (i for i in range(10000))
print('DoneDone')