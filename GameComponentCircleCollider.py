import pygame, math, sys, random
from pygame.locals import *
from GameComponent import *

class GameComponentCircleCollider(GameComponent):
	def __init__(self, owner, position, radius):
		GameComponent.__init__(self,owner,position)
		self.index = len(self.owner.owner.colliderList)
		self.owner.owner.colliderList.append(self)
		self.radius = radius
		self.colliderType = 'circle'
		self.static = False
		self.width = radius * 2
		self.height = radius * 2
	def kill(self) :
		cList = self.owner.owner.colliderList
		for compo in cList[self.index+1:] :
			compo.index -= 1
		del cList[self.index]
	def GetHowColliding(self, delta, otherCollider) :
		if otherCollider.colliderType == 'box' :
			return otherCollider.GetHowColliding((-delta[0],-delta[1]),self)
		elif otherCollider.colliderType == 'circle' :
			other = otherCollider.GetWorldPosition()
			prev = (other[0]-delta[0],other[1]-delta[1])
			mine = self.GetWorldPosition()
			tangent = delta[1]/delta[0]
			dx = prev[0] - mine[0]
			dy = prev[1] - mine[1]
			R = self.radius + otherCollider.radius
			A = 1 + tangent**2
			B = 2*(dx + tangent*dy)
			C = dx**2 + dy**2 - R**2
			S = math.sqrt(B**2 - 4*A*C)
			ans_m = (-B-S) / (2*A)
			ans_M = (-B+S) / (2*A)
			if abs(ans_m) < abs(ans_M) :
				ans = ans_m
			else :
				ans = ans_M 
			return ans/delta[0]
	def GetIsColliding(self, otherCollider) :
		if otherCollider.colliderType == 'box' :
			return otherCollider.GetIsColliding(self)
		elif otherCollider.colliderType == 'circle' :
			other = otherCollider.GetWorldPosition()
			mine = self.GetWorldPosition()
			dx = other[0] - mine[0]
			dy = other[1] - mine[1]
			distance = math.sqrt(dx**2 + dy**2)
			if distance < self.radius + otherCollider.radius :
				return True
			return False
	def GetIsCollidingWithRawCircle(self, other, radius) :
		delta = self.GetWorldPosition() - np.array(other)
		dist = math.hypot(delta[0], delta[1])
		if dist < radius + self.radius :
			return True
		return False