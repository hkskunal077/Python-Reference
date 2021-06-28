names = ['Jeff','Gary','Jill','Smantha']

# for name in names:
# 	print("Hello "+ name)
# 	print(' * '.join(['Hello',name]))

print(names)

print(', '.join(names))
#join is more preferable when joining multople strings together 

from os import path
location_of_files = 'C:\\Users\\H\\Desktop\\Inter_python'
filename = 'example.txt'

print(location_of_files + '\\' + filename)
#For joining anything everything

#This is the best way to combine name_space in sense of addresses
# with open(path.join(location_of_files,filename)) as f: 
# 	print(f.read())


#String Formatting
who = 'Gary'
how_many = 12
print(who, 'bought', how_many, 'apples')
print("{} bought {} apples".format(who,how_many))
#This is correct way of string formatting or plcaing 
#values of variables in its place
#we can also put indexs in those {} 

