import pygame, math, sys
from pygame.locals import *
from GameComponent import *

class GameComponentBulletScenario(GameComponent):
	def __init__(self, owner, fileName, bulletMaker):
		GameComponent.__init__(self, owner)
		self.fileName = fileName
		self.bulletPlan = []
		self.timeCounter = 0
		self.bulletMaker = bulletMaker
		self.LoadFile()
	def LoadFile(self):
		ifile = open(self.fileName, 'r')
		raw_data = ifile.read()
		ifile.close()
		plans = raw_data.split('\n')
		if plans[-1] == '' :
			plans.pop()
		self.bulletPlan = [[float(i) for i in plan.split(' ')] for plan in plans]
		for i in range(len(self.bulletPlan)) :
			self.bulletPlan[i][1] = int(self.bulletPlan[i][1])
	def Frame(self, dt):
		if len(self.bulletPlan) != 0 :
			self.timeCounter += dt
			index = 0
			while index < len(self.bulletPlan) :
				plan = self.bulletPlan[index]
				if plan[0] > self.timeCounter :
					break
				self.bulletMaker[plan[1]](plan[2], plan[3], plan[4])
				index += 1
			del self.bulletPlan[:index]
