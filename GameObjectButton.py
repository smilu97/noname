from GameObject import *

class GameObjectButton(GameObject):
	def __init__(self, owner, image, onClick, senseRect, name=''):
		GameObject.__init__(self, owner, name=name)
		self.components['button'] = GameComponentButton(self, onClick=onClick, senseRect=senseRect)
		self.components['image'] = GameComponentImage(self, image)
		self.position = [senseRect[0], senseRect[1]]