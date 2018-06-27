import pyglet

WIDTH = 500
HEIGHT = 500

class CA:
    def __init__(self, cell_width, rule_set):
        self.cell_width = cell_width
        self.rule_set = rule_set
        self.cells = []
        for i in range(0, WIDTH // self.cell_width):
            self.cells.append(0)
        self.cells[WIDTH // self.cell_width // 2] = 1
        self.generation = 0

        self.history = [self.cells]

    def run(self):
        # I do not understand this bug, help needed!
        next_gen = [0] * len(self.cells)
        for i in range(1, len(self.cells) - 1):
            left = self.cells[i - 1]
            right = self.cells[i + 1]
            next_gen[i] = self.rules(left, self.cells[i], right)

            color = (122, 25, 0)
            if self.cells[i] == 0:
                color = (0, 125, 25)  
            self.rect((i * self.cell_width, WIDTH - self.cell_width - self.generation * self.cell_width), self.cell_width, self.cell_width, color)

        self.cells = next_gen
        self.history.append(self.cells)
        self.generation += 1
        
    def rect(self, pos, width, height, color):
        pyglet.graphics.draw(4, pyglet.gl.GL_TRIANGLE_STRIP, 
            ("v2f", (pos[0], pos[1], pos[0], pos[1] + height, pos[0] + width, pos[1], pos[0] + width, pos[1] + height)),
            ("c3B", tuple(color[i] for i in range(0, 3)) * 4))

    def rules(self, cell0, cell1, cell2):
        config = ((1, 1, 1, 1, 0, 0, 0, 0), (1, 1, 0, 0, 1, 1, 0, 0), (1, 0, 1, 0, 1, 0, 1, 0))
        for i in range(0, 8):
            if cell0 == config[0][i] and cell1 == config[1][i] and cell2 == config[2][i]:
                return self.rule_set[i]

class MainWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Better 1D CA")

        pyglet.clock.schedule_interval(self.update, 1 / 10)
        self.ca = CA(5, (0, 1, 0, 1, 1, 0, 1, 0))

    def on_draw(self):
        # self.clear()

        pyglet.gl.glClearColor(1, 1, 1, 1)

        if self.ca.generation < WIDTH // self.ca.cell_width:
            self.ca.run()

    def update(self, dt):
        pass

window = MainWindow()
pyglet.app.run()