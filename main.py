# starfield

from pygame import init,quit,QUIT
from pygame.display import set_mode,flip
from pygame.event import get
from pygame.time import Clock
from pygame.draw import circle,line
from random import random

# Globals
WIDTH,HEIGHT = 1050,700
SCREEN = set_mode((WIDTH,HEIGHT))
FPSClock = Clock()
FPS = 32

class Stars:
	def __init__(self):
		self.x = (random()*2-1)*WIDTH/2
		self.y = (random()*2-1)*HEIGHT/2
		self.z = random()*WIDTH

	def update(self):
		self.z -= 10
		if self.z < 1:
			self.z = WIDTH
			self.x = (random()*2-1)*WIDTH/2
			self.y = (random()*2-1)*HEIGHT/2

	def show(self):
		px = self.x/self.z * WIDTH
		py = self.y/self.z * HEIGHT
		px += WIDTH/2
		py += HEIGHT/2
		r = 5 - self.z/WIDTH * 5

		circle(SCREEN,(255,255,255),(px,py),r)
		

if __name__ == "__main__":
	init()
	stars = [None for _ in range(1000)]
	for i in range(len(stars)):
		stars[i] = Stars()	
	# r = 1

	while True:
		SCREEN.fill((0,0,0))

		for event in get():
			if event.type == QUIT:
				quit()
				exit()
		for star in stars:
			star.update()
			star.show()
		# circle(SCREEN,(255,45,0),(WIDTH/2,HEIGHT/2),r)
		# r += 0.01
		flip()
		FPSClock.tick(FPS)
