from p5 import *
import random

class Ball:
    """Simple ball class which can accept a vector as a force"""

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

        # It's important to reset the acceleration every frame!
        self.acc *= 0

        # print(round(self.pos.x, 1), round(self.pos.y, 1), end="\r")

    def apply_force(self, force):
        """Accepts a vector as a force. The force formula is F = A * M,
        where F is force, A is acceleration and M is mass, can also be written as A = F / M"""
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

        # Applies a force when the mouse is pressed
        if mouse_is_pressed:
            ball.apply_force(Vector(0, -0.55))

run()