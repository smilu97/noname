from GameObject import *

class GameObjectBullet(GameObject):
	def __init__(self, owner, position, bulletImage, size, angle, name='', key=-1, \
					bulletShape = BulletShapeStraight, speed=1.0):
		GameObject.__init__(self,owner,position,name=name)
		self.position = position
		self.key = key
		self.size = size
		self.components['image'] = GameComponentImage(self,bulletImage)
		self.components['collider'] = GameComponentCircleCollider(self, (size/2,size/2), size/2)
		self.components['collider'].static = True
		self.components['controller'] = GameComponentBulletController(self, [0.0,0.0], angle, speed,\
											 size, bulletShape)

