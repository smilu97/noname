import pygame, math, sys
from pygame.locals import *
from CustomFunctions import *
import numpy as np

class GameComponent():
	def __init__(self,owner,position=[0.0,0.0]):
		self.owner = owner
		self.position = np.array(position)
	def GetWorldRect(self) :
		return np.array((self.rect[0] + self.owner.position[0],\
						self.rect[1] + self.owner.position[1],\
						self.rect[2],\
						self.rect[3]))
	def GetWorldPosition(self) :
		return self.position + self.owner.position
	def Frame(self,dt):
		pass
	def Render(self):
		pass