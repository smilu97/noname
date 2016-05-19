import pygame, math, sys
from pygame.locals import *
from Scene import *

MAPTEST_TERRRAIN_RECT = (0.0,0.0,1000.0,100.0)
PLAYER_SPAWNPOSITION = [10.0,10.0]

class SceneMapTest(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self,screen, clock, player)
		font = pygame.font.SysFont('comicsansms', 25)
		#TestButton
		TestButton = GameObjectButton(self, font.render('Print Hello!', True, (255,255,255)), self.PrintHello, (0.0,0.0,100.0,30.0), \
										'testbutton')
		TestButton.static = True
		self.objects['testbutton'] = TestButton
		# Test
		# terrain
		terrain = GameObject(self, (0.0,400.0), name='terrain')
		terrain_boxcollider = GameComponentBoxCollider(terrain, MAPTEST_TERRRAIN_RECT)
		terrain.components['collider'] = terrain_boxcollider
		terrain_image = GameComponentImage(terrain, pygame.image.load('Data/testmapTerrain.bmp'))
		terrain.components['image'] = terrain_image
		self.objects['terrain'] = terrain
		# player
		self.objects['player'] = GameObjectPlayer(self, list(PLAYER_SPAWNPOSITION), \
									pygame.image.load('Data/character.bmp'), name='player')
		self.objects['player'].components['hellotext'] = GameComponentImage(self.objects['player'], \
															font.render('Hello!', True, (255,255,255)), position=[0,-40])
		self.objects['player'].components['runanim'] = GameComponentAnimator(self.objects['player'], \
														'Data/CharAnim')
		self.objects['player'].components['controller'].showComponent = {'idle' : self.objects['player'].components['image'] ,\
															'run' : self.objects['player'].components['runanim']}
		self.objects['player'].components['image'].able = False
		# camera
		CameraController = GameObject(self)
		CameraController.components['CameraController'] = GameComponentCameraController(CameraController)
		self.objects['camera'] = CameraController
		# A_box
		A_box = GameObject(self, (200.0, 350.0), name='A_box')
		A_box_collider = GameComponentBoxCollider(A_box, (0.0,0.0,100.0,50.0))
		A_box_image = GameComponentImage(A_box, pygame.image.load('Data/ABOXimage.bmp'))
		A_box.components['collider'] = A_box_collider
		A_box.components['image'] = A_box_image
		self.objects['A_box'] = A_box
		# testSpeech
		testSpeech = GameObject(self, (0.0,30.0), name='testSpeech')
		testSpeech.static = True
		testSpeech_speech = GameComponentSpeech(testSpeech, [0.0,0.0], 'comicsansms', 30)
		testSpeech_speech.SetText(['This is speech testuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu',\
									'This is second speech testuuuuuuuuuuuuuuuuuuuuuu', \
									 'This is third speech testuuuuuuuuuuuuuuuuu',''])
		testSpeech.components['speech'] = testSpeech_speech
		self.objects['testSpeech'] = testSpeech
	def PrintHello(self) :
		print 'Hello!'
	def Frame(self):
		self.dt = self.clock.tick(60) 
		self.events = pygame.event.get()
		self.key_pressed = pygame.key.get_pressed()
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
		for obj in self.objects.values() :
			obj.Frame(self.dt)
	def Render(self):
		self.screen.fill((0,0,0))
		for obj in self.objects.values() :
			obj.Render()
		pygame.display.flip()
