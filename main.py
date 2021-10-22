# starfield

from pygame import init,quit,QUIT,KEYDOWN,K_SPACE
from pygame.display import set_mode,flip
from pygame.event import get
from pygame.time import Clock
from pygame.draw import circle,line
from random import random
from pygame.key import set_repeat

# Globals
WIDTH,HEIGHT = 1050,700
SCREEN = set_mode((WIDTH,HEIGHT))
FPSClock = Clock()
FPS = 32
speed = 1
acc = 3
set_repeat(100)

class Stars:
	def __init__(self):
		self.x = (random()*2-1)*WIDTH/2
		self.y = (random()*2-1)*HEIGHT/2
		self.z = random()*WIDTH

	def update(self):
		self.z -= speed
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
		accelerating = False
		SCREEN.fill((0,0,0))

		for event in get():
			if event.type == QUIT:
				quit()
				exit()
			elif event.type == KEYDOWN and event.key == K_SPACE:
				speed += acc
				if speed > 30:
					speed = 30
				# print(speed)
				acc -= 1
				if acc <= 0.2:
					acc = 0.2
				accelerating = True
		for star in stars:
			star.update()
			star.show()
		# circle(SCREEN,(255,45,0),(WIDTH/2,HEIGHT/2),r)
		# r += 0.01
		speed -= 0.05
		if speed < 1:
			speed = 1
		
		if not accelerating:
			acc = 3

		flip()
		FPSClock.tick(FPS)
