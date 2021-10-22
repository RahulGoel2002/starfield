# starfield

from pygame import init,quit,QUIT
from pygame.display import set_mode,flip
from pygame.event import get
from pygame.time import Clock

# Globals
WIDTH,HEIGHT = 600,400
SCREEN = set_mode((WIDTH,HEIGHT))
FPSClock = Clock()
FPS = 32

if __name__ == "__main__":
	init()

	while True:
		for event in get():
			if event.type == QUIT:
				quit()
				exit()
		flip()
		FPSClock.tick(FPS)
