import os,random
import pygame, math, sys
from pygame.locals import *

def CountLine() :
	s = 0
	for a, b, paths in os.walk('.') :
		for file in paths :
			if '.py' in file and (not '.pyc' in file) :
				print file,
				ifile = open(file, 'r')
				dat = ifile.read()
				ifile.close()
				l = len(dat.split('\n'))
				print l
				s += l
		break
	print s

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
spr = pygame.sprite.Sprite()
spr.image = pygame.image.load('ball.bmp')
spr.rect = (0,10)
pygame.transform.scale(spr.image, (10,10))
group = pygame.sprite.Group()
group.add(spr)
while True :
	dt = clock.tick(60)
	group.draw(screen)
	pygame.display.flip()
	for event in pygame.event.get() :
		if hasattr(event, 'key') and event.type == KEYDOWN :
			if event.key == K_ESCAPE :
				sys.exit(0)