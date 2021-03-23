import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5000))
full_msg = ''
while True: #The port remains open indefinately
	msg = s.recv(8)
	if len(msg) <= 0:
		break
	full_msg += msg.decode("utf-8")	 
	print(msg.decode("utf-8"))
	
print(full_msg)
#This is the complete msg being sent 
#adding onto full_msg list
#32 This is minimum for Welcome to the server 
#1024 chunk of data 
#The length of msg gets to zero only because the connection closes 	