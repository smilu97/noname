import pygame, math, sys
from pygame.locals import *
from GameComponent import *

def BulletShapeStraight(time) :
	return (0.0,0.0)

class GameComponentBulletController(GameComponent):
	def __init__(self, owner, position, direction, speed, shapeFunc=BulletShapeStraight):
		GameComponent.__init__(self, owner, position)
		self.direction = direction
		self.speed = speed
		self.basePosition = self.owner.position
		self.shapeFunc = shapeFunc
		self.basePositionAdder = (math.cos(self.direction)*self.speed, math.sin(self.direction)*self.speed)
		self.timeCounter = 0
	def Frame(self,dt):
		self.timeCounter += dt
		self.basePosition += self.basePositionAdder
		shapeAdder = shapeFunc(self.timeCounter)
		shapeAdder = RotatePosition(shapeAdder, self.direction)
		self.owner.position[0] = self.basePosition + shapeAdder[0]
		self.owner.position[1] = self.basePosition + shapeAdder[1]
