import unit
import pygame
import os

class Player(unit.Unit):

    def __init__(self, _rect, _name, _img):

        unit.Unit.__init__(self, _rect, _name, _img)
