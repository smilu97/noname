from GameObject import *
import numpy as np

class GameObjectButton(GameObject):
	def __init__(self, owner, image, onClick, senseRect, name=''):
		GameObject.__init__(self, owner, name=name)
		self.components['button'] = GameComponentButton(self, onClick=onClick, senseRect=(0,0,senseRect[2],senseRect[3]))
		self.components['image'] = GameComponentImage(self, image)
		self.position = np.array([senseRect[0], senseRect[1]])