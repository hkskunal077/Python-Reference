# [i for i in range(5)]
# (i for i in range(5))
# #These are actually lazy ways of generating generators

# #generator do not return they YIELD
# #they are basically in a way functions that
# #YIELD instead of returning a value 

# def simple_gen():
# 	yield 'OH'
# 	yield 'Hello'
# 	yield 'There'

# print(list(simple_gen()))
# #making list form generator

# for i in simple_gen():
# 	print(i)	
# #Actually iterating over a list


#writing generator
import timeit
CORRECT_COMBO = (9, 9, 0)

# found_combo = False
# for c1 in range(10):
# 	for c2 in range(10):
# 		for c3 in range(10):
# 			if (c1, c2, c3) == CORRECT_COMBO:
# 				print('For combo: {}'.format((c1,c2,c3)))
# 				found_combo =True
# 				break
# 				print(c1,c2,c3)



#break statement is pretty ineffective here
#because it breaks out of only one loop

#In a way we can make use 3 loops to One loop

'''THIS IS A CLEANER WAY'''
def combo_gen():
	for c1 in range(10):
		for c2 in range(10):
			for c3 in range(10):
				yield (c1, c2, c3)
#yield here means that it generates it in that order 				
#this generator is in a way saving us memory 
#and no need to make it in put
#we can have one simple loop to iterate over 				


for (x,y,z) in combo_gen():
	print(x,y,z)
	if (x,y,z)== CORRECT_COMBO:
		print('Found the combination: {}'.format((x,y,z)))
		break				

print(timeit.timeit('''CORRECT_COMBO = (9, 9, 0)

# found_combo = False
# for c1 in range(10):
# 	for c2 in range(10):
# 		for c3 in range(10):
# 			if (c1, c2, c3) == CORRECT_COMBO:
# 				print('For combo: {}'.format((c1,c2,c3)))
# 				found_combo =True
# 				break
# 				print(c1,c2,c3)



#break statement is pretty ineffective here
#because it breaks out of only one loop

#In a way we can make use 3 loops to One loop

#this is a cleaner way
def combo_gen():
	for c1 in range(10):
		for c2 in range(10):
			for c3 in range(10):
				yield (c1, c2, c3)
#this generator is in a way saving us memory 
#and no need to make it in put
#we can have one simple loop to iterate over 				


for (x,y,z) in combo_gen():
	print(x,y,z)
	if (x,y,z)== CORRECT_COMBO:
		print('Found the combination: {}'.format((x,y,z)))
		break				
''', number = 1000))