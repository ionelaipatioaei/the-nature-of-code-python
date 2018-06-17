from p5 import *

angle = 0
angle_vel = 0
angle_acc = 0.001

def setup():
    size(500, 500)
    title("Rotating Rectangle")

def draw():
    global angle, angle_vel, angle_acc

    background(255)

    angle_vel += angle_acc
    angle += angle_vel

    translate(width / 2, height / 2)
    rect_mode("CENTER")
    rotate(angle)
    fill(0)
    rect((0, 0), 64, 16)

    # Change direction if mouse is pressed
    if mouse_is_pressed:
        angle_acc *= -1

    print(angle_acc, angle_vel, end="\r")

run()