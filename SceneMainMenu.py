import pygame, math, sys
from pygame.locals import *
from Scene import *		

class SceneMainMenu(Scene):
	"""docstring for MainMenu"""
	def __init__(self, screen, clock):
		Scene.__init__(self, screen, clock)
		font = pygame.font.SysFont('comicsansms', 25)
		TestButton = GameObjectButton(self, font.render('Test', True, (255,255,255)), self.PrintTest, (0,0,300,25))
		self.objects.append(TestButton)
		self.events = []
	def Frame(self) :
		self.clock.tick(30)
		self.events = pygame.event.get()
		for event in self.events :
			if hasattr(event, 'key') :
				if event.key == K_ESCAPE :
					sys.exit(0)
		for obj in self.objects :
			obj.Frame()
	def PrintTest(self) :
		print 'test'
	def Render(self) :
		self.screen.fill((0,0,0))
		for obj in self.objects :
			obj.Render()
		pygame.display.flip()