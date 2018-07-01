from p5 import *
from random import randint

xoff = 0
yoff = 0

def setup():
    global xoff, yoff
    size(300, 300)
    title("2D Perlin Noise")

    for x in range(0, width):
        for y in range(0, height):
            brightness = remap(noise(xoff, yoff), (0, 1), (0, 255))
            stroke(brightness)
            point(x, y)
            yoff += 0.01
        xoff += 0.01

def draw():
    pass

run()