from GameObject import *

CHARACTER_SIZE = 40.0

class GameObjectPlayer(GameObject):
	def __init__(self, owner, position, image, size=CHARACTER_SIZE, name=''):
		GameObject.__init__(self, owner, position, name=name)
		self.components['image'] = GameComponentImage(self, image)
		self.size = size
		self.components['controller'] = GameComponentCharacterController(self, (0, 0,\
										self.size, self.size))

