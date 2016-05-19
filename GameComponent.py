import pygame, math, sys
from pygame.locals import *

class GameComponent():
	def __init__(self,owner,position=[0.0,0.0]):
		self.owner = owner
		self.position = list(position)
	def GetWorldRect(self) :
		return (self.rect[0] + self.owner.position[0],\
				self.rect[1] + self.owner.position[1],\
				self.rect[2] + self.owner.position[0],\
				self.rect[3] + self.owner.position[1])
	def Frame(self,dt):
		pass
	def Redner(self):
		pass