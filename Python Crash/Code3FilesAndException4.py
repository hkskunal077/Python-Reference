# Analyzing text 
# There is a split() function which build lists from strings 

# msg = "Kunal is hustling"
# print(msg.split())

def count_the_words(file_name):
	"""It reads a file and checks the no. of words"""

	try:
		with open(file_name) as temp_file_object:
			contents = temp_file_object.read()
	except FileNotFoundError:
		#print("Sorry ur file DNE\n")
		pass # it will just pass the error generating code, so NP		
	else:
		print("The no. of words in this are "+ str(len(contents.split()))+ " words.\n")	


#Working with Multiple files 


# file_name='analyzing_text.txt.txt'
# count_the_words(file_name)

filenames = ['analyzing_text.txt.txt','analyzinganother.txt.txt','siddhartha.txt','analyzingonemore.txt']
for name in filenames:
	count_the_words(name)




