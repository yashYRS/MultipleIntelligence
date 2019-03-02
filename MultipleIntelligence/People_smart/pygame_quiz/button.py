import pygame
from text_block import TextBlock
from colors import Color


class Button(TextBlock):

    def __init__(self, x, y, w, h, text, onclick_func):
        super().__init__(x, y, w, h, text, isquestion = False)
        self.state = 'normal'
        self.onclick_func = onclick_func
        self.HOVERED_BACK_COLOR = Color.BLUE
        self.PRESSED_BACK_COLOR = Color.WHITE

    def update(self):
        if self.state == 'normal':
            self.back_color = self.DEFAULT_BACK_COLOR
        elif self.state == 'hover':
            self.back_color = self.HOVERED_BACK_COLOR
        elif self.state == 'pressed':
            self.back_color = self.PRESSED_BACK_COLOR

    def handleMouseEvent(self, type_of_event, pos):
        if type_of_event == pygame.MOUSEMOTION:
            self.handleMouseMove(pos)
        elif type_of_event == pygame.MOUSEBUTTONDOWN:
            self.handleMouseDown(pos)
        elif type_of_event == pygame.MOUSEBUTTONUP:
            self.handleMouseUp(pos)

    def handleMouseMove(self, pos):
        if self.bounds.collidepoint(pos):
            if self.state != 'pressed':
                self.state = 'hover'
        else:
            self.state = 'normal'

    def handleMouseDown(self, pos):
        if self.bounds.collidepoint(pos):
            self.state = 'pressed'

    def handleMouseUp(self, pos):
            if self.state == 'pressed':
                self.onclick_func(self)
                self.state = 'hover'
