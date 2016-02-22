import pygame


class Item(pygame.sprite.Sprite):

    def __init__(self, _rect, _img, _name, _loc):
        self.name = _name

        # Calling the parent constructor, pygame.sprite.Sprite
        pygame.sprite.Sprite.__init__(self)

        # This is the rectangle where the unit resides
        x = _rect.x
        y = _rect.y
        width = 32
        height = 32
        self.rect = pygame.Rect(x, y, width, height)

        self.loc = _loc

        # Loading the item sprite
        self.image = pygame.image.load('assets/' + _img + '.png')

    def set_rect(self, _cell):

        self.rect.x = _cell.x + int((_cell.width - self.rect.width) / 2)
        self.rect.y = _cell.y + int((_cell.height - self.rect.height) / 2)

    def move(self, _cell):

        self.set_rect(_cell)
        self.loc = _cell.loc
