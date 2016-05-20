from GameObject import *

class GameObjectBullet(GameObject):
	def __init__(self, owner, position, bulletImage, size, direction, name=''):
		GameObject.__init__(self,owner,position,name=name)
		self.position = position
		self.key = -1
		self.components['image'] = GameComponentImage(self,bulletImage)
		self.components['collider'] = GameComponentBoxCollider(self, (0.0,0.0,size,size))
		self.components['collider'].static = True
		if direction == 1:
			angle = 0
		else :
			angle = math.pi
		self.components['controller'] = GameComponentBulletController(self, [0.0,0.0], angle, 10.0,\
											 size, BulletShapeStraight)

