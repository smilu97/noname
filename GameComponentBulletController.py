import pygame, math, sys
from pygame.locals import *
from GameComponent import *

def BulletShapeStraight(self, time, dt) :
	return np.zeros(2)
def BulletShapeChasePlayer(self, time, dt) :
	player = self.owner.owner.objects['player']
	playerPos = player.position + player.size/2
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
	self.basePositionAdder = np.array((math.cos(self.direction), math.sin(self.direction))) * self.speed
	return np.zeros(2)
def BulletShapeSin(self, time, dt) :
	return np.array((0.0, math.sin(time/100)*10))
class GameComponentBulletController(GameComponent):
	def __init__(self, owner, position, direction, speed, size, shapeFunc=BulletShapeStraight):
		GameComponent.__init__(self, owner, position)
		self.direction = direction
		self.speed = speed
		self.basePosition = self.owner.position
		self.shapeFunc = shapeFunc
		self.basePositionAdder = np.array([math.cos(self.direction), math.sin(self.direction)]) * self.speed
		self.rect = np.array((0.0,0.0,size,size))
		self.timeCounter = 0
	def Delete(self) :
		del self.owner.owner.objects['bulletContainer'][self.owner.key]
	def Frame(self,dt):
		self.timeCounter += dt
		shapeAdder = self.shapeFunc(self,self.timeCounter, dt)
		shapeAdder = RotatePosition(shapeAdder, self.direction)
		self.basePosition += self.basePositionAdder * dt
		self.owner.position = self.basePosition + shapeAdder
		px = self.owner.position[0]
		py = self.owner.position[1]
		if px < -200 or 1400 < px or py < -200 or 1000 < py :
			self.Delete()
		myRect = self.GetWorldRect()
		for obj in DecomposeList(self.owner.owner.objects.values()) :
			if obj == self.owner : continue
			if obj == self.owner.owner.objects['player'] : continue
			coll = obj.components.get('collider', 0)
			if coll != 0 :
				if not coll.static :
					if coll.GetIsColliding(self.owner.components['collider']) :
						del self.owner.owner.objects['bulletContainer'][self.owner.key]
		
