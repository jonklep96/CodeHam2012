import pygame


class Item(pygame.sprite.Sprite):

     def __init__(self, _rect, _img, _name):
        self.name = _name

        # Calling the parent constructor, pygame.sprite.Sprite
        pygame.sprite.Sprite.__init__(self)

        # This is the rectangle where the unit resides
        x = _rect.x
        y = _rect.y
        width = 32
        height = 32
        self.rect = pygame.Rect(x, y, width, height)

        # Loading the item sprite
        self.image = pygame.image.load('assets/' + _img + '.png')
