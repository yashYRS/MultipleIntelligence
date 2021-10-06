import pygame 

def getWidthHeight() : 
	pygame.init()
	I = pygame.display.Info()
	width, height = I.current_w , I.current_h
	pygame.display.quit()
	return width - 300  , height - 120  #300,250