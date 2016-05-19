import pygame, math, sys
from pygame.locals import *
from Scene import *

MAPTEST_TERRRAIN_RECT = (0.0,0.0,1000.0,100.0)
PLAYER_SPAWNPOSITION = [10.0,10.0]

class SceneMapTest(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self,screen, clock, player)
		font = pygame.font.SysFont('comicsansms', 25)
		self.objects['HelloText'] = GameObject(self,name='HelloText')
		text = GameComponentImage(self.objects['HelloText'], font.render('Test', True, (255,255,255)))
		self.objects['HelloText'].components['image'] = text
		terrain = GameObject(self, (0.0,400.0), name='terrain')
		terrain_boxcollider = GameComponentBoxCollider(terrain, MAPTEST_TERRRAIN_RECT)
		terrain.components['collider'] = terrain_boxcollider
		terrain_image = GameComponentImage(terrain, pygame.image.load('Data/testmapTerrain.bmp'))
		terrain.components['image'] = terrain_image
		self.objects['terrain'] = terrain
		self.objects['player'] = GameObjectPlayer(self, list(PLAYER_SPAWNPOSITION), \
									pygame.image.load('Data/character.bmp'),name='player')
		self.objects['player'].components['hellotext'] = GameComponentImage(self.objects['player'], \
															font.render('Hello!', True, (255,255,255)), position=[0,-40])
		CameraController = GameObject(self)
		CameraController.components['CameraController'] = GameComponentCameraController(CameraController)
		self.objects['camera'] = CameraController
	def Frame(self):
		self.dt = self.clock.tick(60) 
		self.events = pygame.event.get()
		self.key_pressed = pygame.key.get_pressed()
		for event in self.events : 
			if hasattr(event, 'key') :
				if event.key == K_ESCAPE and event.type == KEYDOWN :
					self.nextSceneState = NEXTSCENE_POP
				elif event.key == K_f :
					self.nextScene = 'Tetris'
					self.nextSceneState = NEXTSCENE_STACK
		for obj in self.objects.values() :
			obj.Frame(self.dt)
	def Render(self):
		self.screen.fill((0,0,0))
		for obj in self.objects.values() :
			obj.Render()
		pygame.display.flip()
