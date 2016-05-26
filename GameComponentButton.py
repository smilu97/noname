import pygame, math, sys
from pygame.locals import *
from GameComponent import *

class GameComponentButton(GameComponent):
	def __init__(self, owner, onClick=0, senseRect = [0.0,0.0,0.0,0.0]):
		GameComponent.__init__(self, owner)
		self.senseRect = list(senseRect)
		self.onClick = onClick
		self.static = False
	def Frame(self,dt):
		if self.onClick != 0 :
			for event in self.owner.owner.events :
				if event.type == MOUSEBUTTONDOWN :
					mousepos = event.pos
					if not self.owner.static :
						mousepos = (mousepos[0] + self.owner.owner.cam[0], \
									mousepos[1] + self.owner.owner.cam[1])
					if self.senseRect[0] <= mousepos[0] and mousepos[0] <= self.senseRect[2] and \
						self.senseRect[1] <= mousepos[1] and mousepos[1] <= self.senseRect[3] :
						self.onClick()
					break
	def Render(self):
		pass