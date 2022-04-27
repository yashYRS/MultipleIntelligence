#!/usr/bin/env python
import os
import pygame
import sys
EXEC_DIR = os.path.dirname(__file__)


class Word(object):
    def __init__(self, word, level):
        if sys.platform == 'darwin':
            if level == 1:
                self.word_image = os.path.join('word_files', word)
            elif level == 2:
                self.word_image = os.path.join('animals', word)
            elif level == 3:
                self.word_image = os.path.join('species', word)
        else:
            if level == 1:
                self.word_image = os.path.join(EXEC_DIR, 'word_files', word)
            elif level == 2:
                self.word_image = os.path.join(EXEC_DIR, 'animals', word)
            elif level == 3:
                self.word_image = os.path.join(EXEC_DIR, 'species', word)
        self.word = word
        self.image = pygame.image.load(self.word_image)
        self.rect = self.image.get_rect()
        self.spelling_word = self.word.split('.')[0]
        self.letters = list(self.spelling_word)
        self.width = self.image.get_width()
        self.length = len(self.letters)

    def draw(self, screen, x, y):
        screen.blit(self.image, [x, y])
