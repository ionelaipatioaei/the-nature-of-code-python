from p5 import *
from random import uniform, randint

class Particle:
    """This class defines a single particle"""

    def __init__(self, pos):
        self.pos = pos
        self.vel = Vector(0, 0)
        self.acc = Vector(uniform(-0.01, 0.01), uniform(0, 0.1))
        self.lifespan = 255
        self.size = uniform(10, 20)

    def show(self):
        fill(127, self.lifespan)
        no_stroke()
        ellipse(self.pos, self.size, self.size)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel

        self.lifespan -= 2

    def is_dead(self):
        return self.lifespan <= 0

class SquareParticle(Particle):
    """This class inherits the particle characteristics and overrides the show method(displays squares instead of circles)"""

    def __init__(self, pos):
        super().__init__(pos)

    def show(self):
        fill(127, self.lifespan)
        no_stroke()
        rect_mode("CENTER")
        rect(self.pos, self.size, self.size)

class ParticleSystem:
    """This class keeps track of all the particles"""

    def __init__(self, pos):
        self.pos = pos
        self.particles = []

    def run(self):
        if frame_count % 7 == 0:
            x_coord = uniform(self.pos.x - 20, self.pos.x + 20)
            y_coord = uniform(self.pos.y - 20, self.pos.y + 20)
            # Technically this is polymorphism
            if randint(0, 10) > 5:
                self.particles.append(SquareParticle(Vector(x_coord, y_coord)))
            else:
                self.particles.append(Particle(Vector(x_coord, y_coord)))
        if len(self.particles) > 0:
            for i in range(len(self.particles) - 1, -1, -1):
                self.particles[i].show()
                self.particles[i].update()
                if self.particles[i].is_dead():
                    self.particles.pop(i)

particle_system = None

def setup():
    global particle_system

    size(500, 500)
    title("Inheritance and Polymorphism")

    particle_system = ParticleSystem(Vector(width / 2, 20))

def draw():
    background(255)

    particle_system.run()

run()