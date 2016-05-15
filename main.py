import pygame, math, sys
from pygame.locals import *

if __name__ == '__main__' :
	screen = pygame.display.set_mode((1024, 768))
	clock = pygame.time.Clock()
	BLACK = (0, 0, 0)

	while 1: # Frame Routine
		# INPUT
		clock.tick(30)
		for event in pygame.event.get() :
			if not hasattr(event, 'key') :
				continue
			down = event.type == KEYDOWN
			if event.key == K_ESCAPE :
				sys.exit(0)
		screen.fill(BLACK)

		# FRAME

		# RENDER
		pygame.display.flip()