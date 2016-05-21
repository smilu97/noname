import pygame, math, sys
from pygame.locals import *
from Scene import *

MAPTEST_TERRRAIN_RECT = (0.0,0.0,1000.0,100.0)
PLAYER_SPAWNPOSITION = [10.0,10.0]

class SceneMapTest(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self,screen, clock, player)
		font = pygame.font.SysFont('comicsansms', 25)
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
		TestButton = GameObjectButton(self, font.render('Print Hello!', True, (255,255,255)), self.PrintHello, (0.0,0.0,100.0,30.0), \
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
		self.objects['player'] = GameObjectPlayer(self, list(PLAYER_SPAWNPOSITION), \
									pygame.image.load('Data/character.bmp'),\
									  size=40.0, name='player')
		self.objects['player'].components['hellotext'] = GameComponentImage(self.objects['player'], \
															font.render('Hello!', True, (255,255,255)), position=[0,-40])
		self.objects['player'].components['runanim'] = GameComponentAnimator(self.objects['player'], \
														'Data/CharAnim')
		self.objects['player'].components['controller'].showComponent = {'idle' : self.objects['player'].components['image'] ,\
															'run' : self.objects['player'].components['runanim']}
		self.objects['player'].components['image'].able = False
		self.objects['player'].components['collider'] = GameComponentBoxCollider(self.objects['player'], \
															(0.0,0.0,40.0,40.0))
		# bullet[]
		bulletContainer = {}
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
		# A_box
		BoxSurface = pygame.Surface((100,50))
		pygame.draw.rect(BoxSurface, (0,255,0), (0,0,100,50))
		A_box = GameObject(self, (200.0, 350.0), name='A_box')
		A_box_collider = GameComponentBoxCollider(A_box, (0.0,0.0,100.0,50.0))
		A_box_image = GameComponentImage(A_box, BoxSurface)
		A_box.components['collider'] = A_box_collider
		A_box.components['image'] = A_box_image
		self.objects['A_box'] = A_box
		# B_box
		B_box = GameObject(self, (300.0, 280.0), name='B_box')
		B_box_collider = GameComponentBoxCollider(B_box, (0.0,0.0,100.0,50.0))
		B_box_image = GameComponentImage(B_box, BoxSurface)
		B_box.components['collider'] = B_box_collider
		B_box.components['image'] = B_box_image
		self.objects['B_box'] = B_box
		# C_box
		C_box = GameObject(self, (400.0, 210.0), name='C_box')
		C_box_collider = GameComponentBoxCollider(C_box, (0.0,0.0,100.0,50.0))
		C_box_image = GameComponentImage(C_box, BoxSurface)
		C_box.components['collider'] = C_box_collider
		C_box.components['image'] = C_box_image
		self.objects['C_box'] = C_box
		# testSpeech
		testSpeech = GameObject(self, (0.0,30.0), name='testSpeech')
		testSpeech.static = True
		testSpeech_speech = GameComponentSpeech(testSpeech, [0.0,0.0], 'comicsansms', 30)
		testSpeech_speech.SetText(['This is speech testuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu',\
									'This is second speech testuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', \
									 'This is third speech testuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu',''])
		testSpeech.components['speech'] = testSpeech_speech
		self.objects['testSpeech'] = testSpeech
	def PrintHello(self) :
		print 'Hello!'
	def Frame(self):
		self.dt = self.clock.tick(60)
		self.events = pygame.event.get() 
		self.key_pressed = pygame.key.get_pressed()
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
		FrameAll(self.objects.values(), self.dt)
	def Render(self):
		self.screen.fill((0,0,0))
		RenderAll(self.objects.values())
		pygame.display.flip()
