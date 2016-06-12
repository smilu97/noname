import pygame, math, sys

from pygame.locals import *
from Scene import *
import random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BOX_WIDTH = 400
BOX_HEIGHT = 400
WALL_THICKNESS = 100

class SceneDodge(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		# player
		player = GameObjectPlayer(self,[600.0,400.0],pygame.image.load('Data/character.png'), 40.0,'player')
		player_showComponents = {'idle':player.components['image'],\
							'leftmove':GameComponentImage(player,pygame.image.load('Data/leftmove.png')),\
							'rightmove':GameComponentImage(player,pygame.image.load('Data/rightmove.png'))}
		player_collider = GameComponentCircleCollider(player, (20.0,20.0), 20.0)
		player_controller = GameComponentTopViewController(player, 0.3, 0.3, player_showComponents)
		player.components['showComponents'] = player_showComponents
		player.components['collider'] = player_collider
		player.components['controller'] = player_controller
		self.objects['player'] = player
		# bullets
		self.objects['bulletContainer'] = []
		self.bContainer = self.objects['bulletContainer']
		# bulletScenario
		bulletMakerSet = (self.MakeSinBullet, self.MakeStraightBullet, \
			self.MakeChasePlayerBullet)
		bs_obj = GameObject(self)
		bs_comp = GameComponentBulletScenario(bs_obj, 'Data/BulletScenario/output.txt', \
			bulletMakerSet)
		bs_obj.components['scenario'] = bs_comp
		self.objects['scenario']  = bs_obj
		#LeftWall
		LeftWall = GameObject(self, (SCREEN_WIDTH/2 - BOX_WIDTH/2 - WALL_THICKNESS, \
			SCREEN_HEIGHT/2 - BOX_HEIGHT/2 - WALL_THICKNESS), name='leftwall')
		LeftWall_BoxCollider = GameComponentBoxCollider(LeftWall, (0.0,0.0,WALL_THICKNESS,BOX_HEIGHT + 2*WALL_THICKNESS))
		LeftWall_Surface = pygame.Surface((100,500))
		pygame.draw.rect(LeftWall_Surface, (255,255,0), (0,0,100,500))
		LeftWall_Image = GameComponentImage(LeftWall, LeftWall_Surface, [0.0,0.0])
		LeftWall.components['collider'] = LeftWall_BoxCollider
		LeftWall.components['image'] = LeftWall_Image
		self.objects['leftwall'] = LeftWall
		#RightWall
		RightWall = GameObject(self, (SCREEN_WIDTH/2 + BOX_WIDTH/2, \
			SCREEN_HEIGHT/2 - BOX_HEIGHT/2 - WALL_THICKNESS), name='rightwall')
		RightWall_BoxCollider = GameComponentBoxCollider(RightWall, (0.0,0.0,WALL_THICKNESS,BOX_HEIGHT + 2*WALL_THICKNESS))
		RightWall_Surface = pygame.Surface((100,500))
		pygame.draw.rect(RightWall_Surface, (255,255,0), (0,0,100,500))
		RightWall_Image = GameComponentImage(RightWall, RightWall_Surface, [0.0,0.0])
		RightWall.components['collider'] = RightWall_BoxCollider
		RightWall.components['image'] = RightWall_Image
		self.objects['rightwall'] = RightWall
		#DownWall
		DownWall = GameObject(self, (SCREEN_WIDTH/2 - BOX_WIDTH/2 - WALL_THICKNESS, \
			SCREEN_HEIGHT/2 + BOX_HEIGHT/2), name='downwall')
		DownWall_BoxCollider = GameComponentBoxCollider(DownWall, (0.0,0.0,BOX_WIDTH + 2*WALL_THICKNESS, WALL_THICKNESS))
		DownWall_Surface = pygame.Surface((600,100))
		pygame.draw.rect(DownWall_Surface, (255,255,0), (0,0,600,100))
		DownWall_Image = GameComponentImage(DownWall, DownWall_Surface, [0.0,0.0])
		DownWall.components['collider'] = DownWall_BoxCollider
		DownWall.components['image'] = DownWall_Image
		self.objects['downwall'] = DownWall
		#UpWall
		UpWall = GameObject(self, (SCREEN_WIDTH/2 - BOX_WIDTH/2 - WALL_THICKNESS, \
			SCREEN_HEIGHT/2 - BOX_HEIGHT/2 - WALL_THICKNESS), name='upwall')
		UpWall_BoxCollider = GameComponentBoxCollider(UpWall, (0.0,0.0,BOX_WIDTH + 2*WALL_THICKNESS, WALL_THICKNESS))
		UpWall_Surface = pygame.Surface((500,100))
		pygame.draw.rect(UpWall_Surface, (255,255,0), (0,0,500,100))
		UpWall_Image = GameComponentImage(UpWall, UpWall_Surface, [0.0,0.0])
		UpWall.components['collider'] = UpWall_BoxCollider
		UpWall.components['image'] = UpWall_Image
		self.objects['upwall'] = UpWall

		self.timer = 0
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
		if self.player.hp > 7 :
			self.nextScene = 'Dodge'
		if self.timer < 2000 :
			self.timer += self.dt
		else :
			if len(self.bContainer) == 0 :
				self.nextScene = 'WorldMap'
				self.player.story = 4
				self.player.pos[0] = 2200
				self.player.pos[1] = 1867
		bContainer = self.objects['bulletContainer']
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
		if self.key_pressed[K_p] :
			self.nextScene = 'WorldMap'
			self.player.story = 4
			self.player.pos[0] = 2200
			self.player.pos[1] = 1867
		FrameAll(self.objects.values(), self.dt)