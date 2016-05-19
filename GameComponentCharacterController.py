import pygame, math, sys
from pygame.locals import *
from GameComponent import *

CHARACTER_HORIZONTAL_SPEED = 3
CHARACTER_JUMP_FORCE = 10.0
CHARACTER_GRAVITY = 0.5
class GameComponentCharacterController(GameComponent):
	def __init__(self, owner, rect):
		GameComponent.__init__(self, owner)
		self.ownCollider = owner.components.get('collider', 0)
		self.vy = 0
		self.vx = 0
		self.rect = list(rect)
		self.width = rect[2] - rect[0]
		self.height = rect[3] - rect[1]
		self.isground = False
	def Frame(self,dt):
		self.vx = 0.0
		self.vy += CHARACTER_GRAVITY
		prevRect = (self.owner.position[0], self.owner.position[1], \
					self.owner.position[0] + self.width,\
					self.owner.position[1] + self.height)
		if self.owner.owner.key_pressed[K_LEFT] :
			self.vx -= CHARACTER_HORIZONTAL_SPEED
		if self.owner.owner.key_pressed[K_RIGHT] :
			self.vx += CHARACTER_HORIZONTAL_SPEED
		for event in self.owner.owner.events :
			if hasattr(event, 'key') :
				if event.type == KEYDOWN and event.key == K_UP and self.isground :
					self.vy -= CHARACTER_JUMP_FORCE
		self.owner.position[0] += self.vx
		self.owner.position[1] += self.vy
		self.isground = False
		for obj in self.owner.owner.objects.values() :
			coll = obj.components.get('collider', 0)
			if coll != 0 :
				hcv = coll.GetHowColliding(prevRect, self.GetWorldRect())
				if hcv == False : continue
				if hcv[1] == 0 : self.owner.position[0] += (hcv[0]-1) * self.vx
				elif hcv[1] == 1 : self.owner.position[1] += (hcv[0]-1) * self.vy
				if hcv[1] == 1 and self.vy > 0 :
					self.isground = True
					self.owner.position[1] = prevRect[1]
		if self.isground :
			self.vy = 0
	def Render(self) :
		pass