import random 

class Blob():

	def __init__(self,color, x_boundary, y_boundary, size_range = (4,6), movement_range = (-1,2)):
		#magic system 
		#one of the magic methods
		self.x_boundary = x_boundary
		self.y_boundary=y_boundary 
		self.x =random.randrange(0, self.x_boundary)
		self.y =random.randrange(0, self.y_boundary)
		self.size_range =size_range
		self.size = random.randrange(self.size_range[0],self.size_range[1])
		self.color = color
		self.movement_range = movement_range

		#Since Height and Width are not defined here, so we used some alias
		#And used it as x_boundary and y_boundary
		#Till now we are giving color only
		#as a parameter

	def move(self):
		self.move_x = random.randrange(self.movement_range[0],self.movement_range[1])
		self.move_y = random.randrange(self.movement_range[0],self.movement_range[1])		
		self.x += self.move_x
		self.y += self.move_y

		#This makes us the TRUE USER of the bob class sas compared to the blob
		#class enforcing us 

		
