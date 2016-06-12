import pygame, math, sys, random
from pygame.locals import *
from Scene import *


class SceneAvoider(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		self.obList = []
		# self.Load('Data/Avoid/Scenario/Test.txt')
		for i in range(15) :
			self.obList.append([3000+i*800, random.randint(300, 800)])
		self.obY = []
		self.px = 550
		self.py = 700
		self.speed = 0.5
		self.timeCounter = 0
		self.charImage = pygame.image.load('Data/Avoid/Character.png')
		self.obImage = pygame.image.load('Data/Avoid/Obstacle.png')
		self.obSize = 100
		self.charSize = 100
		self.charImage = pygame.transform.scale(self.charImage, (self.charSize, self.charSize))
		self.obImage = pygame.transform.scale(self.obImage, (self.obSize, self.obSize))
		self.timer = 0
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
		if self.key_pressed[K_p] :
			self.nextScene = 'WorldMap'
			self.player.story = 6
			self.player.pos[0] = 4721
			self.player.pos[1] = 827
		if self.timer < 15000 :
			self.timer += self.dt
		else :
			self.nextScene = 'WorldMap'
			self.player.story = 6
			self.player.pos[0] = 4721
			self.player.pos[1] = 827
		if not self.dumpTime :
			self.dt = 0
			self.dumpTime = True
		for event in self.events : 
			if hasattr(event, 'key') and event.type == KEYDOWN :
				pass
		if self.key_pressed[K_LEFT] :
			self.px -= self.speed * self.dt
			if self.px < 300 :
				self.px = 300
		if self.key_pressed[K_RIGHT] :
			self.px += self.speed * self.dt
			if self.px > 800 :
				self.px = 800
		if self.key_pressed[K_ESCAPE] :
			self.nextSceneState = NEXTSCENE_POP
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
				self.nextScene = 'Avoider'
				return
			self.obY.append(posy)
	def Render(self) :
		self.screen.fill((0,0,0))
		self.screen.blit(self.charImage, (self.px, 700))
		for i in range(len(self.obY)) :
			self.screen.blit(self.obImage, (self.obList[i][1] - (self.obSize/2), self.obY[i] - (self.obSize/2)))
		pygame.display.flip()