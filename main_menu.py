import pygame
import color

def start_menu(screen):

    menuimg = pygame.image.load('assets/titlescreen.png')
    s_background = pygame.Surface((screen.get_width(), screen.get_height()))
    x = 0
    y = 0
    pygame.draw.rect(s_background, color.BLUE, (x, y, screen.get_width(), screen.get_height()))
    s_background = menuimg.convert(screen)
    screen.blit(s_background, (x, y))
    pygame.display.flip()

    done = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] >= x or pos[1] >= y:
                    done = True
                    break
        if done:
            break
