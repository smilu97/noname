import pygame, math, sys
from pygame.locals import *
from Scene import *

MINE = -1

class SceneAvoider(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		self.tile = [[-2 for i in range(5)] for j in range(5)]
		# set mines
		# count near mines
	def Frame(self) :
		pass
	def Render(self) :
		pass