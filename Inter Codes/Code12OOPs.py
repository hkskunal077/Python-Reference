from module_blob import * 
import pygame
import random

WIDTH = 1920
HEIGHT = 1080
#These dimensions height and  width are made constant
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0,255, 0)
STARTING_BLUE_BLOBS = 100
STARTING_GREEN_BLOBS = 20
STARTING_RED_BLOBS = 100
game_display = pygame.display.set_mode((WIDTH,HEIGHT))
#most of the modules are pre-defined 
#game_display is just a variable
pygame.display.set_caption("BLOB WORLD")
clock =pygame.time.Clock()


def draw_environment(blobs_list):
	game_display.fill(WHITE)
	for blob_dict in blobs_list:
		for blob_id in blob_dict:
			blob = blob_dict[blob_id]
			#blob-id is the KEY and the blob_dict[blob_id] is the VALUE 
			pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
			blob.move()
			if blob.x < 0:	blob.x = -2
			elif blob.x > blob.x_boundary:	blob.x = -3

			if blob.y < 0:	blob.y = -2 
			elif blob.y > blob.y_boundary:	blob.x = -3
			#This is one of the harcoded things of the class
			#To make the class more OOPS side, we needed this 
			
	
	pygame.display.update()
	

	#this is when we want to update user space 
	#using update function


def main(): 
	blue_blobs = dict(enumerate([Blob(BLUE,WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
	#To give it a number or ID
	red_blobs = dict(enumerate([Blob(RED,WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))
	green_blobs = dict(enumerate([Blob(GREEN,WIDTH,HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))

	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
		draw_environment([blue_blobs,red_blobs,green_blobs])
		#draw_environment(red_blobs)
		clock.tick(60)
		
if __name__ == '__main__':
	main()



#One of the general idea here is that,we start from ground zero 
# ofc but as the things are made we do not try to screw the ones 
#already made before 
