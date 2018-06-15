from p5 import *

class Ball:
	"""Simple ball which stays on the screen"""

	def __init__(self):
		self.pos = Vector(width / 2, height / 2)
		self.acc = Vector(2, 3)

	def show(self):
		fill(0)
		ellipse(self.pos, 25, 25)

	def move(self):
		self.pos += self.acc

		if self.pos.x < 0 or self.pos.x > width:
			self.acc.x *= -1
		if self.pos.y < 0 or self.pos.y > height:
			self.acc.y *= -1
		print(self.pos, end="\r")

ball = None

def setup():
	global ball 
	
	size(500, 500)
	title("Boucing Ball")
	ball = Ball()

def draw():
	background(255)
	global ball
	ball.show()
	ball.move()

run()