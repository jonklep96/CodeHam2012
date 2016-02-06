import sys
import pygame
import color

pygame.init()


class Window:

    def __init__(self):

        self.width = 600
        self.height = 600
        self.CELL_HOR = 10
        self.CELL_VER = 15
        self.cell_width = int(self.width / self.CELL_HOR)
        self.cell_height = int(self.height / self.CELL_VER)

        # Create a window with the Surface screen
        self.screen_label = 'Code Ham Game'
        pygame.display.set_caption(self.screen_label)
        self.screen = pygame.display.set_mode((self.width, self.height))

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
        self.last_loc = self.CELL_VER * 2 + self.OUTER_CELLS

        # Draw the layers to the screen
        self.draw_layers()

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
                    self.draw_grid(False)

                    # Selectable grid choices
                    self.sel_cells[0] = self.grid[grid_index - 1]
                    self.sel_cells[1] = self.grid[grid_index + self.CELL_VER]
                    self.sel_cells[2] = self.grid[grid_index + 1]
                    self.sel_cells[3] = self.grid[grid_index - self.CELL_VER]

                    # Remove the previous selected cells
                    self.draw_layers()

                    # Width of cell selection
                    sel_width = self.GRID_CELL_WIDTH + 2

                    # Draw the selectable locations
                    if self.is_movable(grid_index - 1, grid_index):
                        pygame.draw.rect(self.screen, color.BLUE, self.sel_cells[0], sel_width)
                    if self.is_movable(grid_index + self.CELL_VER, grid_index):
                        pygame.draw.rect(self.screen, color.BLUE, self.sel_cells[1], sel_width)
                    if self.is_movable(grid_index + 1, grid_index):
                        pygame.draw.rect(self.screen, color.BLUE, self.sel_cells[2], sel_width)
                    if self.is_movable(grid_index - self.CELL_VER, grid_index):
                        pygame.draw.rect(self.screen, color.BLUE, self.sel_cells[3], sel_width)
                    pygame.draw.rect(self.screen, color.YELLOW, sel_cell, sel_width + 1)
                    self.last_loc = grid_index
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
        cell_hor = self.CELL_HOR
        cell_ver = self.CELL_VER

        if index >= (outer_cells * cell_ver):
            if index < ((cell_hor * cell_ver) - (outer_cells * cell_ver)):
                if outer_cells <= (index % cell_ver) < (cell_ver - outer_cells):
                    return False

        return True

    def draw_layers(self):

        self.screen.blit(self.s_background, (0, 0))
        self.screen.blit(self.s_grid, (self.grid_x, self.grid_y))
        pygame.display.flip()

    def is_movable(self, sel_index, cell_check):

        cell_ver = self.CELL_VER

        if not self.is_outer_border(sel_index):
            if sel_index == (cell_check - 1) or sel_index == (cell_check + cell_ver):
                return True
            if sel_index == (cell_check + 1) or sel_index == (cell_check - cell_ver):
                return True

        return False
