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

RECT_JAGWADAE = [1236, 1438, 2110, 2135]
RECT_GONGHAK1 = [3493, 1751, 4102, 2026]
RECT_ITBT = [4365, 387, 5307, 768]
RECT_GROUND = [4625, 1522, 5291, 2044]
RECT_SUBWAY = [3211, 3040, 3679, 3428]

class SceneWorldMap(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		self.consoleFont = pygame.font.Font('ttf/NanumGothic.ttf', 25)
		#background
		self.bg_img = pygame.image.load('Data/WorldMapBackground.png')
		# player
		playerObj = GameObjectPlayer(self,self.player.pos,pygame.image.load('Data/character.png'), 40.0,'player')
		player_showComponents = {'idle':playerObj.components['image'],\
							'leftmove':playerObj.components['image'],\
							'rightmove':playerObj.components['image']}
		player_collider = GameComponentCircleCollider(playerObj, (20.0,20.0), 20.0)
		player_controller = GameComponentTopViewController(playerObj, 0.3, 0.3, player_showComponents)
		playerObj.components['showComponents'] = player_showComponents
		playerObj.components['collider'] = player_collider
		playerObj.components['controller'] = player_controller
		self.objects['player'] = playerObj
		self.playerObj = playerObj
		self.playerCont = player_controller
		self.playerColl = player_collider
		# camera
		CameraController = GameObject(self)
		CameraController.components['CameraController'] = GameComponentCameraController(CameraController, playerObj)
		self.objects['camera'] = CameraController
		# bullets
		self.objects['bulletContainer'] = []
		# Speech
		Speech = GameObject(self, (0.0,30.0), name='Speech')
		Speech.static = True
		Speech_speech = GameComponentSpeech(Speech, [0.0,0.0], 'nanumgothic', 30, (0,255,255))
		Speech_speech.font = pygame.font.Font('ttf/NanumGothic.ttf', 25)
		if self.player.story == 0 :
			Speech_speech.SetText([u'상쾌한 아침이야!',\
										u'과제때문에 비록 2시간 밖에 못 잤지만',\
										u'하하하 1교시가 미적이었던가?',\
										u'5분밖에 안남았으니까 빨리 가야겠다!'])
		elif self.player.story == 2 :
			Speech_speech.SetText([u"그래도 공부 안한 것 치고 선빵한 것 같아...",
										u"다음 교시는 물리실험인가?",
										u"내가 미쳤지 밥 먹을 시간도 없이 시간표를 짜다니",
										u"ㅂㄷㅂㄷ.. 자과대로 가자"])
		elif self.player.story == 4 :
			Speech_speech.SetText([u"헉헉... 죽다 살았네",
									u"다음은 소입설인가",
									u"ITBT로 가자"])
		elif self.player.story == 6 :
			Speech_speech.SetText([u"내가 해냈다",
									u"아무 것도 하기 싫다",
									u"이미 아무 것도 하지 않지만",
									u"더 적극적으로 아무 것도 하지 않기 위해서",
									u"집에 가자"])
		else :
			Speech_speech.SetText(['Error'])
		Speech.components['speech'] = Speech_speech
		self.objects['Speech'] = Speech
		self.speech = Speech_speech
	def Frame(self):
		self.dt = self.clock.tick(60)
		self.events = pygame.event.get() 
		self.key_pressed = pygame.key.get_pressed()
		bContainer = self.objects['bulletContainer']
		for img in self.spriteGroup :
			if hasattr(img.owner, 'key') :
				if not img.owner in bContainer :
					img.kill()
		if not self.dumpTime :
			self.dt = 0
			self.dumpTime = True
		if self.key_pressed[K_ESCAPE] :
			self.nextSceneState = NEXTSCENE_POP
		for event in self.events : 
			if hasattr(event, 'key') and event.type == KEYDOWN :
				pass
		if self.player.story in (0,2,4,6) :
			self.playerCont.able = False
			if self.speech.isLast() :
				self.player.story += 1
		elif self.player.story == 1 :
			self.playerCont.able = True
			if self.playerColl.GetIsCollidingWithRawCircle(((RECT_GONGHAK1[2]+RECT_GONGHAK1[0])/2,\
									 (RECT_GONGHAK1[1]+RECT_GONGHAK1[3])/2),(RECT_GONGHAK1[2]-RECT_GONGHAK1[0])/2) :
				self.nextScene = 'ClassRoom'
		elif self.player.story == 3 :
			self.playerCont.able = True
			if self.playerColl.GetIsCollidingWithRawCircle(((RECT_JAGWADAE[2]+RECT_JAGWADAE[0])/2,\
									 (RECT_JAGWADAE[1]+RECT_JAGWADAE[3])/2),(RECT_JAGWADAE[2]-RECT_JAGWADAE[0])/2) :
				self.nextScene = 'ClassRoom'
		elif self.player.story == 5 :
			self.playerCont.able = True
			if self.playerColl.GetIsCollidingWithRawCircle(((RECT_ITBT[2]+RECT_ITBT[0])/2,\
									 (RECT_ITBT[1]+RECT_ITBT[3])/2),(RECT_ITBT[2]-RECT_ITBT[0])/2) :
				self.nextScene = 'ClassRoom'
		elif self.player.story == 7 :
			self.playerCont.able = True
			if self.playerColl.GetIsCollidingWithRawCircle(((RECT_SUBWAY[2]+RECT_SUBWAY[0])/2,\
									 (RECT_SUBWAY[1]+RECT_SUBWAY[3])/2),(RECT_SUBWAY[2]-RECT_SUBWAY[0])/2) :
				self.nextScene = 'Epilog'
		FrameAll(self.objects.values(), self.dt)
	def Render(self) :
		self.screen.fill((0,0,0))
		self.screen.blit(self.bg_img, -self.cam)
		RenderAll(self.objects.values())
		self.spriteGroup.draw(self.screen)
		self.screen.blit(self.consoleFont.render('X:%d Y:%d' % (self.playerObj.position[0], self.playerObj.position[1]), True, (0,0,0)), (0,0))
		pygame.display.flip()