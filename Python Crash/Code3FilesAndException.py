# we work with files to analyse the data 
# organised code
# json module which allows user to save your data


#Reading from a File 
# text files contain important data for usage 

#readin an entrire file 
#let us start file handling 
file_path = 'C:\SublimeText3Python\PythonCrash\#3_Function_Class_File_Testing\pi_digits.txt'
with open(file_path) as file_object:
	contents = file_object.read()
	print(contents.rstrip())

	

#open() function returns the file as an object so the obect now needs a name 
# (with) closes the files ince they are no longer needed
# poorly written close() command gives error
#read() cmd reads the entire content and stores it as a ONE long string 
#there will be an empty line after printing contents of this file 
#it returns an empty strings
#We can give paths 


with open('pipi.txt') as new_file_object:
	for line in new_file_object:
		print(line.rstrip())



with open('piagain.txt') as new_temp_file_object:
	lines = new_temp_file_object.readlines()


for l in lines:	
	print(l.rstrip())	


#working with a file's content 

pi_string = '' 
#Here it is a string 
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))	
#we basically did string concatenation



new_file_name = 'pilakh.txt'

with open(new_file_name) as new_mega_fileobject:
	lines = new_mega_fileobject.readlines()


for line in lines:
	print(line.strip())

print("\n"+ str(len(lines)))

prompt = "Enter ur b'day as mmddyy: \n"
birthday = input(prompt)

if birthday in lines:
	print("in pi")
else:
	print("stfu")

	
