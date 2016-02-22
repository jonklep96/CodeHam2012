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
                pygame.draw.rect(s_grid, color.OFF_WHITE, rect, CELL_LINE_WIDTH)
            else:
                pygame.draw.rect(s_grid, color.WHITE, rect, CELL_LINE_WIDTH)
            grid_index += 1


# checks for which grid you clicked in
def check_click(_pos, _step, _last_loc):

    grid_index = 0
    for _cell in grid:
        if rect_contain(_cell, _pos):
            if _cell.is_access and not _cell.on_border:
                for _j in grid[_last_loc].get_adjacent():
                    if grid_index == _j:
                        print(grid_index)  # debug cell index
                        _sel_cell = grid[grid_index]

                        # Update the rect of the AI bots
                        for _bot in bot_list:
                            move_bot(_bot, _bot.get_move_dir(byt))

                        # Move the player
                        byt.move(_sel_cell)

                        # Draw the selectable locations
                        draw_adjacents(grid, _sel_cell)

                        sound.play_sound('bytmove')
                        _last_loc = grid_index
                        _step += 1
        grid_index += 1
    return [_step, _last_loc]


# Check to see if the position was inside the specified cell
def rect_contain(_rect, _pos):

    # Values to store clicking and drawing
    padding_adjustment = CELL_LINE_WIDTH + 1

    if _pos[0] > _rect.x + padding_adjustment:
        if _pos[0] < _rect.x + _rect.width - padding_adjustment:
            if _pos[1] > _rect.y + padding_adjustment:
                if _pos[1] < _rect.y + _rect.height - padding_adjustment:
                    return True

    return False


def init_outer_border(index):

    if index >= (OUTER_CELLS * CELL_VER):
        if index < ((CELL_HOR * CELL_VER) - (OUTER_CELLS * CELL_VER)):
            if OUTER_CELLS <= (index % CELL_VER) < (CELL_VER - OUTER_CELLS):
                grid[index].on_border = False


def draw_layers(_m_sel):

    screen.blit(s_background, (0, 0))
    screen.blit(s_grid, (s_grid_x, s_grid_y))
    draw_adjacents(grid, grid[last_loc])
    draw_selector(_m_sel)
    draw_group(bot_list)
    draw_group(byt_list)
    draw_group(item_list)
    pygame.display.flip()


# Draw the group of sprites
def draw_group(_group):

    _t_group = pygame.sprite.Group()
    for _sprite in _group.sprites():
        _t_group.add(_sprite)
    _t_group.draw(screen)


def draw_adjacents(_grid, _cell):

    adj_cells = _grid[_cell.loc].get_adjacent()

    # Width of cell selection
    sel_width = CELL_LINE_WIDTH + 2

    if adj_cells[0] != -1 and not grid[adj_cells[0]].on_border and check_cell(adj_cells[0]):
        pygame.draw.rect(screen, color.LIGHTBLUE, grid[adj_cells[0]].get_rect(), sel_width)
    elif adj_cells[0] != -1 and not grid[adj_cells[0]].on_border:
        pygame.draw.rect(screen, color.BLUE, grid[adj_cells[0]].get_rect(), sel_width)

    if adj_cells[1] != -1 and not grid[adj_cells[1]].on_border and check_cell(adj_cells[1]):
        pygame.draw.rect(screen, color.LIGHTBLUE, grid[adj_cells[1]].get_rect(), sel_width)
    elif adj_cells[1] != -1 and not grid[adj_cells[1]].on_border:
        pygame.draw.rect(screen, color.BLUE, grid[adj_cells[1]].get_rect(), sel_width)

    if adj_cells[2] != -1 and not grid[adj_cells[2]].on_border and check_cell(adj_cells[2]):
        pygame.draw.rect(screen, color.LIGHTBLUE, grid[adj_cells[2]].get_rect(), sel_width)
    elif adj_cells[2] != -1 and not grid[adj_cells[2]].on_border:
        pygame.draw.rect(screen, color.BLUE, grid[adj_cells[2]].get_rect(), sel_width)

    if adj_cells[3] != -1 and not grid[adj_cells[3]].on_border and check_cell(adj_cells[3]):
        pygame.draw.rect(screen, color.LIGHTBLUE, grid[adj_cells[3]].get_rect(), sel_width)
    elif adj_cells[3] != -1 and not grid[adj_cells[3]].on_border:
        pygame.draw.rect(screen, color.BLUE, grid[adj_cells[3]].get_rect(), sel_width)

    pygame.draw.rect(screen, color.YELLOW, _cell.get_rect(), sel_width + 1)


# Check for direction that the bot should move
def move_bot(_bot, _dir):

    if _dir == 0:
        _bot.move(grid[_bot.loc - 1])
    elif _dir == 1:
        _bot.move(grid[_bot.loc + CELL_VER])
    elif _dir == 2:
        _bot.move(grid[_bot.loc + 1])
    elif _dir == 3:
        _bot.move(grid[_bot.loc - CELL_VER])


# Spawn the bots on the sides of the screen
def spawn_rand():

    _ret = int(random.random() * 4)
    if _ret == 0:
        while True:
            _ret = int(random.random() * (CELL_HOR * CELL_VER))
            if _ret % CELL_VER == 0:
                break
    elif _ret == 1:
        _ret = ((CELL_HOR * CELL_VER) - 1) - int(random.random() * CELL_VER)
    elif _ret == 2:
        while True:
            _ret = int(random.random() * (CELL_HOR * CELL_VER))
            if _ret % CELL_VER == CELL_VER - 1:
                break
    elif _ret == 3:
        _ret = int(random.random() * CELL_VER)

    return _ret


# Draws the currently selected cell
def draw_selector(_pos):

    _index = 0
    for _cell in grid:
        if rect_contain(_cell, _pos):
            _sel_width = CELL_LINE_WIDTH + 2
            pygame.draw.rect(screen, color.HOT_PINK, _cell.get_rect(), _sel_width)
            break
        _index += 1


# Checks to see if there is a Unit in the cell
def check_cell(_loc):

    for _unit in bot_list:
        if _loc == _unit.loc:
            return True

    return False


# Initializes pygame and the mixer to prevent sound lag.
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

# Start Music
sound.play_music()

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
CELL_LINE_WIDTH = 2
draw_grid(True)

# Stores the index of the starting location and the previous location
last_loc = 112

# Stores the amount of times the player has made an action
step = 0

# Creating the groups for sprites. Items, BytBot - contains all characters, Bot - enemies
item_list = pygame.sprite.Group()
bytbot_list = pygame.sprite.Group()
bot_list = pygame.sprite.Group()
byt_list = pygame.sprite.Group()

# Create Characters - Initial
byt = player.Player(grid[last_loc], 'byt', 'Byt', last_loc)
byt_list.add(byt)
for i in range(1, 5):
    rand_loc = spawn_rand()
    bot = enemy.Enemy(grid[rand_loc], 'bot', 'Bot', rand_loc)
    bot_list.add(bot)

# Create items - initial
spark = item.Item(grid[55], 'spark', 'Spark', 55)  # debug
heart = item.Item(grid[70], 'heart', 'Heart', 70)  # debug
item_list.add(spark, heart)  # debug
for _item in item_list:
    _item.set_rect(grid[_item.loc])

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            t_list = check_click(pos, step, last_loc)
            step = t_list[0]
            last_loc = t_list[1]
        elif event.type == pygame.QUIT:
            sys.exit()
        draw_layers(pygame.mouse.get_pos())
        pygame.display.flip()
