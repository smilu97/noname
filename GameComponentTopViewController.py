import pygame, math, sys
from pygame.locals import *
from GameComponent import *

class GameComponentTopViewController(GameComponent):
	def __init__(self, owner, verticalSpeed, horizontalSpeed, showComponent={}):
		GameComponent.__init__(self, owner)
		self.verticalSpeed = verticalSpeed
		self.horizontalSpeed = horizontalSpeed
		self.showComponent = dict(showComponent)
	def Render(self):
		pass
	def Frame(self, dt):
		key_pressed = self.owner.owner.key_pressed
		hs = self.horizontalSpeed
		vs = self.verticalSpeed
		vx = vy = 0
		if key_pressed[K_LALT] :
			hs /= 2
			vs /= 2
		if key_pressed[K_LEFT] :
			vx -= hs
		if key_pressed[K_RIGHT] :
			vx += hs
		if key_pressed[K_UP] :
			vy -= vs
		if key_pressed[K_DOWN] :
			vy += vs
		dx = vx *dt
		dy = vy *dt
		self.owner.position[0] += dx
		self.owner.position[1] += dy

		for compo in self.showComponent.values() :
			compo.able = False
		if vx < 0 :
			self.showComponent['leftmove'].able = True
		elif vx > 0 :
			self.showComponent['rightmove'].able = True
		else :
			self.showComponent['idle'].able = True

		self.ownCollider = self.owner.components['collider']
		for coll in self.owner.owner.colliderList :
			if coll.owner == self.owner : continue
			if not coll.static :
				hcv = coll.GetHowColliding((dx, dy), self.ownCollider)
				if hcv == False : continue
				hcv = list(hcv)
				if hcv[1] == 0 : 
					if dx > 0 :
						self.owner.position[0] = coll.GetWorldRect()[0]-self.ownCollider.width
					else :
						self.owner.position[0] = coll.GetWorldRect()[0] + coll.width
					#self.owner.position[0] += (hcv[0]-1) * dx
				elif hcv[1] == 1 : 
					if dy > 0 :
						self.owner.position[1] = coll.GetWorldRect()[1] - self.ownCollider.height
					else :
						self.owner.position[1] = coll.GetWorldRect()[1] + coll.height
					#self.owner.position[1] += (hcv[0]-1) * dy
