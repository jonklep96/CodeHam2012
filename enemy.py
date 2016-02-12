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
    def get_move_dir(self, byt):

        byt_y = (byt.loc - (byt.loc % window_locals.CELL_HOR)) / window_locals.CELL_HOR
        bot_y = (self.loc - (self.loc % window_locals.CELL_VER)) / window_locals.CELL_VER

        if bot_y > byt_y:
            print('Bot is Better')
        else:
            print('Byt is Better')

        if self.rect.x < byt.rect.x:
            return 1
        elif self.rect.y > byt.rect.y:
            return 0
        elif self.rect.x > byt.rect.x:
            return 3
        elif self.rect.y < byt.rect.y:
            return 2
