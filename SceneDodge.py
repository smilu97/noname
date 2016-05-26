import pygame, math, sys
from pygame.locals import *
from Scene import *
import random

class SceneDodge(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		# player
		player = GameObjectPlayer(self,[600.0,400.0],pygame.image.load('Data/character.bmp'), 40.0,'player')
		player_showComponents = {'idle':player.components['image'],\
							'leftmove':GameComponentImage(player,pygame.image.load('Data/leftmove.bmp')),\
							'rightmove':GameComponentImage(player,pygame.image.load('Data/rightmove.bmp'))}
		player_collider = GameComponentCircleCollider(player, (20.0,20.0), 20.0)
		player_controller = GameComponentTopViewController(player, 0.3, 0.3, player_showComponents)
		player.components['showComponents'] = player_showComponents
		player.components['collider'] = player_collider
		player.components['controller'] = player_controller
		self.objects['player'] = player
		# bullets
		self.objects['bulletContainer'] = []
		# bulletScenario
		bulletMakerSet = (self.MakeSinBullet, self.MakeStraightBullet, \
			self.MakeChasePlayerBullet)
		bs_obj = GameObject(self)
		bs_comp = GameComponentBulletScenario(bs_obj, 'Data/BulletScenario/output.txt', \
			bulletMakerSet)
		bs_obj.components['scenario'] = bs_comp
		self.objects['scenario']  = bs_obj
		# Console
		console = GameObjectText(self, [0.0,0.0], 'comicsansms', 15)
		self.objects['console'] = console
	def MakeSinBullet(self, x, y, direction) :
		bullet = GameObjectBullet(self,[x,y],pygame.image.load('Data/bullet.bmp'),\
				5, direction, bulletShape=BulletShapeSin, speed=0.1)
	def MakeStraightBullet(self, x, y, direction) :
		bullet = GameObjectBullet(self,[x,y],pygame.image.load('Data/bullet.bmp'),\
				5, direction, bulletShape=BulletShapeStraight, speed=0.1)
	def MakeChasePlayerBullet(self, x, y, direction) :
		bullet = GameObjectBullet(self,[x,y],pygame.image.load('Data/bullet.bmp'),\
				5, direction, bulletShape=BulletShapeChasePlayer, speed=0.1)
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
				if event.key == K_r :
					self.MakeSinBullet(600,300,math.pi/2)
				if event.key == K_t :
					self.MakeChasePlayerBullet(600,300,math.pi/2)
				if event.key == K_y :
					self.MakeStraightBullet(600,300,math.pi/2)
				
		FrameAll(self.objects.values(), self.dt)