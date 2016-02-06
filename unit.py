import os
import pygame
from pygame.locals import *

class Unit(pygame.sprite.Sprite):

    def __init__(self):

        def load_image(name, colorkey = None):
            fullname = os.path.join('assets', name)
            try:
                image = pygame.image.load(fullname)
            except:
                print('Image cannot be loaded:', fullname)
                raise SystemExit
            image = image.convert()
            if colorkey is not None:
                if colorkey is -1:
                    colorkey = image.get_at((0,0))
                image.set_colorkey(colorkey, RLEACCEL)
            return image, image.get_rect()



   # def draw_image(self, surface, rect):

