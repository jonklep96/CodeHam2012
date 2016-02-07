#
import os
import pygame
from pygame.locals import *
import window

class Unit(pygame.sprite.Sprite):

    #Constructor
    def __init__(self, _rect, img, _name):
        self.name = _name

        #Calling the parent constructor, pygame.sprite.Sprite
        pygame.sprite.Sprite.__init__(self)

        #This is the rectangle where the unit resides
        x = _rect.x
        y = _rect.y
        width = 32
        height = 32
        self.rect = pygame.Rect(x, y, width, height)

        #Loading the sprite
        self.image = pygame.image.load('assets/' + img + '.png')

        #Instance Variables for Byts and Bots:
        self.health = 10
        self.money = 0
        self.atk = 1
        self.speed = 1
        