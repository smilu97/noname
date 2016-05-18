from GameObject import *

class GameObjectButton(GameObject):
	def __init__(self, owner, image, onClick, senseRect):
		GameObject.__init__(self, owner)
		self.components['button'] = GameComponentButton(self, onClick=onClick, senseRect=senseRect)
		self.components['image'] = GameComponentImage(self, image)
