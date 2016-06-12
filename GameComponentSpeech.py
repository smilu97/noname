import pygame, math, sys
from pygame.locals import *
from GameComponent import *

SPEECH_SKIP_KEY = K_z

class GameComponentSpeech(GameComponent):
	def __init__(self, owner, position, fontName, speed, fontColor) :
		GameComponent.__init__(self, owner)
		self.font = pygame.font.SysFont(fontName, 25)
		self.fontColor = fontColor
		self.text = []
		self.level = 0
		self.afterText = ''
		self.progress = 0
		self.speed = 0
		self.timecount = 0
		self.position = list(position)
		self.key = False
	def SetText(self, text) :
		self.text = list(text)
		self.afterText = ''
		self.progress = 0
		self.timecount = 0
		self.level = 0
	def Frame(self, dt) :
		if self.owner.owner.key_pressed[SPEECH_SKIP_KEY] :
			if not self.key :
				self.key = True
				if self.progress == len(self.text[self.level]) :
					if self.level < len(self.text)-1 :
						self.level += 1
						self.progress = 0
						self.timecount = 0
				else :
					self.progress = len(self.text[self.level])
		else :
			self.key = False
		if self.progress < len(self.text[self.level]) : 
			self.timecount += dt
			if self.timecount >= self.speed :
				self.progress += 1
				self.timecount -= self.speed
		self.afterText = self.text[self.level][:self.progress]
	def isLast(self) :
		return self.level == len(self.text)-1
	def Render(self):
		worldPosition = self.GetWorldPosition()
		if self.owner.static :
			self.owner.owner.screen.blit(self.font.render(self.afterText, True, self.fontColor), (worldPosition[0],\
											 worldPosition[1]))
		else :
			self.owner.owner.screen.blit(self.font.render(self.afterText, True, self.fontColor), (worldPosition[0]-self.owner.owner.cam[0],\
											 worldPosition[1] - self.owner.owner.cam[1]))
				