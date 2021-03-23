# Exceptions and Exception handling 
# try-except for handling either cases 

#print(5/0)
#ZeroDivisionError: - exception object
#using TRY-EXCEPT

try:
	print(5/0)
except ZeroDivisionError:
	print("You cannot divide by zero!!")
#if TRY works python skips except block and go forwards
#if it generates error, then use EXCEPT
#error from TRY looks for EXCEpt block with same error

print("Give two numbers for division")
print("Enter q to quit: ")
active = False
while active:

	first_number = input("\nFirst number: ")
	if first_number=='q':
		break

	second_number = input("\nSecond number: ")
	if second_number=='q':
		break

	try:
		answer= int(first_number)/int(second_number)

	except ZeroDivisionError:
		print("Can not divide by Zero!! bruh!!")	

	else:
		print("answer is "+ str(answer))			

	#If we have some another work to be done after TRY block successfully 
	#completes then we use 
	# ELSE block





#Handling the FileNotFoundError Exception

file_name = 'rubyonrails.txt'
try:
	with open(file_name) as new_file_obj:
		contents = new_file_obj.read()

except: 
	print("Sorry the file "+ file_name + " does not exist")

else:
	print("haha file read")



