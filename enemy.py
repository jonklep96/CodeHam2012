import unit
import random
import window


class Enemy(unit.Unit):

    def __init__(self, _rect, img, _name):

        # Call back to parent class
        unit.Unit.__init__(self, _rect, img, _name)

        self.money = int(random.random() * 5 + 1)
        self.atk = 2
