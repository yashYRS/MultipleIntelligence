import pygame
from game_object import GameObject
from colors import Color


class TextBlock(GameObject):
  
    def __init__(self, x, y, w, h, text ):
        super().__init__(x, y, w, h)
        self.text = text
        self.x_padding = x + 23
        self.y_padding = y + 23
        self.font = pygame.font.SysFont('Arial', 22)
        
        self.DEFAULT_BACK_COLOR = Color.WHITE
        self.back_color = self.DEFAULT_BACK_COLOR

    def draw(self, surface):
        pygame.draw.rect(surface, self.back_color, self.bounds)
        surface.blit(self.font.render(self.text, False, (0, 0, 0)),
                     (self.x_padding, self.y_padding))

    def update(self):
        pass
