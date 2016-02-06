import sys
import pygame
import color

pygame.init()


class Window:

    def __init__(self):

        self.width = 540
        self.height = 540
        self.CELL_HOR = 15
        self.CELL_VER = 15
        self.OUTER_CELLS = 2
        self.cell_width = int(self.width / self.CELL_HOR)
        self.cell_height = int(self.height / self.CELL_VER)
        self.screen_label = 'Code Ham Game'
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        self.s_background = pygame.Surface((self.width, self.height))
        self.clear_window()
        pygame.display.set_caption(self.screen_label)
        self.s_grid = pygame.Surface((self.width, self.height))
        self.grid_x = 0
        self.grid_y = 0

        # List to store cell coordinates
        self.grid = []
        self.sel_cells = [0]*4
        self.last_loc = [0, 0]
        # Constant of the cell border width
        self.GRID_CELL_WIDTH = 2
        self.draw_grid(True)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(pos)  # debug mouse position
                    self.check_click(pos)
                elif event.type == pygame.VIDEORESIZE:
                    self.init_sizes(event)
                    sub_width = self.s_grid.get_width()
                    sub_height = self.s_grid.get_height()
                    self.grid_x = int(self.width - sub_width) / 2
                    self.grid_y = int(self.height - sub_height) / 2
                    self.screen.blit(self.s_grid, (self.grid_x, self.grid_y))
                    self.clear_window()
                    self.draw_grid(False)
                    pygame.display.update()
                    print('Screen Change')
                elif event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()

    def init_sizes(self, event):

        size = [event.w, event.h]
        self.width = size[0]
        self.height = size[1]

    # draws the grid according to the screen size
    # during the first_run, draw_grid will add the
    # rects to a list
    def draw_grid(self, first_run):

        for x in range(0, self.width, self.cell_width):
            for y in range(0, self.height, self.cell_height):
                rect = pygame.Rect(x, y, self.cell_width, self.cell_height)
                if first_run:
                    self.grid.append(rect)
                pygame.draw.rect(self.s_grid, color.WHITE, rect, self.GRID_CELL_WIDTH)

    # checks for which grid you clicked in
    def check_click(self, pos):

        grid_index = 0
        for item in self.grid:
            if self.rect_contain(item, pos):
                print(grid_index)  # print place debug
                new_rect = pygame.Rect(item.x, item.y, self.cell_width, self.cell_height)
                self.clear_window()
                self.draw_grid(False)
                # Selectable grid choices
                self.sel_cells[0] = self.grid[grid_index - 1]
                self.sel_cells[1] = self.grid[grid_index + self.CELL_HOR]
                self.sel_cells[2] = self.grid[grid_index + 1]
                self.sel_cells[3] = self.grid[grid_index - self.CELL_HOR]
                # Draw the selectable locations
                pygame.draw.rect(self.s_grid, color.BLUE, self.sel_cells[0], self.GRID_CELL_WIDTH + 1)
                pygame.draw.rect(self.s_grid, color.BLUE, self.sel_cells[1], self.GRID_CELL_WIDTH + 1)
                pygame.draw.rect(self.s_grid, color.BLUE, self.sel_cells[2], self.GRID_CELL_WIDTH + 1)
                pygame.draw.rect(self.s_grid, color.BLUE, self.sel_cells[3], self.GRID_CELL_WIDTH + 1)
                pygame.draw.rect(self.s_grid, color.YELLOW, new_rect, self.GRID_CELL_WIDTH + 2)
                self.last_loc = item
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

    def clear_window(self):

        pygame.draw.rect(self.s_background, color.GRAY, (0, 0, self.width, self.height))

    def draw_layers(self):

        self.screen.blit(self.s_background, (self.width, self.height))
        self.screen.blit(self.s_grid, (self.grid_x, self.grid_y))
