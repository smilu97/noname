import pygame, math, sys
from pygame.locals import *
from GameComponent import *

def BulletShapeStraight(self, time, dt) :
	return (0.0,0.0)
def BulletShapeChasePlayer(self,time, dt) :
	player = self.owner.owner.objects['player']
	playerPos = (player.position[0] + (player.size/2), \
				player.position[1] + (player.size/2))
	myPos = self.GetWorldPosition()
	myPos = (myPos[0] + self.owner.size/2, myPos[1] + self.owner.size/2)
	delta = (playerPos[0] - myPos[0], playerPos[1] - myPos[1])
	angle = math.atan(delta[1]/delta[0])
	if delta[0] < 0 :
		angle += math.pi
	angle = RerangeAngle(angle)
	p_angle = RerangeAngle(self.direction + 0.01 * dt)
	m_angle = RerangeAngle(self.direction - 0.01 * dt)
	if abs(RerangeAngle(m_angle-angle)) < abs(RerangeAngle(p_angle-angle)) :
		self.direction = m_angle
	else :
		self.direction = p_angle
	while self.direction > 2*math.pi :
		self.direction -= 2*math.pi
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
		shapeAdder = self.shapeFunc(self,self.timeCounter, dt)
		shapeAdder = RotatePosition(shapeAdder, self.direction)
		self.basePositionAdder = (math.cos(self.direction)*self.speed, math.sin(self.direction)*self.speed)
		self.basePosition[0] += self.basePositionAdder[0] * dt
		self.basePosition[1] += self.basePositionAdder[1] * dt
		self.owner.position[0] = self.basePosition[0] + shapeAdder[0]
		self.owner.position[1] = self.basePosition[1] + shapeAdder[1]
		myRect = self.GetWorldRect()
		for obj in DecomposeList(self.owner.owner.objects.values()) :
			if obj == self.owner : continue
			if obj == self.owner.owner.objects['player'] : continue
			coll = obj.components.get('collider', 0)
			if coll != 0 :
				if not coll.static :
					if coll.GetIsColliding(self.owner.components['collider']) :
						del self.owner.owner.objects['bulletContainer'][self.owner.key]
		
