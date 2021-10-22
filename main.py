# starfield

from pygame import init,quit,QUIT
from pygame.display import set_mode,flip
from pygame.event import get
from pygame.time import Clock
from pygame.draw import circle
from random import random

# Globals
WIDTH,HEIGHT = 600,400
SCREEN = set_mode((WIDTH,HEIGHT))
FPSClock = Clock()
FPS = 32

class Stars:
	def __init__(self):
		self.x = (random()*2-1)*WIDTH/2
		self.y = (random()*2-1)*HEIGHT/2
		self.z = WIDTH

	def update(self):
		self.z -= 1

	def show(self):
		px = x/z * WIDTH
		py = y/z * HEIGHT
		px += WIDTH/2
		py += HEIGHT/2

		circle(SCREEN,(255,255,255),(px,py),4)


if __name__ == "__main__":
	init()
	stars = [None for _ in range(100)]
	for i in range(len(stars)):
		stars[i] = Stars()	

	while True:
		SCREEN.fill((0,0,0))
		for event in get():
			if event.type == QUIT:
				quit()
				exit()
		for star in stars:
			star.show()
		flip()
		FPSClock.tick(FPS)
