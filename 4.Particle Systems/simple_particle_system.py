from p5 import *
from random import uniform

class Particle:
    def __init__(self, pos, size):
        self.pos = pos
        self.vel = Vector(0, 0)
        self.acc = Vector(uniform(-0.009, 0.009), uniform(0, 0.1))
        self.size = size
        self.lifespan = 255

    def show(self):
        no_stroke()
        fill(155, self.lifespan)
        circle(self.pos, self.size)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel

        self.lifespan -= 1.75

    def isDead(self):
        return self.lifespan <= 0

class ParticleSystem:
    def __init__(self, pos):
        self.pos = pos
        self.elements = []

    def update(self):
        x_coord = uniform(self.pos.x - 25, self.pos.x + 25)
        y_coord = uniform(self.pos.y - 25, self.pos.y + 25)
        if frame_count % 7 == 0:
            self.elements.append(Particle(Vector(x_coord, y_coord), uniform(10, 20)))

        for i in range(len(self.elements) - 1, -1, -1):
            self.elements[i].show()
            self.elements[i].update()
            if self.elements[i].isDead():
                self.elements.pop(i)
        # print(len(self.elements))


particle_systems = []

def setup():
    size(500, 500)
    title("Simple Particle System")
    
def draw():
    global particle_systems
    background(255)

    if len(particle_systems) > 0:
        for particle_system in particle_systems:
            particle_system.update()

    print(len(particle_systems))

def mouse_pressed():
    particle_systems.append(ParticleSystem(Vector(mouse_x, mouse_y)))

run()