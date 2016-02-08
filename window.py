import sys
import pygame
import color
import sound
import unit
import main_menu
import enemy
import random

# Initializes pygame and the mixer to prevent sound lag.
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

CELL_HOR = 15
CELL_VER = 15


class Window:

    def __init__(self):

        self.width = 600
        self.height = 600
        self.cell_width = int(self.width / CELL_HOR)
        self.cell_height = int(self.height / CELL_VER)

        # Create a window with the Surface screen
        self.screen_label = 'BytBot'
        pygame.display.set_caption(self.screen_label)
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Create a main menu
        main_menu.start_menu(self.screen)

        # Create a background Surface
        self.s_background = pygame.Surface((self.width, self.height))
        pygame.draw.rect(self.s_background, color.GRAY, (0, 0, self.width, self.height))
        self.s_background = self.s_background.convert(self.screen)
        self.screen.blit(self.s_background, (0, 0))

        # Create a grid Surface
        self.s_grid = pygame.Surface((self.width, self.height))
        self.s_grid = self.s_grid.convert(self.screen)
        self.s_grid.set_alpha(180)
        self.grid_x = 0
        self.grid_y = 0

        # List to store cell coordinates
        self.grid = []
        self.sel_cells = [0]*4

        # Constant of the cell border width
        self.OUTER_CELLS = 2
        self.GRID_CELL_WIDTH = 2
        self.draw_grid(True)

        # Stores the index of the starting location and the previous location
        self.last_loc = CELL_VER * 2 + self.OUTER_CELLS

        # Stores the amount of times the player has made an action
        self.step = 0

        # Draw the layers to the screen
        self.draw_layers()

        # Start Music
        sound.play_music()

        # Creating the groups for sprites. Items, BytBot - contains all characters, Bot - enemies
        self.item_list = pygame.sprite.Group()
        self.bytbot_list = pygame.sprite.Group()
        self.bot_list = pygame.sprite.Group()
        self.byt_list = pygame.sprite.Group()

        # Draw Characters - Initial
        self.byt = unit.Unit(self.grid[32], 'byt', 'Byt')
        self.byt_list.add(self.byt)
        for i in range(1, 4):
            bot = enemy.Enemy(self.grid[spawn_rand()], 'bot', 'Bot')
            self.bot_list.add(bot)
        self.draw_group(self.bot_list)
        self.draw_group(self.byt_list)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(pos)  # debug mouse position
                    self.check_click(pos)
                elif event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()

    # draws the grid according to the screen size
    # during the first_run, draw_grid will add the
    # rects to a list
    def draw_grid(self, first_run):

        grid_index = 0
        for x in range(0, self.width, self.cell_width):
            for y in range(0, self.height, self.cell_height):
                rect = pygame.Rect(x, y, self.cell_width, self.cell_height)
                if first_run:
                    self.grid.append(rect)
                if self.is_outer_border(grid_index):
                    pygame.draw.rect(self.s_grid, color.OFF_WHITE, rect, self.GRID_CELL_WIDTH)
                else:
                    pygame.draw.rect(self.s_grid, color.WHITE, rect, self.GRID_CELL_WIDTH)
                grid_index += 1

    # checks for which grid you clicked in
    def check_click(self, pos):

        grid_index = 0
        for item in self.grid:
            if self.rect_contain(item, pos):
                if self.is_movable(grid_index, self.last_loc):
                    print(grid_index)  # debug cell index
                    sel_cell = pygame.Rect(item.x, item.y, self.cell_width, self.cell_height)
                    self.byt.rect = pygame.Rect(sel_cell.x, sel_cell.y, self.byt.rect.width, self.byt.rect.height)

                    # Update the rect of the AI bots
                    for bot in self.bot_list:
                        self.move_bot(bot, bot.get_move_dir(self.byt.rect))
                        print(bot.loc)  # debug where the bot is

                    self.draw_grid(False)

                    # Selectable grid choices
                    self.sel_cells[0] = self.grid[grid_index - 1]
                    self.sel_cells[1] = self.grid[grid_index + CELL_VER]
                    self.sel_cells[2] = self.grid[grid_index + 1]
                    self.sel_cells[3] = self.grid[grid_index - CELL_VER]

                    # Remove the previous selected cells
                    self.draw_layers()
                    self.draw_group(self.byt_list)
                    self.draw_group(self.bot_list)

                    # Width of cell selection
                    sel_width = self.GRID_CELL_WIDTH + 2

                    # Draw the selectable locations
                    if self.is_movable(grid_index - 1, grid_index):
                        pygame.draw.rect(self.screen, color.BLUE, self.sel_cells[0], sel_width)
                    if self.is_movable(grid_index + CELL_VER, grid_index):
                        pygame.draw.rect(self.screen, color.BLUE, self.sel_cells[1], sel_width)
                    if self.is_movable(grid_index + 1, grid_index):
                        pygame.draw.rect(self.screen, color.BLUE, self.sel_cells[2], sel_width)
                    if self.is_movable(grid_index - CELL_VER, grid_index):
                        pygame.draw.rect(self.screen, color.BLUE, self.sel_cells[3], sel_width)
                    pygame.draw.rect(self.screen, color.YELLOW, sel_cell, sel_width + 1)
                    self.last_loc = grid_index
                    self.step += 1
            grid_index += 1

    # Check to see if the position was inside the specified cell
    def rect_contain(self, rect, pos):

        # Values to store clicking and drawing
        padding_adjustment = self.GRID_CELL_WIDTH + 1

        if pos[0] > rect.x + padding_adjustment:
            if pos[0] < rect.x + rect.width - padding_adjustment:
                if pos[1] > rect.y + padding_adjustment:
                    if pos[1] < rect.y + rect.height - padding_adjustment:
                        return True
        else:
            return False

    def is_outer_border(self, index):

        outer_cells = self.OUTER_CELLS
        cell_hor = CELL_HOR
        cell_ver = CELL_VER

        if index >= (outer_cells * cell_ver):
            if index < ((cell_hor * cell_ver) - (outer_cells * cell_ver)):
                if outer_cells <= (index % cell_ver) < (cell_ver - outer_cells):
                    return False

        return True

    def draw_layers(self):

        self.screen.blit(self.s_background, (0, 0))
        self.screen.blit(self.s_grid, (self.grid_x, self.grid_y))
        pygame.display.flip()
        sound.play_sound('bytmove')

    def is_movable(self, sel_index, cell_check):

        cell_ver = CELL_VER

        if not self.is_outer_border(sel_index):
            if sel_index == (cell_check - 1) or sel_index == (cell_check + cell_ver):
                return True
            if sel_index == (cell_check + 1) or sel_index == (cell_check - cell_ver):
                return True

        return False

    # Draw the group of sprites
    def draw_group(self, group):
        t_group = group.copy()
        for sprite in t_group.sprites():
            t_x = sprite.rect.x + int((self.cell_width - sprite.rect.width) / 2)
            t_y = sprite.rect.y + int((self.cell_height - sprite.rect.height) / 2)
            t_rect = pygame.Rect(t_x, t_y, sprite.rect.width, sprite.rect.height)
            sprite.rect = t_rect
            t_group.add(sprite)
        t_group.draw(self.screen)

    # Check for direction that the bot should move
    def move_bot(self, bot, _dir):

        if _dir == 0:
            bot.move(self.grid[bot.loc - 1], bot.loc - 1)
        elif _dir == 1:
            bot.move(self.grid[bot.loc + CELL_VER], bot.loc + CELL_VER)
        elif _dir == 2:
            bot.move(self.grid[bot.loc + 1], bot.loc + 1)
        elif _dir == 3:
            bot.move(self.grid[bot.loc - CELL_VER], bot.loc - CELL_VER)


# Spawn the bots on the sides of the screen
def spawn_rand():

    ret = int(random.random() * 4)

    if ret == 0:
        while True:
            ret = int(random.random() * (CELL_HOR * CELL_VER))
            if ret % CELL_VER == 0:
                break
    elif ret == 1:
        ret = (CELL_HOR * CELL_VER) - int(random.random() * CELL_VER)
    elif ret == 2:
        while True:
            ret = int(random.random() * (CELL_HOR * CELL_VER))
            if ret % (CELL_VER - 1) == 0:
                break
    elif ret == 3:
        ret = int(random.random() * CELL_VER)

    return ret
