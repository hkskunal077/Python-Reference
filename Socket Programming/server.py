import socket 
# we define an instance of socket 
# or an object named s

# We are gonna use Headers to tell the details about the
# data to be sent, client keeps receiving data until full			  
#Fixed-Length Headers
# msg = "Welcome To The Server!"



s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),5000))
s.listen(5)
#AF_NET is Ipv4
#SOCK_STREAM is the way communication is 
#going to take place 
#TCP for SOCK_STREAM
#This will be streaming socket 

#means object operates from port 1234 of the host(server) binded
#Sockets are generally the end points that get data 

#Now we have a server socket listening upto 5 connections
#we can enter the mainloop
#ACK after connection is established 
	#and the ACK message is sent also 

while True:
	clientsocket, address = s.accept()
	print(f"connection from {address} has been established!")
	clientsocket.send(bytes("Server Requests...., for AF_INET connection", "utf-8"))
	clientsocket.close()

