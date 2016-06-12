import pygame, math, sys
from pygame.locals import *
from Scene import *		



class SceneMainMenu(Scene):
	"""docstring for MainMenu"""
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		font = pygame.font.Font('ttf/NanumGothic.ttf', 25)
		self.bg_img = pygame.image.load('Data/MainMenu.png')
	def Frame(self) :
		self.dt = self.clock.tick(60)
		if not self.dumpTime :
			self.dumpTime = True
			self.dt = 0
		self.events = pygame.event.get()
		self.key_pressed = pygame.key.get_pressed()
		if self.key_pressed[K_ESCAPE] :
			self.nextSceneState = NEXTSCENE_POP
		if self.key_pressed[K_RETURN] :
			self.OnStart()
		for event in self.events :
			if event.type == MOUSEBUTTONDOWN :
				if event.button == 1 :
					pos = event.pos
					if 50 < pos[0] and pos[0] < 300 and 500 < pos[1] and pos[1] < 750 :
						self.OnStart()
		for obj in self.objects.values() :
			obj.Frame(self.dt)
	def OnStart(self) :
		self.nextScene = 'Prolog'
	def Render(self) :
		self.screen.fill((0,0,0))
		self.screen.blit(self.bg_img, (0,0))
		RenderAll(self.objects.values())
		self.spriteGroup.draw(self.screen)
		pygame.display.flip()