import pyglet
from math import pi, sin, cos, sqrt
from random import uniform

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y

    def sub(self, vec):
        self.x -= vec.x
        self.y -= vec.y

    def mult(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def div(self, scalar):
        self.x /= scalar
        self.y /= scalar

    def mag(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        m = self.mag()
        self.div(m)

    def limit(self, limit):
        m_sq = self.mag() ** 2
        if m_sq > limit ** 2:
            self.div(sqrt(m_sq))
            self.mult(limit)

    def copy(self):
        return Vec2(self.x, self.y)

class Circle:
    def __init__(self, pos, radius, color):
        self.pos = pos
        self.radius = radius
        self.color = color

    def show(self):
        angle = 0
        increment = (pi * 2) / int(self.radius)
        vertices = []
        for i in range(0, int(self.radius)):
            x = self.radius * sin(angle) + self.pos.x
            y = self.radius * cos(angle) + self.pos.y
            vertices.append(x)
            vertices.append(y)
            angle += increment

        pyglet.graphics.draw(int(self.radius), pyglet.gl.GL_TRIANGLE_FAN, ("v2f", vertices), ("c4B", tuple(self.color[i] for i in range(0, 4)) * int(self.radius)))

class Creature:
    def __init__(self, pos, size, color):
        self.pos = pos
        self.vel = Vec2(0, 0)
        self.acc = Vec2(0, 0)
        self.size = size
        self.color = color

    def show(self):
        Circle(self.pos, self.size / 2, self.color).show()

    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)

        if self.pos.x < 0 or self.pos.x > window.width:
            self.vel.x *= -1
        elif self.pos.y < 0 or self.pos.y > window.height:
            self.pos.y *= -1

        self.acc.mult(0)

    def apply_force(self, force):
        self.acc.add(force)

    def go_to(self, target):
        desired = target.pos.copy()
        desired.sub(self.pos)

        dist = desired.mag()

        desired.normalize()
        desired.mult(2)

        steer = desired.copy()
        steer.sub(self.vel)

        # Limit how much the creature can steer towards the target
        steer.limit(0.03)
        print(steer.mag())

        # Apply the force only if the creature is close to the target
        if dist < 200:
            self.apply_force(steer)
        else:
            self.apply_force(Vec2(uniform(-0.1, 0.1), uniform(-0.1, 0.1)))

class MainWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(500, 500, "Steering Behaviors Seek")

        pyglet.clock.schedule_interval(self.update, 1 / 60)

        self.target = Circle(Vec2(250, 250), 15, (255, 0, 0, 255))

        self.creature = Creature(Vec2(200, 200), 20, (0, 255, 0, 255))

    def on_draw(self):
        self.clear()

        pyglet.gl.glClearColor(1, 1, 1, 1)

        # Activates alpha
        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

        self.target.show()

        self.creature.show()
        self.creature.update()


        # self.creature.apply_force(Vec2(0, 0.01))
        self.creature.go_to(self.target)

    def on_mouse_motion(self, x, y, dx, dy):
        self.target.pos = Vec2(x, y)

    def update(self, dt):
        pass

window = MainWindow()
pyglet.app.run()