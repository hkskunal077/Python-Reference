# def get_formatted_name(first,last):
# 	"""Generates a neately formattted full name"""
# 	full_name = first + " " +  last
# 	return full_name.title()


#Considering failingd functions

def get_formatted_name(first,last,middle=''):
	if middle:
		full_name = first + ' ' + middle + ' '+ last
	else:
		full_name = first + ' ' + last
	return full_name.title()
#This is a perfectly working function for every type of name 
