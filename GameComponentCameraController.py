import pygame, math, sys
from pygame.locals import *
from GameComponent import *

CAMERA_MOVE_SPEED = 30.0
CAMERA_PADDING_HORIZONTAL = 50
CAMERA_PADDING_VERTICAL = 50
SCREEN_WIDTH_HALF = 600
SCREEN_HEIGHT_HALF = 400

class GameComponentCameraController(GameComponent):
	def __init__(self, owner, target):
		GameComponent.__init__(self, owner)
		self.target = target
		self.cam = self.owner.owner.cam
	def Frame(self,dt):
		# if self.owner.owner.key_pressed[K_w] :
		# 	self.owner.owner.cam[1] -= CAMERA_MOVE_SPEED
		# if self.owner.owner.key_pressed[K_s] :
		# 	self.owner.owner.cam[1] += CAMERA_MOVE_SPEED
		# if self.owner.owner.key_pressed[K_a] :
		# 	self.owner.owner.cam[0] -= CAMERA_MOVE_SPEED
		# if self.owner.owner.key_pressed[K_d] :
		# 	self.owner.owner.cam[0] += CAMERA_MOVE_SPEED
		xmax = self.cam[0] + SCREEN_WIDTH_HALF + CAMERA_PADDING_HORIZONTAL
		xmin = xmax - 2 * CAMERA_PADDING_HORIZONTAL
		ymax = self.cam[1] + SCREEN_HEIGHT_HALF + CAMERA_PADDING_VERTICAL
		ymin = ymax - 2 * CAMERA_PADDING_VERTICAL 
		if self.target.position[0] > xmax :
			self.cam[0] += self.target.position[0] - xmax
		elif self.target.position[0] < xmin :
			self.cam[0] += self.target.position[0] - xmin
		if self.target.position[1] > ymax :
			self.cam[1] += self.target.position[1] - ymax
		elif self.target.position[1] < ymin :
			self.cam[1] += self.target.position[1] - ymin
	def Render(self):
		pass
