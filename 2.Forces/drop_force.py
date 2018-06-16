from p5 import *
import random

class Liquid:
    def __init__(self, y_pos, drag_coeff):
        self.pos = Vector(0, y_pos)
        self.drag_coeff = drag_coeff

    def show(self):
        fill(155)
        no_stroke()
        rect(self.pos, width, height)

    def collide(self, obj):
        return obj.pos.y > self.pos.y

    def calculate_resistance(self, obj):
        speed = ((obj.vel.copy().magnitude) ** 2) * self.drag_coeff
        drag = obj.vel.copy()
        drag.normalize()
        drag *= speed * -1
        return drag

class Ball:
    def __init__(self, pos, mass):
        self.pos = pos
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.mass = mass
        self.size = self.mass * 20

    def show(self):
        fill(0)
        ellipse(self.pos, self.size, self.size)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel

        if self.pos.y > height:
            self.vel.y *= -1
            self.pos.y = height

        self.vel.limit(15)
        self.acc *= 0

    def apply_force(self, force):
        f = force / self.mass
        self.acc += f

liquid = None
balls = []

def setup():
    global liquid, ball

    size(500, 500)
    title("Drop force")

    liquid = Liquid(300, 0.04)
    for i in range(0, 10):
        balls.append(Ball(Vector(i * 50 + 20, 0), random.uniform(0.4, 3)))

def draw():
    background(255)
    liquid.show()

    for ball in balls:
        if mouse_is_pressed:
            ball.pos.y = 0
            mass = random.uniform(0.3, 3)
            ball.mass = mass
            ball.size = mass * 20
            ball.vel *= 0
            ball.acc *= 0

        ball.show()
        # Gravity force
        ball.apply_force(Vector(0, 0.1 * ball.mass))
        if liquid.collide(ball):
            ball.apply_force(liquid.calculate_resistance(ball))

        ball.update()

run()