from GameObject import *

class GameObjectButton(GameObject):
	def __init__(self, owner, image, onClick, senseRect):
		GameObject.__init__(self, owner)
		buttonComponent = GameComponentButton(self, onClick=onClick, senseRect=senseRect)
		imageComponent = GameComponentImage(self, image)
		self.components.append(buttonComponent)
		self.components.append(imageComponent)
