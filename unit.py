import os
import pygame
from pygame.locals import *
import window

class Unit(pygame.sprite.Sprite):

    #Constructor
    def __init__(self, _rect, name):

        #Calling the parent constructor, pygame.sprite.Sprite
        pygame.sprite.Sprite.__init__(self)

        self.rect = _rect

        #Creating Byt at the 'spawn point' and adding him to bytbot group.
        self.image = pygame.image.load('assets/' + name + '.png')
