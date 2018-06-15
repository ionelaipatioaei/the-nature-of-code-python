from p5 import *
from random import randint

class Walker():
	def __init__(self, x, y):
		self.pos = Vector(x, y)

	def show(self):
		fill(0)
		rect(self.pos, 1, 1)

	def move(self):
		r = randint(0, 4)
		if r == 0:
			self.pos.x += 1
		elif r == 1:
			self.pos.x -+ 1
		elif r == 2:
			self.pos.y += 1
		elif r == 3:
			self.pos.y -= 1

w = Walker(width / 2, height / 2)

def setup():
	size(500, 500)

def draw():
	background(255)
	global w
	w.show()
	w.move()

run()