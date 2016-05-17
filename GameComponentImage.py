from GameComponent import *

class GameComponentImage(GameComponent):
	def __init__(self, owner, image = 0):
		GameComponent.__init__(self, owner)
		self.image = image
	def Frame(self) :
		pass
	def Render(self) :
		screen = self.owner.owner.screen
		cam = self.owner.owner.cam
		screen.blit(self.image, (self.position[0] + self.owner.position[0] - cam[0], \
									self.position[1] + self.owner.position[1] - cam[1]))
