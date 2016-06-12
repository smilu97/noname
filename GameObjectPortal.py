from GameObject import *
import numpy as np

CHARACTER_DEFAULT_SIZE = 40.0

class GameObjectPortal(GameObject):
	def __init__(self, owner, position, image, playerColl, mapName, size=CHARACTER_DEFAULT_SIZE, name='', showComponent={}):
		GameObject.__init__(self, owner, position, name=name)
		self.components['image'] = GameComponentImage(self, image)
		self.collider = GameComponentBoxCollider(self, [0.0,0.0,CHARACTER_DEFAULT_SIZE,CHARACTER_DEFAULT_SIZE]);
		self.collider.static = True;
		self.components['collider'] = self.collider
		self.playerColl = playerColl
		self.size = size
		self.mapName = mapName
	def Frame(self, dt) :
		FrameAll(self.components.values(), dt)
		if self.playerColl.GetIsColliding(self.collider) :
			self.owner.nextScene = self.mapName