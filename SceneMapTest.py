#-*- coding: utf-8 -*-
import pygame, math, sys
from pygame.locals import *
from Scene import *

MAPTEST_TERRRAIN_RECT = (0.0,0.0,1000.0,100.0)
PLAYER_SPAWNPOSITION = [10.0,10.0]

class SceneMapTest(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self,screen, clock, player)
		font = pygame.font.SysFont('nanumgothic', 25)
		#LeftWall
		LeftWall = GameObject(self, (-100.0,0.0,100.0,500.0), name='leftwall')
		LeftWall_BoxCollider = GameComponentBoxCollider(LeftWall, (0.0,0.0,100.0,500.0))
		LeftWall_Surface = pygame.Surface((100,500))
		pygame.draw.rect(LeftWall_Surface, (255,255,0), (0,0,100,500))
		LeftWall_Image = GameComponentImage(LeftWall, LeftWall_Surface, [0.0,0.0])
		LeftWall.components['collider'] = LeftWall_BoxCollider
		LeftWall.components['image'] = LeftWall_Image
		self.objects['leftwall'] = LeftWall
		#RightWall
		RightWall = GameObject(self, (900.0,0.0,100.0,500.0), name='rightwall')
		RightWall_BoxCollider = GameComponentBoxCollider(RightWall, (0.0,0.0,100.0,500.0))
		RightWall_Image = GameComponentImage(RightWall, LeftWall_Surface, [0.0,0.0])
		RightWall.components['collider'] = RightWall_BoxCollider
		RightWall.components['image'] = RightWall_Image
		self.objects['Rightwall'] = RightWall
		#TestButton
		PrintHelloText = font.render('Print Hello!', True, (255,255,255))
		PrintHelloText_rect = PrintHelloText.get_rect()
		TestButton = GameObjectButton(self, font.render('Print Hello!', True, (255,255,255)), self.PrintHello, PrintHelloText_rect, \
										'testbutton')
		TestButton.static = True 
		self.objects['testbutton'] = TestButton
		# terrain
		terrain = GameObject(self, (0.0,400.0), name='terrain')
		terrain_boxcollider = GameComponentBoxCollider(terrain, MAPTEST_TERRRAIN_RECT)
		terrain.components['collider'] = terrain_boxcollider
		terrain_surface = pygame.Surface((1000,100))
		pygame.draw.rect(terrain_surface, (255,255,0), (0,0,1000,100))
		terrain_image = GameComponentImage(terrain, terrain_surface)
		terrain.components['image'] = terrain_image
		self.objects['terrain'] = terrain
		# player
		self.playerObj = GameObjectPlayer(self, list(PLAYER_SPAWNPOSITION), pygame.image.load('Data/character.png'), 40.0, 'player')
		self.objects['player'] = self.playerObj
		self.playerObj.components['collider'] = GameComponentBoxCollider(self.playerObj, \
															(0.0,0.0,40.0,40.0))
		self.playerObj.components['hellotext'] = GameComponentImage(self.playerObj, \
															font.render('Hello!', True, (255,255,255)), position=[0,-40])
		self.playerObj.components['runanim'] = GameComponentAnimator(self.playerObj, \
														'Data/CharAnim')
		self.playerObj.components['controller'].showComponent = {'idle' : self.playerObj.components['image'] ,\
															'run' : self.playerObj.components['runanim']}
		self.playerObj.components['image'].able = False
		self.playerObj.components['controller'].ownCollider = \
			self.playerObj.components['collider']
		# bullet[]
		bulletContainer = []
		characterGunObject = GameObject(self,name='gun')
		characterGunComponent = GameComponentCharacterGun(characterGunObject,bulletContainer, \
									GameObjectBullet, pygame.image.load('Data/bullet.bmp'), \
										self.objects['player'], 5)
		characterGunObject.components['gunComponent'] = characterGunComponent
		self.objects['gun'] = characterGunObject
		self.objects['bulletContainer'] = bulletContainer
		# camera
		CameraController = GameObject(self)
		CameraController.components['CameraController'] = GameComponentCameraController(CameraController)
		self.objects['camera'] = CameraController
		# testSpeech
		testSpeech = GameObject(self, (0.0,30.0), name='testSpeech')
		testSpeech.static = True
		testSpeech_speech = GameComponentSpeech(testSpeech, [0.0,0.0], 'nanumgothic', 30)
		testSpeech_speech.SetText(['This is speech testuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu',\
									'This is second speech testuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', \
									 'This is third speech testuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu',
									 u'이것은 한글 테스트입니다.',''])
		testSpeech.components['speech'] = testSpeech_speech
		self.objects['testSpeech'] = testSpeech
		# portal
		chongPortal = GameObjectPortal(self, np.array(0,460), pygame.image.load("Data/portal.png"), self.playerObj.components['collider'], \
						"Chongjang");
	def PrintHello(self) :
		print 'Hello!'
	def Frame(self):
		self.dt = self.clock.tick(60)
		self.events = pygame.event.get() 
		self.key_pressed = pygame.key.get_pressed()
		self.statInConsole()
		if not self.dumpTime :
			self.dt = 0
			self.dumpTime = True
		for event in self.events : 
			if hasattr(event, 'key') and event.type == KEYDOWN :
				if event.key == K_ESCAPE :
					self.nextSceneState = NEXTSCENE_POP
				elif event.key == K_f :
					self.nextScene = 'Tetris'
					self.nextSceneState = NEXTSCENE_STACK
				elif event.key == K_x :
					self.objects['player'].position = [0.0,30.0]
					self.objects['player'].components['controller'].vy = 0
				elif event.key == K_g :
					self.nextScene = 'Dodge'
					self.nextSceneState = NEXTSCENE_STACK
				elif event.key == K_y :
					self.nextScene = 'MineFinder'
					self.nextSceneState = NEXTSCENE_STACK
				elif event.key == K_t :
					self.nextScene = 'Avoider'
					self.nextSceneState = NEXTSCENE_STACK
				elif event.key == K_r :
					self.nextScene = 'Rhythm'
					self.nextSceneState = NEXTSCENE_STACK
		FrameAll(self.objects.values(), self.dt)
		self.spriteGroup.update()
