import pygame, math, sys
from pygame.locals import *

class GameComponent():
	def __init__(self,owner,position=[0,0]):
		self.owner = owner
		self.position = position