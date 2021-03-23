from name_function import get_formatted_name


print("\nEnter q to quit anytime")
while True:
	first = input("\nEnter ur first name: ")
	if first == 'q':
		break

	last = input("\nEnter ur last name: ")
	if last == 'q':
		break


	format_name = get_formatted_name(first,last)
	print("\tNeatly formatted name is "+ format_name)


