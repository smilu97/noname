import pygame, math, sys
from pygame.locals import *
from Scene import *

class SceneMapTest(Scene):
	def __init__(self, screen, clock):
		Scene.__init__(self,screen, clock)
		font = pygame.font.SysFont('comicsansms', 25)
		self.objects['HelloText'] = GameObject(self)
		text = GameComponentImage(self.objects['HelloText'], font.render('Test', True, (255,255,255)))
		self.objects['HelloText'].components['image'] = text
	def Frame(self):
		self.clock.tick(30)
		self.events = pygame.event.get()
		for event in self.events :
			if hasattr(event, 'key') :
				if event.key == K_ESCAPE :
					sys.exit(0)
		for obj in self.objects.values() :
			obj.Frame()
	def Render(self):
		self.screen.fill((0,0,0))
		for obj in self.objects.values() :
			obj.Render()
		pygame.display.flip()
