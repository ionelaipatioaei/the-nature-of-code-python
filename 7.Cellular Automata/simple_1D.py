import pyglet

# WARNING, VERY POOR IMPLEMENTATION OF 1D CELLULAR AUTOMATA

class Rect:
    def __init__(self, pos, width, height, color):
        self.pos = pos
        self.w = width
        self.h = height
        self.color = color

    def show(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_TRIANGLE_STRIP, 
            ("v2f", (self.pos[0], self.pos[1], self.pos[0], self.pos[1] + self.h, self.pos[0] + self.w, self.pos[1], self.pos[0] + self.w, self.pos[1] + self.h)),
            ("c3B", tuple(self.color[i] for i in range(0, 3)) * 4))

class CA:
    def __init__(self, width, rule_set):
        self.width = width
        self.rule_set = rule_set
        self.cells_amount = int(500 / self.width)
        self.cells = []
        for i in range(0, self.cells_amount):
            self.cells.append(0)
        self.cells[self.cells_amount // 2] = 1
        self.generation = 0

        self.history = []
        self.history.append(self.cells)
        
    def generate(self):
        next_gen = list(0 for i in range(0, self.cells_amount))
        for i in range(1, len(self.cells) - 1):
            left = self.cells[i - 1]
            right = self.cells[i + 1]
            next_gen[i] = self.rules(left, self.cells[i], right)
        self.cells = next_gen
        self.history.append(self.cells)
        self.generation += 1

    def show(self):
        # Here lies the problem, for some reason the y coord is updated weirdly if you use the
        # code which is commented. Using the second one works fine but is VERY SLOW

        # for i in range(0, self.cells_amount):
        #     color = (255, 0, 0)
        #     if self.cells[i] == 1:
        #         color = (0, 255, 0)
        #     Rect((i * self.width, 495 - self.generation * self.width), self.width, self.width, color).show()
                
        for i in range(0, len(self.history)):
            for j in range(0, self.cells_amount):
                color = (255, 0, 0)
                if self.history[i][j] == 1:
                    color = (0, 255, 0)
                Rect((j * self.width, 495 - i * self.width), self.width, self.width, color).show()

    def rules(self, cell0, cell1, cell2):
        if cell0 == 1 and cell1 == 1 and cell2 == 1:
            return self.rule_set[0]
        if cell0 == 1 and cell1 == 1 and cell2 == 0:
            return self.rule_set[1]
        if cell0 == 1 and cell1 == 0 and cell2 == 1:
            return self.rule_set[2]
        if cell0 == 1 and cell1 == 0 and cell2 == 0:
            return self.rule_set[3]
        if cell0 == 0 and cell1 == 1 and cell2 == 1:
            return self.rule_set[4]
        if cell0 == 0 and cell1 == 1 and cell2 == 0:
            return self.rule_set[5]
        if cell0 == 0 and cell1 == 0 and cell2 == 1:
            return self.rule_set[6]
        if cell0 == 0 and cell1 == 0 and cell2 == 0:
            return self.rule_set[7]

class MainWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(500, 500, "Simple 1D CA")

        pyglet.clock.schedule_interval(self.update, 1 / 30)

        self.rule_set = ((0, 1, 0, 1, 1, 0, 1, 0), (1, 0, 1, 1, 1, 1, 0, 0))
        self.ca = CA(5, self.rule_set[1])

    def on_draw(self):
        # self.clear()

        # pyglet.gl.glClearColor(1, 1, 1, 1)
        self.ca.show()
        if self.ca.generation < 500 / self.ca.width:
            self.ca.generate()
        
    def update(self, dt):
        pass

window = MainWindow()
pyglet.app.run()