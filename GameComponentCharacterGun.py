import pygame, math, sys, random
from pygame.locals import *
from GameComponent import *

class GameComponentCharacterGun(GameComponent):
	def __init__(self, owner, bulletContainer, bulletClass, bulletImage, baseObject, size):
		GameComponent.__init__(self,owner)
		self.bulletContainer = bulletContainer
		self.bulletClass = bulletClass
		self.bulletImage = bulletImage
		self.size = size
		self.baseObject = baseObject
	def Frame(self, dt):
		for event in self.owner.owner.events :
			if hasattr(event, 'key') :
				if event.type == KEYDOWN :
					if event.key == K_q :
						self.MakeBullet()
	def MakeBullet(self) :
		if self.owner.owner.objects['player'].horizontalDirection == 1 :
			bullet_angle = 0
		else :
			bullet_angle = math.pi
		bullet = self.bulletClass(self.owner.owner, \
					list([self.baseObject.position[0], self.baseObject.position[1] - 10]),\
					 self.bulletImage, self.size, bullet_angle)
