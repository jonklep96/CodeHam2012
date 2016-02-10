import sys
import pygame
import color
import sound
import main_menu
import enemy
import random
import cell
import player
import item
import window_locals

# draws the grid according to the screen size
# during the first_run, draw_grid will add the
# rects to a list
def draw_grid(first_run):

    grid_index = 0
    for x in range(0, WIDTH, cell_width):
        for y in range(0, HEIGHT, cell_height):
            rect = cell.Cell(x, y, cell_width, cell_height, grid_index)
            if first_run:
                grid.append(rect)
                init_outer_border(grid_index)
            if grid[grid_index].on_border:
                pygame.draw.rect(s_grid, color.OFF_WHITE, rect, GRID_CELL_WIDTH)
            else:
                pygame.draw.rect(s_grid, color.WHITE, rect, GRID_CELL_WIDTH)
            grid_index += 1


# checks for which grid you clicked in
def check_click(_pos, _step):

    grid_index = 0
    for _item in grid:
        if rect_contain(_item, _pos):
            _cell = grid[grid_index]
            if _cell.is_access and not _cell.on_border:
                for i in _cell.get_adjacent():
                    for j in grid[last_loc].get_adjacent():
                        if i == j:
                            print(grid_index)  # debug cell index
                            sel_cell = grid[grid_index]
                            adj_cells = cell.get_adjacent()
                            byt.set_rect(sel_cell)

                            # Update the rect of the AI bots
                            for bot in bot_list:
                                move_bot(bot, bot.get_move_dir(byt))
                                print(bot.loc)  # debug where the bot is

                            draw_grid(False)

                            # Remove the previous selected cells
                            draw_layers()
                            draw_group(byt_list)
                            draw_group(bot_list)

                            # Width of cell selection
                            sel_width = GRID_CELL_WIDTH + 2

                            # Draw the selectable locations
                            if adj_cells[0] != -1 and not grid[adj_cells[0]].on_border:
                                pygame.draw.rect(screen, color.BLUE, grid[adj_cells[0]].get_rect(), sel_width)
                            if adj_cells[1] != -1 and not grid[adj_cells[1]].on_border:
                                pygame.draw.rect(screen, color.BLUE, grid[adj_cells[1]].get_rect(), sel_width)
                            if adj_cells[2] != -1 and not grid[adj_cells[2]].on_border:
                                pygame.draw.rect(screen, color.BLUE, grid[adj_cells[2]].get_rect(), sel_width)
                            if adj_cells[3] != -1 and not grid[adj_cells[3]].on_border:
                                pygame.draw.rect(screen, color.BLUE, grid[adj_cells[3]].get_rect(), sel_width)
                            pygame.draw.rect(screen, color.YELLOW, sel_cell.get_rect(), sel_width + 1)
                            last_loc = grid_index
                            _step += 1
        grid_index += 1
    return _step


# Check to see if the position was inside the specified cell
def rect_contain(rect, pos):

    # Values to store clicking and drawing
    padding_adjustment = GRID_CELL_WIDTH + 1

    if pos[0] > rect.x + padding_adjustment:
        if pos[0] < rect.x + rect.width - padding_adjustment:
            if pos[1] > rect.y + padding_adjustment:
                if pos[1] < rect.y + rect.height - padding_adjustment:
                    return True
    else:
        return False


def init_outer_border(index):

    if index >= (OUTER_CELLS * CELL_VER):
        if index < ((CELL_HOR * CELL_VER) - (OUTER_CELLS * CELL_VER)):
            if OUTER_CELLS <= (index % CELL_VER) < (CELL_VER - OUTER_CELLS):
                grid[index].on_border = False


def draw_layers():

    screen.blit(s_background, (0, 0))
    screen.blit(s_grid, (s_grid_x, s_grid_y))
    sound.play_sound('bytmove')
    pygame.display.flip()


# Draw the group of sprites
def draw_group(group):
    t_group = group.copy()
    for sprite in t_group.sprites():
        t_x = sprite.rect.x + int((cell_width - sprite.rect.width) / 2)
        t_y = sprite.rect.y + int((cell_height - sprite.rect.height) / 2)
        t_rect = pygame.Rect(t_x, t_y, sprite.rect.width, sprite.rect.height)
        sprite.rect = t_rect
        t_group.add(sprite)
    t_group.draw(screen)


# Check for direction that the bot should move
def move_bot(_bot, _dir):

    if _dir == 0:
        _bot.move(grid[_bot.loc - 1], -bot.loc - 1)
    elif _dir == 1:
        _bot.move(grid[_bot.loc + CELL_VER], _bot.loc + CELL_VER)
    elif _dir == 2:
        _bot.move(grid[_bot.loc + 1], _bot.loc + 1)
    elif _dir == 3:
        _bot.move(grid[_bot.loc - CELL_VER], _bot.loc - CELL_VER)


# Spawn the bots on the sides of the screen
def spawn_rand():

    ret = int(random.random() * 4)
    if ret == 0:
        while True:
            ret = int(random.random() * (CELL_HOR * CELL_VER))
            if ret % CELL_VER == 0:
                break
    elif ret == 1:
        ret = ((CELL_HOR * CELL_VER) - 1) - int(random.random() * CELL_VER)
    elif ret == 2:
        while True:
            ret = int(random.random() * (CELL_HOR * CELL_VER))
            if ret % CELL_VER == CELL_VER - 1:
                break
    elif ret == 3:
        ret = int(random.random() * CELL_VER)

    return ret

# Initializes pygame and the mixer to prevent sound lag.
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

CELL_HOR = window_locals.CELL_HOR
CELL_VER = window_locals.CELL_VER
OUTER_CELLS = window_locals.OUTER_CELLS

WIDTH = window_locals.WIDTH
HEIGHT = window_locals.HEIGHT

cell_width = int(WIDTH / CELL_HOR)
cell_height = int(HEIGHT / CELL_VER)

# Create a window with the Surface screen
screen_label = 'BytBot'
pygame.display.set_caption(screen_label)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a main menu
main_menu.start_menu(screen)

# Create a background Surface
s_background = pygame.Surface((WIDTH, HEIGHT))
pygame.draw.rect(s_background, color.GRAY, (0, 0, WIDTH, HEIGHT))
s_background = s_background.convert(screen)
screen.blit(s_background, (0, 0))

# Create a grid Surface
s_grid = pygame.Surface((WIDTH, HEIGHT))
s_grid = s_grid.convert(screen)
s_grid.set_alpha(180)
s_grid_x = 0
s_grid_y = 0

# List to store cell coordinates
grid = []

# Constant of the cell border width
GRID_CELL_WIDTH = 2
draw_grid(True)

# Stores the index of the starting location and the previous location
last_loc = CELL_VER * 2 + OUTER_CELLS

# Stores the amount of times the player has made an action
step = 0

# Draw the layers to the screen
draw_layers()

# Start Music
sound.play_music()

# Creating the groups for sprites. Items, BytBot - contains all characters, Bot - enemies
item_list = pygame.sprite.Group()
bytbot_list = pygame.sprite.Group()
bot_list = pygame.sprite.Group()
byt_list = pygame.sprite.Group()

# Draw Characters - Initial
byt = player.Player(grid[32], 'byt', 'Byt', 32)
byt_list.add(byt)
for i in range(1, 5):
    rand_loc = spawn_rand()
    bot = enemy.Enemy(grid[rand_loc], 'bot', 'Bot', rand_loc)
    bot_list.add(bot)

draw_group(bot_list)
draw_group(byt_list)

# Draw items - initial
spark = item.Item(grid[55], 'spark', 'Spark')  # debug
heart = item.Item(grid[70], 'heart', 'Heart')  # debug
item_list.add(spark, heart)  # debug
draw_group(item_list)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)  # debug mouse position
            step = check_click(pos, step)
        elif event.type == pygame.QUIT:
            sys.exit()
        pygame.display.flip()
