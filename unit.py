import os
import pygame
from pygame.locals import *
import window

class Unit(pygame.sprite.Sprite):

    #Constructor
    def __init__(self):

        #Calling the parent constructor, pygame.sprite.Sprite
        pygame.sprite.Sprite.__init__(self)

        #Creating the groups for sprites. Items, BytBot - contains all characters, Bot - enemies
        item_list = pygame.sprite.Group()
        bytbot_list = pygame.sprite.Group()
        bot_list = pygame.sprite.Group()
        byt_list = pygame.sprite.Group()

        #Creating Byt at the 'spawn point' and adding him to bytbot group.
        byt = pygame.image.load('assets/byt.png')
        byt.rect.x = 20
        byt.rect.y = 20
        byt_list.add(byt)
        self.bytbot_list.add(byt)

        #Creating Byt at the 'spawn point' and adding him to bytbot group.
        bot = pygame.image.load('assets/bot.png')
        bot.rect.x = 100
        bot.rect.y = 100
        self.bytbot_list.add(bot)
        bot_list.add(bot)


        bytbot_list.draw(window.display)

        # def load_image(name, colorkey = None):
        #     fullname = os.path.join('assets', name)
        #     try:
        #         image = pygame.image.load(fullname)
        #     except:
        #         print('Image cannot be loaded:', fullname)
        #         raise SystemExit
        #     image = image.convert()
        #     if colorkey is not None:
        #         if colorkey is -1:
        #             colorkey = image.get_at((0,0))
        #         image.set_colorkey(colorkey, RLEACCEL)
        #     return image, image.get_rect()



#A method that plays a sound object into the game.
def play_music():
    pygame.mixer.music.load('assets/music.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.get_pos()


   # def draw_image(self, surface, rect):
