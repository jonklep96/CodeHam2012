from unit import Unit
import pygame
import os

class Player(Unit):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = self.load_image('assets/byt.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
