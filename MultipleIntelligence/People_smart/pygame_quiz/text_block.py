import pygame
from game_object import GameObject
from colors import Color
import shapes as Helper_shapes 

class TextBlock(GameObject):    
	def __init__(self, x, y, w, h, text,isquestion = False):
		super().__init__(x, y, w, h)
		self.text = text
		self.x_padding = x + 23
		self.y_padding = y + 23
		if(isquestion):
			self.font = pygame.font.SysFont('Arial', 22)
			self.DEFAULT_BACK_COLOR = Color.BLACK
			self.TEXT_COLOR = (0,255,0)
		else:
			self.font = pygame.font.SysFont('Arial', 18)
			self.DEFAULT_BACK_COLOR = Color.GREEN
			self.TEXT_COLOR = (0,0,0)
		self.back_color = self.DEFAULT_BACK_COLOR
		self.text_color = self.TEXT_COLOR

	def draw(self, surface):
		Helper_shapes.rounded_rect(surface,self.bounds,self.back_color,0.5)
		#pygame.draw.rect(surface, self.back_color, self.bounds)
		surface.blit(self.font.render(self.text, False, self.text_color),
					(self.x_padding, self.y_padding))
		
	def update(self):
		pass



    
    


