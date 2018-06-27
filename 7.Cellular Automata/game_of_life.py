import pyglet
from random import random

WIDTH = 600
HEIGHT = 600

class GameOfLife:
    def __init__(self, cell_size, alive):
        self.rows = WIDTH // cell_size
        self.cols = HEIGHT // cell_size
        self.cell_size = cell_size
        self.alive = alive
        self.cells = []
        # We generate the grid at the beginning
        self.generate_grid()

    def generate_grid(self):
        for row in range(0, self.rows):
            # Every row is an array with cells
            self.cells.append([])
            for col in range(0, self.cols):
                if random() < self.alive:
                    self.cells[row].append(1)
                else:
                    self.cells[row].append(0)

    def run_rules(self):
        # Generates a list with only dead cells as a template
        temp = list([[0 for i in range(0, self.rows)] for i in range(0, self.cols)])
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                # Apply the rules of the game of life
                if self.cells[row][col] == 1 and self.get_cell_neighbors(row, col) < 2: # Loneliness
                    temp[row][col] = 0
                elif self.cells[row][col] == 1 and self.get_cell_neighbors(row, col) > 3: # Overpopulation
                    temp[row][col] = 0
                elif self.cells[row][col] == 0 and self.get_cell_neighbors(row, col) == 3: # Reproduction
                    temp[row][col] = 1
                else: # Stasis
                    temp[row][col] = self.cells[row][col]
        # Replace the grid
        self.cells = temp

    def get_cell_neighbors(self, r, c):
        neighbors = 0
        # The coordinates for the neighbors
        check_row = (-1, 0, 1, -1, 1, -1, 0, 1)
        check_col = (-1, -1, -1, 0, 0, 1, 1, 1)
        for i in range(0, 8):
            # check the state of the neighbors
            if r + check_row[i] < 0 or r + check_row[i] > self.rows - 1 or c + check_col[i] < 0 or c + check_col[i] > self.cols - 1:
                pass
            elif self.cells[r + check_row[i]][c + check_col[i]] == 1:
                neighbors += 1
        return neighbors

    def show(self):
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                color = (0, 0, 0)
                if self.cells[row][col] == 1:
                    color = (255, 255, 255)
                self.rect((row * self.cell_size, col * self.cell_size), self.cell_size, self.cell_size, color)

    def rect(self, pos, width, height, color):
        pyglet.graphics.draw(4, pyglet.gl.GL_TRIANGLE_STRIP, 
            ("v2f", (pos[0], pos[1], pos[0], pos[1] + height, pos[0] + width, pos[1], pos[0] + width, pos[1] + height)),
            ("c3B", tuple(color[i] for i in range(0, 3)) * 4))


class MainWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Game of Life")

        pyglet.clock.schedule_interval(self.update, 1 / 10)

        self.gof = GameOfLife(15, 0.5)

    def on_draw(self):
        self.clear()

        pyglet.gl.glClearColor(1, 1, 1, 1)

        self.gof.show()
        self.gof.run_rules()

    def update(self, dt):
        pass

window = MainWindow()
pyglet.app.run()