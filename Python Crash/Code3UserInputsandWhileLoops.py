#User Inputs and While Loops
#Code being interactive

#input() function pauses ur programme and waits for user to input some data
#then it stores it in a variable, which can be convinienty worked upon


# message = input("Tell me something, ill say it out loud\n")
# print(message)


#the imp msg that we are showing to user before input
# is called prompt


# prompt = "If u can tell use ur name we can do personalised experience:\n "
# prompt += "What is ur first name??: "

# fname = input(prompt)
# print("\nHello "+ fname)


#user always inputs string, convert it into, whatever data type u want

#while LOOPS
#they run for a while, as long as a specific condition is met

# current_number = 1
# while current_number<=5:
# 	print("current_number is "+ str(current_number))
# 	current_number+=1


prompt = "Tell me something, and i will repeat:"
prompt+="\nEnter 'quit' to quit the programme: "

# message= ""
# #we always need a condition for an initial pass
# while message!='quit': #This was only for the first pass as a tester, then it is just a checker 
# 	message= input(prompt)
# 	if message!=quit:
# 		print(message+"\n")


#we use flags to jump past

# stat = True
# while stat:
# 	message=input(prompt)
# 	if message=='quit':
# 		stat=False
# 	else:
# 		print(message+ "\n")	


# A loop with True as pass statement will run forever 

talk = "Where you have been??"
talk+= "\nEnter 'quit' to quit the code:  "

# while True:
# 	city = input(talk)

# 	if city=='quit':
# 		break

# 	else:
# 		print(city + " is a nice place")	

#if u want to use continue use increment first, otw code will jump 
# cnumber = 0
# while cnumber<10:
# 	cnumber+=1
# 	if cnumber%2 == 0:
# 		continue
# 	else:
# 		print(cnumber)	





#using a while loop with lists and dictionaries
#while loops on lists and Dries helps in modification and better management 


# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []

# while unconfirmed_users:
# 	current_user = unconfirmed_users.pop()

# 	print("verifying User: "+ current_user.upper())
# 	confirmed_users.append(current_user.title())


# print("\nThe following users are confirmed:")
# for confirmed_user in confirmed_users:
# 	print(confirmed_user)


# # to remove multiple instances of a value in a list
# print("\n")
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
# 	pets.remove('cat')#removes the first instance of intermediate list
# print(pets)
	





#Filling a dictionary with user input
responses = {}
active = True

while active:
	name = input ("\nWhat is ur name??? ")
	response = input ("Which mountain u'd like to climb one day?? ")

	responses[name]=response # we have actually used two assignments through one
	#its basically KEY-VALUE PAIR in one instance

	repeat= input("\n Another response?? (y/n)")
	if repeat.lower() == 'n':
		active=False



for name, response in responses.items():
	print(name + " wants to go to "+ responses[name])






























