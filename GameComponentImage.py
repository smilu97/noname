from GameComponent import *

class GameComponentImage(GameComponent, pygame.sprite.Sprite):
	def __init__(self, owner, image = 0, position = [0,0], able=True):
		GameComponent.__init__(self, owner, position=position)
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.able = able
		self.rect = image.get_rect()
		self.owner.owner.spriteGroup.add(self)
		self.original = image
		self.blank = pygame.Surface((0,0))
	def Frame(self,dt) :
		pass
	def Render(self) :
		if self.able :
			self.image = self.original
			if not self.owner.static :
				cam = self.owner.owner.cam
				self.rect.x = self.position[0] + self.owner.position[0] - cam[0]
				self.rect.y = self.position[1] + self.owner.position[1] - cam[1]
			else :
				self.rect.x = self.position[0]
				self.rect.y = self.position[1]
		else :
			self.image = self.blank