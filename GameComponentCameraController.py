import pygame, math, sys
from pygame.locals import *
from GameComponent import *

CAMERA_MOVE_SPEED = 30.0

class GameComponentCameraController(GameComponent):
	def __init__(self, owner):
		GameComponent.__init__(self, owner)
	def Frame(self,dt):
		if self.owner.owner.key_pressed[K_w] :
			self.owner.owner.cam[1] -= CAMERA_MOVE_SPEED
		if self.owner.owner.key_pressed[K_s] :
			self.owner.owner.cam[1] += CAMERA_MOVE_SPEED
		if self.owner.owner.key_pressed[K_a] :
			self.owner.owner.cam[0] -= CAMERA_MOVE_SPEED
		if self.owner.owner.key_pressed[K_d] :
			self.owner.owner.cam[0] += CAMERA_MOVE_SPEED
	def Render(self):
		pass
