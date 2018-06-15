from p5 import *
import random

class Ball:
    def __init__(self, pos, mass):
        self.pos = pos
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.mass = mass

    def show(self):
        fill(0)
        ellipse(self.pos, self.mass * 25, self.mass * 25)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel

        if self.pos.x < 0 or self.pos.x > width:
            self.vel.x *= -1
        if self.pos.y < 0 or self.pos.y > height:
            self.vel.y *= -1

        self.acc *= 0

        print(round(self.pos.x, 1), round(self.pos.y, 1), end="\r")

    def apply_force(self, force):
        f = force / self.mass
        self.acc += f

balls = []

def setup():
    global balls

    size(500, 500)
    title("Aplying Force")
    for i in range(25):
        balls.append(Ball(Vector(random.randint(0, width), random.randint(0, height)), random.uniform(0, 3)))

def draw():
    background(255)

    for ball in balls:
        ball.show()
        ball.update()
        ball.apply_force(Vector(0, 0.3))

        if mouse_is_pressed:
            ball.apply_force(Vector(0, -0.55))

run()