import pygame, math, sys
from pygame.locals import *
from GameComponent import *

class GameComponentText(GameComponent):
	def __init__(self, owner, position, fontName, fontSize, fontColor=(255,255,255), text=''):
		GameComponent.__init__(self, owner, position)
		self.fontName = fontName
		self.text = text
		self.font = pygame.font.Font(self.fontName, fontSize)
		self.fontColor = fontColor
		self.textImage = self.font.render(self.text, True, self.fontColor)
	def UpdateImage(self) :
		self.textImage = self.font.render(self.text, True, self.fontColor)
	def Render(self):
		worldPosition = self.GetWorldPosition()
		if self.owner.static :
			self.owner.owner.screen.blit(self.textImage, worldPosition)
		else :
			camPos = self.owner.owner.cam
			self.owner.owner.screen.blit(self.textImage, (worldPosition[0]-camPos[0], worldPosition[1]-camPos[1]))
