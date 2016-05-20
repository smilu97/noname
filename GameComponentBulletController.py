import pygame, math, sys
from pygame.locals import *
from GameComponent import *

def BulletShapeStraight(time) :
	return (0.0,0.0)

class GameComponentBulletController(GameComponent):
	def __init__(self, owner, position, direction, speed, size, shapeFunc=BulletShapeStraight):
		GameComponent.__init__(self, owner, position)
		self.direction = direction
		self.speed = speed
		self.basePosition = self.owner.position
		self.shapeFunc = shapeFunc
		self.basePositionAdder = (math.cos(self.direction)*self.speed, math.sin(self.direction)*self.speed)
		self.rect = (0.0,0.0,size,size)
		self.timeCounter = 0
	def Frame(self,dt):
		self.timeCounter += dt
		self.basePosition[0] += self.basePositionAdder[0]
		self.basePosition[1] += self.basePositionAdder[1]
		shapeAdder = self.shapeFunc(self.timeCounter)
		shapeAdder = RotatePosition(shapeAdder, self.direction)
		self.owner.position[0] = self.basePosition[0] + shapeAdder[0]
		self.owner.position[1] = self.basePosition[1] + shapeAdder[1]
		myRect = self.GetWorldRect()
		for obj in DecomposeList(self.owner.owner.objects.values()) :
			if obj == self.owner : continue
			if obj == self.owner.owner.objects['player'] : continue
			coll = obj.components.get('collider', 0)
			if coll != 0 :
				if not coll.static :
					if coll.GetIsColliding(myRect) :
						del self.owner.owner.objects['bulletContainer'][self.owner.key]
		
