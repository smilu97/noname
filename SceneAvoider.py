import pygame, math, sys
from pygame.locals import *
from Scene import *


class SceneAvoider(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		self.obList = []
		self.Load('Data/Avoid/Scenario/Test.txt')
		self.obY = []
		self.px = 0
		self.py = 700
		self.speed = 0.5
		self.timeCounter = 0
		self.charImage = pygame.image.load('Data/Avoid/Character.png')
		self.obImage = pygame.image.load('Data/Avoid/Obstacle.png')
		self.obSize = 100
		self.charSize = 100
		self.charImage = pygame.transform.scale(self.charImage, (self.charSize, self.charSize))
		self.obImage = pygame.transform.scale(self.obImage, (self.obSize, self.obSize))
	def Load(self, path) :
		ifile = open(path, 'r')
		self.obList = list()
		for dat in [[int(i) for i in line.split(' ')] for line in ifile.read().split('\n')[:-1]] : self.obList.append(dat)
		ifile.close()
	def Frame(self) :
		self.dt = self.clock.tick(60)
		self.timeCounter += self.dt
		self.events = pygame.event.get() 
		self.key_pressed = pygame.key.get_pressed()
		if not self.dumpTime :
			self.dt = 0
			self.dumpTime = True
		for event in self.events : 
			if hasattr(event, 'key') and event.type == KEYDOWN :
				if event.key == K_ESCAPE :
					self.nextSceneState = NEXTSCENE_POP
		if self.key_pressed[K_LEFT] :
			self.px -= self.speed * self.dt
		if self.key_pressed[K_RIGHT] :
			self.px += self.speed * self.dt
		self.obY = list()
		for i in range(len(self.obList)) :
			posy = self.obList[i][0] - self.timeCounter
			posy = posy*800/2000
			posy = 800 - posy
			if posy < -100 :
				break
			posx = self.obList[i][1]
			dx = posx - self.px
			dy = posy - self.py
			dis = math.hypot(dx,dy)
			if dis < (self.obSize + self.charSize) / 2 :
				print 'collision!!'
			self.obY.append(posy)
	def Render(self) :
		self.screen.fill((0,0,0))
		self.screen.blit(self.charImage, (self.px, 700))
		for i in range(len(self.obY)) :
			self.screen.blit(self.obImage, (self.obList[i][1] - (self.obSize/2), self.obY[i] - (self.obSize/2)))
		pygame.display.flip()