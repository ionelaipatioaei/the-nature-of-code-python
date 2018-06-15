from p5 import *
from random import randint
import math

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def add(self, vec):
		self.x += vec.x
		self.y += vec.y

	def sub(self, vec):
		self.x -= vec.x
		self.y -= vec.y

	def mult(self, amount):
		self.x *= amount
		self.y *= amount

	def div(self, amount):
		self.x /= amount
		self.y /= amount

	def mag(self):
		return math.sqrt(self.x ** 2 + self.y ** 2)

	def normalize(self):
		self.div(self.mag())

	def coord(self):
		return (self.x, self.y)

def rand_vector():
	return Vector(randint(0, width), randint(0, height))

pos = Vector(250, 250)
acc = Vector(-0.15, 0.21)

def setup():
	size(500, 500)
	background(255)

def draw():
	global pos
	global acc

	# background(255)
	no_stroke()
	fill(0,0,0, 10)

	ellipse(pos.coord(), 25, 25)
	pos.add(acc)

	if pos.x < 0 or pos.x > width:
		acc.x *= -1
	if pos.y < 0 or pos.y > height:
		acc.y *= -1

	# pos.normalize()
	print(pos.coord() ,end="\r")

	# print(round(pos.y, 0), acc, round(vel, 1), end="\r")


run()