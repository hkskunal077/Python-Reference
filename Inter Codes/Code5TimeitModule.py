#Timeit measures the time for certain SNIPPET of code
#Timeit runs the snippet of code multiple times to find 
#Statistically acurate piece of time required
import timeit
# print(timeit.timeit('1+3', number =100000000))

 
# input_list = range(100)
# def div_by_five(num):
# 	if num%5 == 0:
# 		return True
# 	else:
# 		return False


# xyz = (i for i in input_list if div_by_five(i))
# #Generator
# #those numbers in rabge(100) that satisfy div_by_five
# #Are taken as iterabels

# xyz = [i for i in input_list if div_by_five(i)]
# #List Comprehension

#number means that it repeats that many times to find thee minimum
#and plausibily the actual time
print(timeit.timeit('''input_list = range(100)
def div_by_five(num):
	if num%5 == 0:
		return True
	else:
		return False

xyz = (i for i in input_list if div_by_five(i))''', number =10000))
#Time when we form the generator TO be used
    
print(timeit.timeit('''input_list = range(100)
def div_by_five(num):
	if num%5 == 0:
		return True
	else:
		return False

xyz = [i for i in input_list if div_by_five(i)]''', number =10000))
#Time when we form list, or assgining memory

print(timeit.timeit('''input_list = range(100)
def div_by_five(num):
	if num%5 == 0:
		return True
	else:
		return False

xyz = list([i for i in input_list if div_by_five(i)])''', number =10000))

	 #Converting a generator to list 
#will take slightly longer than
#List comprehensions 


#Just pass the snippets of Code.
#It needs the complete code
#Timeit does not access other piece of code through scoping

#In general LC is little fastere than iterating with generatots.
