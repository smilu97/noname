import pygame, math, sys
from pygame.locals import *
from Scene import *
import random

class SceneDodge(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		# player
		player = GameObjectPlayer(self,[600.0,400.0],pygame.image.load('Data/character.bmp'),40.0,'player')
		player_showComponents = {'idle':player.components['image'],\
							'leftmove':GameComponentImage(player,pygame.image.load('Data/leftmove.bmp')),\
							'rightmove':GameComponentImage(player,pygame.image.load('Data/rightmove.bmp'))}
		player_collider = GameComponentCircleCollider(player, (20.0,20.0), 20.0)
		player_controller = GameComponentTopViewController(player, 1.0, 1.0, player_showComponents)
		player.components['showComponents'] = player_showComponents
		player.components['collider'] = player_collider
		player.components['controller'] = player_controller
		self.objects['player'] = player
		# bullets
		self.objects['bulletContainer'] = {}
	def MakeTestChaseBullet(self) :
		randomKey = random.random()
		bullet = GameObjectBullet(self,[600.0,300.0],pygame.image.load('Data/bullet.bmp'),\
				5, math.pi/2, key=randomKey, bulletShape=BulletShapeChasePlayer, speed=0.1)
		self.objects['bulletContainer'][randomKey] = bullet
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
					self.MakeTestChaseBullet()
		FrameAll(self.objects.values(), self.dt)
	def Render(self):
		self.screen.fill((0,0,0))
		RenderAll(self.objects.values())
		pygame.display.flip()