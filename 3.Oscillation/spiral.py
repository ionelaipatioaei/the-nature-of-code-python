from p5 import *
from random import randint

r = 0
angle = 0

def setup():
    size(500, 500)
    title("Gray Spiral")
    background(255)

def draw():
    global r, angle

    translate(width / 2, height /2)
    no_stroke()
    fill(randint(0, 255))

    # Using a for loop we can calculate 100 times the r and the angle is just 1 frame,
    # this speeds up the render process
    for i in range(0, 100):
        r += 0.0025
        angle += 0.001

        x = r * sin(angle)
        y = r * cos(angle)
        ellipse((x, y), 8, 8)


run()