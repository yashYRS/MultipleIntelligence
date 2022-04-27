#!/usr/bin/env python
import os
import pygame
import sys
EXEC_DIR = os.path.dirname(__file__)


class Word(object):
    def __init__(self, word):
        if sys.platform == 'darwin':
            self.word_image = os.path.join('sounds', word)
        else:
            self.word_image = word
        self.word = word.split('/')[-1]

        self.image = pygame.mixer.Sound(self.word_image)
        # self.rect = self.image.get_rect()
        self.spelling_word = self.word.split('.')[0]
        self.letters = list(self.spelling_word)
        self.width = 100
        self.length = 100

    '''def draw(self, screen, x, y):
        screen.blit(self.image, [x, y])'''
