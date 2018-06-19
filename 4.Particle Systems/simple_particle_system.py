from p5 import *
from random import uniform

class Particle:
    """The particle class defines the behaviour of a single particle"""

    def __init__(self, pos, size):
        self.pos = pos
        self.vel = Vector(0, 0)
        self.acc = Vector(uniform(-0.009, 0.009), uniform(0, 0.1))
        self.size = size
        # The lifespan is used to to define how much the particle will live
        self.lifespan = 255

    def show(self):
        no_stroke()
        fill(155, self.lifespan)
        circle(self.pos, self.size)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel

        self.lifespan -= 1.75

    def is_dead(self):
        return self.lifespan <= 0

class ParticleSystem:
    """The particle system class is used to group together multiple particles"""

    def __init__(self, pos):
        self.pos = pos
        self.elements = []

    def update(self):
        x_coord = uniform(self.pos.x - 25, self.pos.x + 25)
        y_coord = uniform(self.pos.y - 25, self.pos.y + 25)
        # Every 7 frames a particle is born
        if frame_count % 7 == 0:
            self.elements.append(Particle(Vector(x_coord, y_coord), uniform(10, 20)))

        # It is important to loop through an array backwards
        for i in range(len(self.elements) - 1, -1, -1):
            self.elements[i].show()
            self.elements[i].update()
            if self.elements[i].is_dead():
                self.elements.pop(i)
        print(len(self.elements))


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

    # print(len(particle_systems))

# This function is invoked only once when the mouse is pressed even if you keep it pressed 
def mouse_pressed():
    # Creates a new particle system at the mouse coords
    particle_systems.append(ParticleSystem(Vector(mouse_x, mouse_y)))

run()