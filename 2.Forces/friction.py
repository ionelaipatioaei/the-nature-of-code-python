from p5 import *

class Ball:
    def __init__(self, pos, mass):
        self.pos = pos
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.mass = mass

    def show(self):
        fill(0)
        size = self.mass * 20
        ellipse(self.pos, size, size)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel

        if self.pos.y < 0 or self.pos.y > height:
            self.vel.y *= -1

        self.acc *= 0

    def apply_force(self, force):
        f = force / self.mass
        self.acc += f

ball =  None

def setup():
    global ball

    size(500, 500)
    title("Friction")

    ball = Ball(Vector(width / 2, height /2), 1.5)


def draw():
    background(255)

    ball.show()
    ball.update()

    ball.apply_force(Vector(0, 0.2))

    if mouse_is_pressed:
        friction = ball.vel.copy()
        friction.normalize()
        friction *= -0.1

        ball.apply_force(friction)

run()