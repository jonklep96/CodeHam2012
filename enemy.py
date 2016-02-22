import unit
import random
import pygame
import window_locals


class Enemy(unit.Unit):

    def __init__(self, _rect, _img, _name, _loc):

        # Call back to parent class
        unit.Unit.__init__(self, _rect, _img, _name, _loc)

        self.money = int(random.random() * 5) + 1
        self.atk = 2

    # Make the AI choose the right direction
    def get_move_dir(self, _byt):

        _byt_x = _byt.loc // window_locals.CELL_VER
        _bot_x = self.loc // window_locals.CELL_VER

        _byt_y = _byt.loc % window_locals.CELL_VER
        _bot_y = self.loc % window_locals.CELL_VER

        print(str(self.loc) + ': (' + str(_bot_x) + ', ' + str(_bot_y) + ')')  # debug

        if _bot_y > _byt_y:
            return 0
        elif _bot_y < _byt_y:
            return 2
        else:
            if _bot_x < _byt_x:
                return 1
            elif _bot_x > _byt_x:
                return 3
