#-*- coding: utf-8 -*-

import pygame, math, sys

from pygame.locals import *
from Scene import *
import random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BOX_WIDTH = 400
BOX_HEIGHT = 400
WALL_THICKNESS = 100

class SceneClassRoom(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		self.bg_img = pygame.image.load('Data/ClassRoom.png')
		# bullets
		self.objects['bulletContainer'] = []
		# Speech
		Speech = GameObject(self, (30.0,30.0), name='Speech')
		Speech.static = True
		Speech_speech = GameComponentSpeech(Speech, [0.0,0.0], 'NanumGothic', 30, (0,0,0))
		Speech_speech.font = pygame.font.Font('ttf/NanumGothic.ttf', 40)
		if self.player.story == 1 :
			Speech_speech.SetText([u"교수님 : 에... astronomica shibringdkaskdhlakhsjdgkahkjsd",
									u"교수님 : asdfabadookjokachidooneasdjfhlkajhskjdhfkjahksj",
									u"교수님 : 한 함수에 대해 배워봤어요",
									u"교수님 : 참 쉽죠?",
									u"학생들 : 네!",
									u"대생 : 뭐지? 나만 못 알아들은 건가",
									u"교수님 : 오늘은 퀴즈를 보겠습니다 낄낄낄",
									u"교수님 : 만약 틀리면 다 맞을 때 까지 다시 보겠습니다",
									u"대생 : 젠장 그동안 수업을 안 들었더니 sinhx가 뭔지도 모르겠네",
									u"대생 : 이렇게 된 이상 모든 문제를 찍어야겠다"])
		elif self.player.story == 3 :
			Speech_speech.SetText([u"물리조교님 : 이번 실험은 탄동진자 실험입니다.",
									u"물리조교님 : 평소엔 쇠구슬로 하지만...",
									u"물리조교님 : 오늘은 진짜 총알로 합시다",
									u"대생이 : 그러면 너무 위험하지 않을까요?",
									u"물리조교님 : 닥쳐! 컴공은 까라면 까야지!",
									u"대생이 : ...",
									u"물리조교님 : 어 실수로 발사함"])
		elif self.player.story == 5 :
			Speech_speech.SetText([u"신용기 조교님 : 오늘은 특별히 과제를 4개 내주도록 하겠어요",
									u"이상정 조교님 : 과제는 여러분의 피와 살이 되니 모두",
									u"이상정 조교님 : 행복",
									u"이상정 조교님 : 한 마음으로 합시다",
									u"이상정 조교님 : 참고로 내일 까지",
									u"대생이 : 이건 미쳤어",
									u"대생이 : 3개 연강에 과제까지 있다니!!",
									u"대생이 : ...",
									u"대생이 : 출튀해야지"])
		else :
			Speech_speech.SetText(['Error'])
		Speech.components['speech'] = Speech_speech
		self.objects['Speech'] = Speech
		self.speech = Speech_speech
		self.timer = 0
	def Frame(self):
		self.dt = self.clock.tick(60)
		self.events = pygame.event.get() 
		self.key_pressed = pygame.key.get_pressed()
		if self.speech.isLast() :
			self.timer += self.dt
			if self.timer > 1300 :
				if self.player.story == 1 :
					self.nextScene = 'MineFinder'
				elif self.player.story == 3 :
					self.nextScene = 'Dodge'
				elif self.player.story == 5 :
					self.nextScene = 'Avoider'
		for img in self.spriteGroup :
			if hasattr(img.owner, 'key') :
				if not img.owner in bContainer :
					img.kill()
		if not self.dumpTime :
			self.dt = 0
			self.dumpTime = True
		for event in self.events : 
			if hasattr(event, 'key') and event.type == KEYDOWN :
				if event.key == K_ESCAPE :
					self.nextSceneState = NEXTSCENE_POP
				
		FrameAll(self.objects.values(), self.dt)
	def Render(self) :
		self.screen.fill((0,0,0))
		self.screen.blit(self.bg_img, (0,0))
		RenderAll(self.objects.values())
		self.spriteGroup.draw(self.screen)
		pygame.display.flip()