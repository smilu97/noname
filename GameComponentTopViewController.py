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
		self.owner.position[0] += vx * dt
		self.owner.position[1] += vy * dt

		for compo in self.showComponent.values() :
			compo.able = False
		if vx < 0 :
			self.showComponent['leftmove'].able = True
		elif vx > 0 :
			self.showComponent['rightmove'].able = True
		else :
			self.showComponent['idle'].able = True
