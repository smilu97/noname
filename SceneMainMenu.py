import pygame, math, sys
from pygame.locals import *
from Scene import *		

class SceneMainMenu(Scene):
	"""docstring for MainMenu"""
	def __init__(self, screen, clock):
		Scene.__init__(self, screen, clock)
		font = pygame.font.SysFont('comicsansms', 25)
		TestButton = GameObjectButton(self, font.render('Start', True, (255,255,255)), self.OnStart, (0,0,100,25))
		self.objects['TestButton'] = TestButton
		self.events = []
		self.testvalue = 3
	def Frame(self) :
		self.clock.tick(30)
		self.events = pygame.event.get()
		for event in self.events :
			if hasattr(event, 'key') :
				if event.key == K_ESCAPE :
					sys.exit(0)
		for obj in self.objects.values() :
			obj.Frame()
	def OnStart(self) :
		self.nextScene = 'MapTest'
	def Render(self) :
		self.screen.fill((0,0,0))
		for obj in self.objects.values() :
			obj.Render()
		pygame.display.flip()