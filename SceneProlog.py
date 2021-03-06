#-*- coding: utf-8 -*-

import pygame, math, sys
from pygame.locals import *
from Scene import *

class SceneProlog(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		self.font = pygame.font.Font('ttf/NanumGothic.ttf', 25)
		centerSpeech_obj = GameObject(self, (300,300), name='centerSpeech')
		centerSpeech_speech = GameComponentSpeech(centerSpeech_obj,[0,0],'comicsansms',30,(255,255,255))
		centerSpeech_speech.font = pygame.font.Font('ttf/NanumGothic.ttf', 25)
		centerSpeech_speech.SetText([u'공 대생(20)은 한양대학교 컴퓨터공학과 16학번 새내기이다.',
										u'치열한 입시 끝에 행복한 대학생활을 기대했지만',
										u'그것은 크나큰 착각이었다.',''])
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
			self.nextScene = 'WorldMap'
			self.player.pos[0] = 3445.0
			self.player.pos[1] = 3450.0
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
		self.screen.blit(self.font.render(u'Z키로 진행', True, (255,255,255)), (0,500))
		pygame.display.flip()


