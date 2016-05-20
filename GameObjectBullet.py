from GameObject import *

class GameObjectBullet(GameObject):
	def __init__(self, owner, position, bulletImage, size, name=''):
		GameObject.__init__(self,owner,position,name=name)
		self.position = position
		self.index = -1
		self.components['image'] = bulletImage
		self.components['collider'] = GameComponentBoxCollider(self, (0.0,0.0,size,size))
		self.components['controller'] = GameComponentBulletController(self, [0.0,0.0], -math.pi/2, 3.0,\
											 BulletShapeStraight)

