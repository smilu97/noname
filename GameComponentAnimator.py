import pygame, math, sys
from pygame.locals import *
from GameComponent import *

class GameComponentAnimator(GameComponent, pygame.sprite.Sprite):
	def __init__(self, owner, imagePath = '', able=True):
		GameComponent.__init__(self, owner)
		pygame.sprite.Sprite.__init__(self)
		self.able = able
		self.images = []
		self.imageNum = 0
		self.interval = 0
		self.nowIndex = 0
		self.dtcounter = 0
		self.rect = pygame.Rect(0,0,0,0)
		if imagePath != '' :
			self.Load(imagePath)
	def Load(self, path) :
		ifile = open(path + '/dat.txt', 'r')
		rawstring = ifile.read()
		ifile.close()
		rawstring = rawstring.split('\n')
		self.imageNum = int(rawstring[0])
		self.interval = int(rawstring[1])
		for i in range(self.imageNum) :
			self.images.append(pygame.image.load(path + '/' + '0'*(3-len(str(i))) + str(i) + '.bmp'))
		self.rect = self.images[0].get_rect()
		self.owner.owner.spriteGroup.add(self)
		self.image = self.images[self.nowIndex]
		self.blank = pygame.Surface((0,0))
	def Frame(self,dt):
		if self.able :
			self.dtcounter += dt
	def Render(self):
		if self.able :
			self.image = self.images[self.nowIndex]
			if self.dtcounter > self.interval :
				self.nowIndex += 1
				if self.nowIndex >= self.imageNum :
					self.nowIndex = 0
				self.dtcounter -= self.interval
			if self.owner.static :
				self.rect.x = self.position[0]
				self.recr.y = self.position[1]
			else :
				cam = self.owner.owner.cam
				self.rect.x = self.position[0] + self.owner.position[0] - cam[0]
				self.rect.y = self.position[1] + self.owner.position[1] - cam[1]
		else :
			self.image = self.blank