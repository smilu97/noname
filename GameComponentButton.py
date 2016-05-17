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
					cam = self.owner.owner.cam
					realSenseRect = [self.senseRect[0] - cam[0], self.senseRect[1] - cam[1], \
										self.senseRect[2] - cam[0], self.senseRect[3] - cam[1]]
					mousepos = pygame.mouse.get_pos()
					if realSenseRect[0] <= mousepos[0] and mousepos[0] <= realSenseRect[2] and \
						realSenseRect[1] <= mousepos[1] and mousepos[1] <= realSenseRect[3] :
						self.onClick()
					break
	def Render(self):
		pass