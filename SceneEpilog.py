#-*- coding: utf-8 -*-

import pygame, math, sys
from pygame.locals import *
from Scene import *

class SceneEpilog(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		self.font = pygame.font.Font('ttf/NanumGothic.ttf', 25)
		centerSpeech_obj = GameObject(self, (300,300), name='centerSpeech')
		centerSpeech_speech = GameComponentSpeech(centerSpeech_obj,[0,0],'comicsansms',30,(255,255,255))
		centerSpeech_speech.font = pygame.font.Font('ttf/NanumGothic.ttf', 25)
		centerSpeech_speech.SetText([u"석양이 진다...",
										u"대생이의 재미있는 하루는 그렇게 가고 있었다",
										u"그러나 그는 잊고 있다",
										u"기말고사가 코 앞이라는 것을",
										u"그의 학점 또한 지고 있었다는 것을"])
		centerSpeech_obj.components['speech'] = centerSpeech_speech
		self.objects['centerspeech'] = centerSpeech_obj
		self.spch = centerSpeech_speech
		self.timeCounter = 0
	def Frame(self):
		self.dt = self.clock.tick(60)
		if self.timeCounter != 0 :
			self.timeCounter += self.dt
		self.events = pygame.event.get() 
		self.key_pressed = pygame.key.get_pressed()
		if self.spch.level == len(self.spch.text)-1 :
			if self.timeCounter == 0 : self.timeCounter = 1
		if self.timeCounter > 1000 :
			self.nextSceneState = NEXTSCENE_POP
			return
		if not self.dumpTime :
			self.dt = 0
			self.dumpTime = True
		if self.key_pressed[K_ESCAPE] :
			self.nextSceneState = NEXTSCENE_POP
		for event in self.events : 
			if hasattr(event, 'key') and event.type == KEYDOWN :
				pass
		FrameAll(self.objects.values(), self.dt)
		self.spriteGroup.update()
	def Render(self) :
		self.screen.fill((0,0,0))
		RenderAll(self.objects.values())
		self.spriteGroup.draw(self.screen)
		pygame.display.flip()


