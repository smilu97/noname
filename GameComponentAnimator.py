import pygame, math, sys
from pygame.locals import *
from GameComponent import *

class GameComponentAnimator(GameComponent):
	def __init__(self, owner, imagePath = '', able=True):
		GameComponent.__init__(self, owner)
		self.able = able
		self.images = []
		self.imageNum = 0
		self.interval = 0
		self.nowIndex = 0
		self.dtcounter = 0
		if imagePath != '' :
			self.Load(imagePath)
	def Load(self, path) :
		ifile = open(imagePath, 'r')
		rawstring = ifile.read()
		ifile.close()
		rawstring = rawstring.split('\n')
		self.imageNum = int(rawstring[0])
		self.interval = int(rawstring[1])
		for i in range(self.imageNum) :
			images.append(pygame.image.load('0'*(3-len(str(i))) + str(i) + '.bmp'))
	def SetOff(self) :
		self.able = False
		self.nowIndex = 0
	def SetOn(self) :
		sefl.able = True
	def Frame(self,dt):
		if self.able :
			self.dtcounter += dt
			if self.dtcounter > self.interval :
				self.nowIndex += 1
				if self.nowIndex >= imageNum :
					self.nowIndex = 0
				self.dtcounter -= self.interval
	def Render(self):
		if self.able :
			screen = self.owner.owner.screen
			cam = self.owner.owner.cam
			printPos = (self.position[0] + self.owner.position[0] - cam[0], \
						self.position[1] + self.owner.position[1] - cam[1])
			screen.blit(self.images[self.nowIndex], printPos)
