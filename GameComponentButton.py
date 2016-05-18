import pygame, math, sys
from pygame.locals import *
from GameComponent import *

class GameComponentButton(GameComponent):
	def __init__(self, owner, onClick=0, senseRect = [0,0,0,0]):
		GameComponent.__init__(self, owner)
		self.senseRect = senseRect
		self.onClick = onClick
	def Frame(self):
		if self.onClick != 0 :
			for event in self.owner.owner.events :
				if event.type == pygame.MOUSEBUTTONDOWN :
					mousepos = pygame.mouse.get_pos()
					if self.senseRect[0] <= mousepos[0] and mousepos[0] <= self.senseRect[2] and \
						self.senseRect[1] <= mousepos[1] and mousepos[1] <= self.senseRect[3] :
						self.onClick()
					break
	def Render(self):
		pass