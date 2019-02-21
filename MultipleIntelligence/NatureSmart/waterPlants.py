import pygame 

def start_game(level) : 
	pygame.init() 

	display_width = 800 
	display_height = 1000 


	screen = pygame.display.set_mode((display_width , display_height ))
	pygame.display.set_caption(" Water 'em")

	black = (0,0,0)
	white = (255,255,255)

	clock = pygame.time.Clock() 
	canImg = pygame.image.load('waterCan.png')
	gameOver = False 

	x = display_width*0.5
	y = display_height*0.9
	xChange = 0 
	canSpeed = 0 

	while not gameOver : 
		for event in pygame.event.get() : 
			if event.type == pygame.QUIT : 
				gameOver = True 

			if event.type == pygame.KEYDOWN : 
				if event.key == pygame.K_LEFT : 
					xChange = -5 
				elif event.key == pygame.K_RIGHT : 
					xChange = 5 
			if event.type == pygame.KEYUP : 
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT : 
					xChange = 0 

			x += xChange
			waterCan(canImg , screen , x , y )
			pygame.display.update()



def waterCan( canImg, screen, x,y) : 
	screen.blit(canImg , (x,y))
