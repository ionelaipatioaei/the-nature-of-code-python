from p5 import *

class Ball:
	"""A simple ball which goes towards the mouse"""
	def __init__(self, pos):
		self.pos = pos
		self.vel = Vector(0, 0)
		self.acc = None
		self.size = 20

	def show(self):
		fill(0)
		ellipse(self.pos, self.size, self.size)

	def side(self):
		if self.pos.x < (0 - self.size / 2):
			self.pos.x = width
		if self.pos.x > (width + self.size / 2):
			self.pos.x = 0
		if self.pos.y < (0 - self.size / 2):
			self.pos.y = height
		if self.pos.y > (height + self.size / 2):
			self.pos.y = 0

	def update(self):
		self.pos += self.vel

		target = Vector(mouse_x, mouse_y)
		# Calculates the distance between the mouse and the ball
		dist = (target - self.pos)
		dist.normalize()
		# print(dist)

		# The normalized distance is the added to the velocity
		self.vel += (dist * 0.1)
		self.vel.limit(3)
		self.side()

ball = None;

def setup():
	global ball
	size(500, 500)
	title("Towards the Mouse")

	ball = Ball(Vector(width / 2, height / 2))

def draw():
	background(255)

	ball.show()
	ball.update()

run()