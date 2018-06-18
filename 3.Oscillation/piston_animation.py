from p5 import *
from math import pi
import keyboard as kb

class Engine:
    """Simulates a piston movement"""

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.r = self.size / 2
        self.angle = 0
        self.a_vel = 0
        self.a_acc = 0
        self.motion_pos = Vector(0, 0)
        self.started = False
        self.frames = [0, 0]

    def show(self):
        push_matrix()
        fill(155)
        rect_mode("CORNER")
        translate(width / 2, height / 2)
        scale = self.size * 1.2

        rect((-scale / 2, self.motion_pos.y - scale * 1.25), scale, scale * 0.2)
        line(self.motion_pos, (0, self.motion_pos.y - scale * 1.2))

        ellipse((self.pos.x, self.pos.y + width / 4), scale, scale)

        reset_matrix()
        # Casing TODO

    def control(self):
        if kb.is_pressed("A") and self.started:
            self.a_acc += 0.00005
        else:
            self.a_acc = 0

        if kb.is_pressed("I"):
            self.started = True
        if kb.is_pressed("S"):
            self.started = False

        if kb.is_pressed("SPACE"):
            self.a_vel *= 0.9

    def start(self):
        """Keep the engine in a idle rmp when it starts"""
        if self.a_vel < 0.15:
            self.a_acc += 0.005

    def update(self):
        """Updates the state of the engine"""

        # Calculates the right position using trigonometry
        self.motion_pos = Vector(self.r * sin(self.angle), (self.r * cos(self.angle)) + width / 4)
        if self.started:
            self.start()

        self.a_vel += self.a_acc 
        self.angle += self.a_vel

        if self.angle > pi * 2:
            self.frames.append(frame_count)
            self.angle = 0

        if len(self.frames) > 2:
            self.frames.pop(0)

        self.a_vel *= 0.99

    def calculate_speed(self):
        """Hacky way to calculate the 'rpm'"""
        frames_per_rotation = self.frames[1] - self.frames[0]
        if frames_per_rotation > 0:
            rpm = (frame_rate / frames_per_rotation) * 60
        else:
            rpm = 0
        return rpm

    def display_stats(self):
        if(frame_count % 17 == 0):
            print(f"ON: {self.started}", f"VEL: {round(self.a_vel, 2)}", f"ACC: {round(self.a_acc, 3)}", f"RPM: {int(self.calculate_speed())}")

engine = None

def setup():
    global engine
    size(500, 500)
    title("Piston Animation")

    engine = Engine(Vector(0, 0), 150)

def draw():
    background(255)

    engine.show()
    engine.update()
    engine.control()
    engine.display_stats()

run()