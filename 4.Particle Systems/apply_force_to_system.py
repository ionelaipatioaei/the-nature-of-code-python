from p5 import *
from random import uniform

class Particle:
    """Single particle class"""

    def __init__(self, pos):
        self.pos = pos
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.size = uniform(10, 20)
        self.lifespan = 255

    def show(self):
        fill(0, self.lifespan)
        no_stroke()
        ellipse(self.pos, self.size, self.size)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel

        self.lifespan -= 1.9
        self.acc *= 0

    def is_dead(self):
        return self.lifespan <= 0

    def apply_force(self, force):
        f = force / self.size
        self.acc += f

class Repeller:
    """This object repels other objects"""

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

    def show(self):
        fill(0, 50)
        no_stroke()
        ellipse(self.pos, self.size, self.size)

    def repel(self, particle):
        """TODO: remake this formula"""
        di = self.pos.copy() - particle.pos.copy()
        d = di.magnitude
        di.normalize()
        force = -1 / (d * d) * 1000
        di *= force
        return di

class ParticleSystem:
    """This class keeps track of all particles"""

    def __init__(self, pos):
        self.pos = pos
        self.particles = []

    def run(self):
        if frame_count % 7 == 0:
            x = uniform(self.pos.x - 20, self.pos.x + 20)
            y = uniform(self.pos.y - 20, self.pos.y + 20)
            self.particles.append(Particle(Vector(x, y)))

        for i in range(len(self.particles) - 1, -1, -1):
            self.particles[i].show()
            self.particles[i].update()
            if self.particles[i].is_dead():
                self.particles.pop(i)

    def apply_force(self, force):
        for particle in self.particles:
            particle.apply_force(force)

    def apply_repeller(self, repeller):
        """Apply the force from a repeller"""
        for particle in self.particles:
            force = repeller.repel(particle)
            particle.apply_force(force)

        # print(len(self.particles))

particle_system = None
repeller = None

def setup():
    global particle_system, repeller

    size(500, 500)
    title("Apply Force to Particle System")

    particle_system = ParticleSystem(Vector(width / 2, 0))
    repeller = Repeller(Vector(width / 2, height / 2), 60)

def draw():
    background(255)

    particle_system.run()
    particle_system.apply_force(Vector(0, 1))
    particle_system.apply_repeller(repeller)

    repeller.show()

    if mouse_is_pressed:
        particle_system.apply_force(Vector(-2, -1.1))

run()