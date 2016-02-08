import pygame
import enemy
import player
import window


class Cell(pygame.Rect):

    def __init__(self, _x, _y, _width, _height, _loc):

        # Initialize the Rect
        self.x = _x
        self.y = _y
        self.width = _width
        self.height = _height

        # Used to evaluate where the player and bots move
        self.is_access = True
        self.on_border = True

        # Used to evaluate what is in the Cell
        self.item_list = []
        self.unit_list = []

        # Initializes the index of locations adjacent to the cell
        self.loc = _loc
        self.adj_loc = self.get_adjacent()

    def has_unit(self):

        count = self.unit_list.__sizeof__()

        if count > 0:
            return True
        else:
            return False

    def has_item(self):

        count = self.item_list.__sizeof__()

        if count > 0:
            return True
        else:
            return False

    def is_moveable(self, index, unit):

        if isinstance(unit, enemy.Enemy):
            if index == unit.loc - 1 or index == unit.loc + window.CELL_VER:
                if index == unit.loc + 1 or index == unit.loc - window.CELL_VER:
                    return True
        elif isinstance(unit, player.Player):
            if index == unit.loc - 1 or index == unit.loc + window.CELL_VER:
                if index == unit.loc + 1 or index == unit.loc - window.CELL_VER:
                    return True

        return False

    def get_adjacent(self):

        ret = [0, 0, 0, 0]

        if self.loc % window.CELL_VER == 0:
            ret[0] = -1
        else:
            ret[0] = self.loc - 1
        if ((window.CELL_HOR * window.CELL_VER) - window.CELL_VER) < self.loc < (window.CELL_HOR * window.CELL_VER):
            ret[1] = -1
        else:
            ret[1] = self.loc + window.CELL_VER
        if self.loc % window.CELL_VER == window.CELL_VER - 1:
            ret[2] = -1
        else:
            ret[2] = self.loc + 1
        if 0 <= self.loc < window.CELL_VER:
            ret[3] = -1
        else:
            ret[3] = self.loc - window.CELL_VER

        return ret

    def get_rect(self):

        return [self.x, self.y, self.width, self.height]
