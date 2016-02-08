import pygame


class Cell(pygame.Rect):

    def __init__(self, _x, _y, _width, _height):

        # Initialize the Rect
        self.x = _x
        self.y = _y
        self.width = _width
        self.height = _height

        # Used to evaluate where the player and bots move
        self.is_access = True
        self.on_border = False

        # Used to evaluate what is in the Cell
        self.item_list = []
        self.unit_list = []

    def has_unit(self):

        count = 0
        for unit in self.unit_list:
            count += 1

        if count > 0:
            return True
        else:
            return False

    def has_item(self):

        count = 0
        for item in self.item_list:
            count += 1

        if count > 0:
            return True
        else:
            return False
