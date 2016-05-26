from GameObject import *

class GameObjectText(GameObject):
	def __init__(self, owner, position, fontName, fontSize, fontColor=(255,255,255), text=''):
		GameObject.__init__(self,owner,position, name='console')
		self.components['text'] = GameComponentText(self, (0.0,0.0), fontName, fontSize, fontColor, text)