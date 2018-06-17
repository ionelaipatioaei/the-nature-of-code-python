from p5 import *
import keyboard

r = 150
angle = 0
angle_vel = 0
angle_acc = 0.0001

def setup():
	size(500, 500)
	title("Trigonometry Motion")

def draw():
	global angle, angle_vel, angle_acc

	background(255)
	angle_vel += angle_acc
	angle += angle_vel

	translate(width / 2, height / 2)
	fill(0)

	"""Using trigonometry we can get the x and y coords.
	Sine, cosine and tangent(sin, cos and tan) are the main functions used is trigonometry and 
	are based on a right angle triangle and are each a ratio of sides.
	sin = opposite / hypotenuse
	cos = adjacent / hypotenuse
	tan = opposite / adjacent
	"""
	x = r * sin(angle)
	y = r * cos(angle)
	line((0, 0), (x, y))
	ellipse((x, y), 30, 30)

	# Change direction if mouse is pressed
	if mouse_is_pressed:
		angle_acc *= -1

	# keyboard module used for keyboard input
	# Install using: pip install keyboard

	# If up key is pressed increase acceleration, if down key is pressed decrease
	if keyboard.is_pressed("UP"):
		angle_acc += 0.0001
	if keyboard.is_pressed("DOWN"):
		angle_acc -= 0.0001

	print(angle_acc, angle_vel, end="\r")

run()