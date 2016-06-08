from GameObject import *
import numpy as np

CHARACTER_DEFAULT_SIZE = 40.0

class GameObjectPlayer(GameObject):
	def __init__(self, owner, position, image, playerColl, mapName, size=CHARACTER_DEFAULT_SIZE, name='', showComponent={}):
		GameObject.__init__(self, owner, position, name=name)
		self.components['image'] = GameComponentImage(self, image)
		self.collider = GameComponentBoxCollider(self, np.array(0.0,0.0,CHARACTER_DEFAULT_SIZE,CHARACTER_DEFAULT_SIZE));
		self.collider.static = True;
		self.components['collider'] = self.collider
		self.size = size
	def Frame(self, dt) :
		FrameAll(self.components.values(), dt)
		if playerColl.GetIsColliding(self.collider) :
			self.owner.nextScene = mapName