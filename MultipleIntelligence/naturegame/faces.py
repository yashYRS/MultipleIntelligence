#!/usr/bin/env python

import pygame
from pygame.locals import *
import os
import sys
from random import randint
EXEC_DIR = os.path.dirname(__file__)


class Face(pygame.sprite.Sprite):
    def __init__(self, type):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        if sys.platform == 'darwin':
            face_path = 'faces'
        else:
            face_path = os.path.join(EXEC_DIR, 'faces')
        if self.type == 'happy':
            self.image = pygame.image.load(os.path.join(face_path,'happy.png'))
        elif self.type == 'sad':
            self.image = pygame.image.load(os.path.join(face_path, 'sad.png'))
        self.rect = self.image.get_rect()
        self.rect.topleft = [200, 300]
        self.lifespan = 15 
        
    def update(self):
        self.lifespan -= 1
        if self.type == 'happy':
            x, y = (randint(1,500), randint(1,500))
        else:
            x, y = [200, 300]
        self.rect.topleft = [x, y]
    
    def reset(self):
        self.lifespan = 25 
