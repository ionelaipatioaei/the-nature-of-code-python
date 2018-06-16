from p5 import *
from random import randint

class Sun:
    """An object which can't move on its own and attracts other objects"""

    def __init__(self, pos, mass):
        self.pos = pos
        self.mass = mass
        self.g = 1

    def show(self):
        fill(240,230,140)
        no_stroke()
        circle(self.pos, self.mass * 5)

    def attract(self, planet):
        """Calculates the attraction force using this formula:
        F = ((g * m1 * m2) / r^2) * r^, where
        F is the result, g is the universal gravitational constant, we can make the force stronger or weaker, 
        usually is left 1 in the programming world, m1 and m2 are the masses of the Sun and the provided object,
        r^ is the unit vector pointing from object 1(the Sun) and object 2, i.e: (self.pos - planet.pos).normalize(),
        r^2 is the distance between the two objects squared, i.e: ((self.pos - planet.pos).magnitude) ** 2
        """
        force = self.pos.copy() - planet.pos.copy()
        dist = force.magnitude
        dist = constrain(dist, 5, 20)
        strenght = (self.g * self.mass * planet.mass) / (dist ** 2)
        force.normalize()
        force *= strenght
        return force

    def constrain(val, min_val, max_val):
        return min(max_val, max(min_val, val))

class Planet:
    """An objects which is attracted by the Sun"""

    def __init__(self, pos, mass):
        self.pos = pos
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.mass = mass
        self.red = randint(0, 255)

    def show(self):
        fill(self.red, 0, 0)
        ellipse(self.pos, self.mass * 10, self.mass * 10)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel

        self.vel.limit(5)
        self.acc *= 0

    def apply_force(self, force):
        f = force / self.mass
        self.acc += f

sun = None
planet = None

def setup():
    global sun, planet

    size(500, 500)
    title("Gravitational Attraction")

    sun = Sun(Vector(width / 2, height / 2), 20)
    planet = Planet(Vector(100, 100), 2)

def draw():
    background(255)

    sun.show()

    planet.apply_force(sun.attract(planet))
    # print(sun.attract(planet), planet.vel, end="\r")

    # Moves the Sun at the mouse coords
    if mouse_is_pressed:
        sun.pos = Vector(mouse_x, mouse_y)

    planet.show()
    planet.update()

run()