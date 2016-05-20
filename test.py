import pygame, math, sys
from pygame.locals import *
screen = pygame.display.set_mode((500,500))
character_image = pygame.image.load('car.png')
clock = pygame.time.Clock()
character_position = [0.0, 0.0]
character_speed = 5.0

while True :
	dt = clock.tick(60)
	pressed = pygame.key.get_pressed()
	# Frame
	if pressed[K_LEFT] :
		character_position[0] -= character_speed * dt
	if pressed[K_RIGHT] :
		character_position[0] += character_speed * dt
	if pressed[K_UP] :
		character_position[1] -= character_speed * dt
	if pressed[K_DOWN] :
		character_position[1] += character_speed * dt
	for event in pygame.event.get() :
		if hasattr(event, 'key') :
			if event.type == KEYDOWN :
				if event.key == K_ESCAPE :
					sys.exit(0)
	# Render
	screen.fill((0,0,0))
	screen.blit(character_image, (character_position[0], character_position[1]))
	pygame.display.flip()
