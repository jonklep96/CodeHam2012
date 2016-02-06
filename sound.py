import pygame
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

def play_sound(name):
    try:
        effect = pygame.mixer.Sound('assets/' + name + '.ogg')
        effect.play(0)
    except:
        print("Cannot play this. Check the file name.")

def play_music():
    pygame.mixer.music.load('assets/music.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)




