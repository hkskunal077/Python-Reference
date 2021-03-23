# writing a file 

file_name = 'programming_wsl.txt'
with open(file_name,'w') as file_object:
	file_object.write("I love space\n")
	file_object.write("I just want to be there\n")
	#writing multiple lines

#read mode r
#read and write mode r+
#append mode 

new_file_name = 'progr.txt'
with open(new_file_name,'a') as new_file_object:
	new_file_object.write("\nIt helps connect and model real world\n")
	new_file_object.write("It helps to better understand the computers also\n")




 
