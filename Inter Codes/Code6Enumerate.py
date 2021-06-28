#Enumerate returns the count alog the way and the items 
#To keep a track of iterations
example = ['left','right','up','down']
for i in range(len(example)):
	print(i,example[i])

#Whenever we use range(len) to denote the oterator
#there is a better way to do it
#using an Enumerate option
print("\n")

for i,j in enumerate(example):
	print(i,j)
#enumerte automatically assign the index to value
#dict() builds dictionary from normal lists 

new_dict = dict(enumerate(example))
print(new_dict)

[print(i,j) for i,j in enumerate(new_dict)]
