from GameObject import *

class GameObjectBullet(GameObject):
	def __init__(self, owner, position, bulletImage, size, angle, name='', \
					bulletShape = BulletShapeStraight, speed=1.0):
		GameObject.__init__(self,owner,position,name=name)
		self.position = position
		self.size = size
		self.components['image'] = GameComponentImage(self,bulletImage)
		self.components['collider'] = GameComponentCircleCollider(self, (size/2,size/2), size/2)
		self.components['collider'].static = True
		self.components['controller'] = GameComponentBulletController(self, [0.0,0.0], angle, speed,\
											 size, bulletShape)
		bContainer = self.owner.objects['bulletContainer']
		self.key = len(bContainer)
		bContainer.append(self)
	def kill(self) :
		self.components['image'].kill()
		self.components['collider'].kill()
		bContainer = self.owner.objects['bulletContainer']
		for obj in bContainer[self.key+1:] :
			obj.key -= 1
 		del bContainer[self.key]