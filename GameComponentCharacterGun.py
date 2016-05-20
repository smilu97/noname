import pygame, math, sys
from pygame.locals import *
from GameComponent import *

class GameComponentCharacterGun(GameComponent):
	def __init__(self, owner, bulletContainer, bulletClass, bulletImage, size):
		GameComponent.__init__(self,owner)
		self.bulletContainer = bulletContainer
		self.bulletClass = bulletClass
		self.bulletImage = bulletImage
		self.size = size
	def Frame(self, dt):
		for event in self.owner.owner.events :
			if hasattr(event, 'key') :
				if event.type == KEYDOWN :
					if event.key == K_q :
						self.MakeBullet()
	def MakeBullet(self) :
		bullet = self.bulletClass(self.owner.owner, list(self.baseObject.position), self.bulletImage, \
					self.size)
		bullet.index = len(bulletContainer)
		bulletContainer.append(bullet)
