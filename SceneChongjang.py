import pygame, math, sys
from pygame.locals import *
from Scene import *
import random

class SceneChongjang(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player);
		self.animTimer = 0
		# player
		self.playerObj = GameObjectPlayer(self, list(PLAYER_SPAWNPOSITION), \
									pygame.image.load('Data/character.png'),\
									  size=40.0, name='player')
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
		RightWall = GameObject(self, (1900.0,0.0,100.0,500.0), name='rightwall')
		RightWall_BoxCollider = GameComponentBoxCollider(RightWall, (0.0,0.0,100.0,500.0))
		RightWall_Image = GameComponentImage(RightWall, LeftWall_Surface, [0.0,0.0])
		RightWall.components['collider'] = RightWall_BoxCollider
		RightWall.components['image'] = RightWall_Image
		self.objects['Rightwall'] = RightWall
		# terrain
		terrain = GameObject(self, (0.0,400.0), name='terrain')
		terrain_boxcollider = GameComponentBoxCollider(terrain, MAPTEST_TERRRAIN_RECT)
		terrain.components['collider'] = terrain_boxcollider
		terrain_surface = pygame.Surface((1000,100))
		pygame.draw.rect(terrain_surface, (255,255,0), (0,0,2000,100))
		terrain_image = GameComponentImage(terrain, terrain_surface)
		terrain.components['image'] = terrain_image
		self.objects['terrain'] = terrain
		
	def Frame(self) :
		self.dt = self.clock.tick(60)
		self.events = pygame.event.get() 
		self.key_pressed = pygame.key.get_pressed()
		self.animTimer += self.dt
