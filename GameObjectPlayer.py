from GameObject import *

CHARACTER_DEFAULT_SIZE = 40.0

class GameObjectPlayer(GameObject):
	def __init__(self, owner, position, image, size=CHARACTER_DEFAULT_SIZE, name='', showComponent={}):
		GameObject.__init__(self, owner, position, name=name)
		self.components['image'] = GameComponentImage(self, image)
		self.size = size
		self.horizontalDirection = 1
		self.components['controller'] = GameComponentCharacterController(self, (0, 0,\
										self.size, self.size), showComponent)
		self.hp = 10