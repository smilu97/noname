import pygame, math, sys
from pygame.locals import *
from GameComponent import *

CHARACTER_HORIZONTAL_SPEED = 3
CHARACTER_JUMP_FORCE = 10.0
CHARACTER_GRAVITY = 0.5
class GameComponentCharacterController(GameComponent) :
	def __init__(self, owner, rect, showComponent={}) :
		GameComponent.__init__(self, owner)
		self.ownCollider = owner.components.get('collider', 0)
		self.vy = 0
		self.vx = 0
		self.rect = list(rect)
		self.width = rect[2] - rect[0]
		self.height = rect[3] - rect[1]
		self.isground = False
		self.showComponent = dict(showComponent)
	def changeShow(self, val) :
		for compo in self.showComponent.values() :
			compo.able = False
		self.showComponent[val].able = True
	def Frame(self,dt):
		self.vx = 0.0
		self.vy += CHARACTER_GRAVITY
		prevRect = self.GetWorldRect()
		if self.owner.owner.key_pressed[K_LEFT] :
			self.vx -= CHARACTER_HORIZONTAL_SPEED
			self.owner.horizontalDirection = -1
		if self.owner.owner.key_pressed[K_RIGHT] :
			self.vx += CHARACTER_HORIZONTAL_SPEED
			self.owner.horizontalDirection = 1
		for event in self.owner.owner.events :
			if hasattr(event, 'key') :
				if event.type == KEYDOWN and event.key == K_UP and self.isground :
					self.vy -= CHARACTER_JUMP_FORCE
		self.owner.position[0] += self.vx
		self.owner.position[1] += self.vy
		self.isground = False
		myRect = self.GetWorldRect()
		for obj in DecomposeList(self.owner.owner.objects.values()) :
			if obj == self.owner : continue
			coll = obj.components.get('collider', 0)
			if coll != 0 :
				if not coll.static :
					hcv = coll.GetHowColliding((self.vx, self.vy), self.owner.components['collider'])
					if hcv == False : continue
					hcv = list(hcv)
					if hcv[1] == 0 : 
						self.owner.position[0] += (hcv[0]-1) * self.vx
					elif hcv[1] == 1 : 
						self.owner.position[1] += (hcv[0]-1) * self.vy
					if hcv[1] == 1 :
						if self.vy > 0 :
							self.isground = True
						else :
							self.vy = 0
		if self.vx == 0 :
			self.changeShow('idle')
		else :
			self.changeShow('run')
		if self.isground :
			self.vy = 0
	def Render(self) :
		pass
