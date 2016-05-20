import pygame, math, sys
from pygame.locals import *
from Scene import *		



class SceneMainMenu(Scene):
	"""docstring for MainMenu"""
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		font = pygame.font.SysFont('comicsansms', 25)
		TestButton = GameObjectButton(self, font.render('Start', True, (255,255,255)), self.OnStart, (400,400,500,430))
		self.objects['TestButton'] = TestButton
		self.events = []
		self.testvalue = 3
	def Frame(self) :
		self.dt = self.clock.tick(60)
		if not self.dumpTime :
			self.dumpTime = True
			self.dt = 0
		self.events = pygame.event.get()
		self.key_pressed = pygame.key.get_pressed()
		for event in self.events :
			if hasattr(event, 'key') :
				if event.key == K_ESCAPE :
					self.nextSceneState = NEXTSCENE_POP
				if event.key == K_RETURN :
					self.OnStart()
		for obj in self.objects.values() :
			obj.Frame(self.dt)
	def OnStart(self) :
		self.nextScene = 'MapTest'
	def Render(self) :
		self.screen.fill((0,0,0))
		for obj in self.objects.values() :
			obj.Render()
		pygame.display.flip()