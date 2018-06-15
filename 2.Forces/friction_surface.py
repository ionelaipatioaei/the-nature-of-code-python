from p5 import *

class Obj:
    """An object represented as an rectangle, when it hits the 'floor' 
    the friction is applied until the object stops"""

    def __init__(self, pos, mass):
        self.pos = pos
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.mass = mass

    def show(self):
        fill(0)
        size = self.mass * 20
        rect(self.pos, size, size)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel

        if self.pos.x < 0:
            self.pos.x = width
        if self.pos.x > width:
            self.pos.x = 0

        if self.pos.y > 260:
            self.pos.y = 260

        # self.vel.limit(10)
        self.acc *= 0

    def apply_force(self, force):
        f = force / self.mass
        self.acc += f

obj = None

def setup():
    global obj
    obj = Obj(Vector(0, 0), 2)

    size(500, 500)
    title("Friction Surface")

def draw():
    background(255)

    obj.apply_force(Vector(0, 0.1))
    obj.apply_force(Vector(0.05, 0))

    # If the objeçt 'hits' the floor apply friction
    if obj.pos.y == 260:
        friction = obj.vel.copy()
        friction.normalize()
        friction *= -0.15

        obj.apply_force(friction)

    obj.show()
    obj.update()

    # print(obj.vel)

    # Create the surface
    fill(100)
    no_stroke()
    rect((0, 300), width, height)

run()