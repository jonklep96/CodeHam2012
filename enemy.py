import unit
import random
import window


class Enemy(unit.Unit):

    def __init__(self, _rect, img, _name):

        # Call back to parent class
        unit.Unit.__init__(self, _rect, img, _name)

        self.money = int(random.random() * 5 + 1)
        self.atk = 2

    def get_move_dir(self, byt_rect):

        if self.rect.x < byt_rect.x:
            return 1
        elif self.rect.y > byt_rect.y:
            return 0
        elif self.rect.x > byt_rect.x:
            return 3
        elif self.rect.y < byt_rect.y:
            return 2
        else:
            return 0

    # Is called when the bot is moved
    def move(self, _rect, _loc):

        self.rect = _rect
        self.loc = _loc
