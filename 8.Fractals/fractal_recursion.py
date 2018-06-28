import pyglet
from math import sin, cos, pi

class CircleOutline:
    def __init__(self, pos, radius, points, color):
        self.pos = pos
        self.radius = radius
        self.points = points
        self.color = color

    def show(self):
        # My attempt to draw a circle outline
        angle = 0
        increment = (pi * 2) / self.points
        for i in range(0, self.points):
            x = self.radius * sin(angle) + self.pos[0]
            y = self.radius * cos(angle) + self.pos[1]
            angle += increment

            pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ("v2f", tuple([x, y])), ("c3B", self.color))

def draw_fractal(x, y, size):
    CircleOutline((x, y), size, int(size * 2), (0, 0, 0)).show()
    # Here takes place the recursion
    if size > 2:
        draw_fractal(x + size / 2, y, size / 2)
        draw_fractal(x - size / 2, y, size / 2)


class Mainwindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(500, 500, "Fractal Recursion")

        pyglet.clock.schedule_interval(self.update, 1 / 10)

    def on_draw(self):
        self.clear()

        pyglet.gl.glClearColor(1, 1, 1, 1)
        draw_fractal(250, 250, 250)

    def update(self, dt):
        pass

window = Mainwindow()
pyglet.app.run()