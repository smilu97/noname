from GameComponent import *

class GameComponentImage(GameComponent):
	def __init__(self, owner, image = 0, position = [0,0], able=True):
		GameComponent.__init__(self, owner, position=position)
		self.image = image
		self.able = able
	def Frame(self,dt) :
		pass
	def Render(self) :
		if self.able :
			screen = self.owner.owner.screen
			cam = self.owner.owner.cam
			printPos = (self.position[0] + self.owner.position[0] - cam[0], \
						self.position[1] + self.owner.position[1] - cam[1])
			screen.blit(self.image, printPos)
