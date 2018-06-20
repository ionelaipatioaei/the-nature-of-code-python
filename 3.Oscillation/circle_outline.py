from p5 import *
import math
import keyboard

class CircleOutline:
    def __init__(self, pos, radius, points):
        self.pos = pos
        self.radius = radius
        self.points = points
        self.angle = 0

    def show(self):
        increment = (math.pi * 2) / self.points
        for i in range(0, self.points):
            x = self.radius * sin(self.angle) + self.pos.x
            y = self.radius * cos(self.angle) + self.pos.y
            line((self.pos.x, self.pos.y), (x, y))
            self.angle += increment

    def update(self):
        """You can easily play around with the values using the keyboard"""
        if keyboard.is_pressed("LEFT"):
            self.angle += 0.01

        if keyboard.is_pressed("RIGHT"):
            self.angle -= 0.01

        if keyboard.is_pressed("A"):
            self.points += 1

        if keyboard.is_pressed("D") and self.points > 1:
            self.points -= 1

        if keyboard.is_pressed("UP"):
            self.radius += 1

        if keyboard.is_pressed("DOWN"):
            self.radius -= 1

circle = None

def setup():
    global circle

    size(500, 500)
    title("Circle line")

    circle = CircleOutline(Vector(width / 2, height / 2), 128, 32)

def draw():
    background(255)

    circle.show()
    circle.update()

run()