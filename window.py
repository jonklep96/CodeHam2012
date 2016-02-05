import os
import sys
import pygame
from pygame.locals import *


class Window:

    def __init__(self):

        pygame.init()
        self.WIDTH = 720
        self.HEIGHT = 600
        self.display_size = [self.WIDTH, self.HEIGHT]
        self.cell_width = int(self.WIDTH / 12)
        self.cell_height = int(self.HEIGHT / 12)
        self.display_label = 'Code Ham Game'
        self.display = pygame.display.set_mode(self.display_size)
        pygame.display.set_caption(self.display_label)

        # List to store cell coordinates
        self.grid = []
        self.last_loc = [0, 0]
        # Constant of the cell border width
        self.GRID_CELL_WIDTH = 2
        self.draw_grid()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    self.check_click(pos)
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()

    # draws the grid according to the screen size
    def draw_grid(self):

        rect_color = (255, 255, 255)
        for x in range(0, self.WIDTH, self.cell_width):
            for y in range(0, self.HEIGHT, self.cell_height):
                rect = pygame.Rect(x, y, self.cell_width, self.cell_height)
                self.grid.append([[x, x + self.cell_width], [y, y + self.cell_height]])
                pygame.draw.rect(self.display, rect_color, rect, self.GRID_CELL_WIDTH)

    # checks for which grid you clicked in
    def check_click(self, pos):

        # Values to store clicking and drawing
        padding_adjustment = self.GRID_CELL_WIDTH + 3
        new_color = (255, 30, 180)
        rect_color = (255, 255, 255)

        coordinate = 0
        for item in self.grid:
            coordinate += 1
            if pos[0] > item[0][0] + padding_adjustment:
                if pos[0] < item[0][1] - padding_adjustment:
                    if pos[1] > item[1][0] + padding_adjustment:
                        if pos[1] < item[1][1] - padding_adjustment:
                            print(coordinate) #print place debug
                            new_rect = pygame.Rect(item[0][0], item[1][0], self.cell_width, self.cell_height)
                            cell_width = self.cell_width
                            cell_height = self.cell_height
                            last_rect = pygame.Rect(self.last_loc[0], self.last_loc[1], cell_width, cell_height)
                            pygame.draw.rect(self.display, new_color, new_rect, self.GRID_CELL_WIDTH)
                            pygame.draw.rect(self.display, rect_color, last_rect, self.GRID_CELL_WIDTH)
                            self.last_loc = [item[0][0], item[1][0]]
