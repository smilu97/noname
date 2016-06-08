#-*- coding: utf-8 -*-

import pygame, math, sys
from pygame.locals import *
from Scene import *

class SceneProlog(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		centerSpeech_obj = GameObject(self, (300,300), name='centerSpeech')
		centerSpeech_speech = GameComponentSpeech(centerSpeech_obj,[0,0],'comicsansms',30)
		centerSpeech_speech.font = pygame.font.Font('ttf/NanumGothic.ttf', 25)
		centerSpeech_speech.SetText([u'나는 한양대에 왔따!!!!!', \
										u'그래서 학교에 가야 한다!!!!!',\
										u'학교에!!',
										u'가!',
										u'자!!!!!!',
										u'!!!!!!!!!!!!!!!!!!!!!!!!!!!!',''])
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
			self.nextScene = 'MapTest'
		if not self.dumpTime :
			self.dt = 0
			self.dumpTime = True
		for event in self.events : 
			if hasattr(event, 'key') and event.type == KEYDOWN :
				if event.key == K_ESCAPE :
					self.nextSceneState = NEXTSCENE_POP
		FrameAll(self.objects.values(), self.dt)
		self.spriteGroup.update()


