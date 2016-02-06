import sys
import pygame
import color
import window

pygame.init()

width = 540
height = 540
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
s_background = pygame.Surface((width, height))
pygame.draw.rect(s_background, color.GRAY, (0, 0, width, height))
s_background = s_background.convert(screen)
screen.blit(s_background, (0, 0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            s_background = window.update_window(event, s_background, screen)
            screen.blit(s_background, (0, 0))
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
