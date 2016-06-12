from GameObject import *

class GameObjectText(GameObject):
	def __init__(self, owner, position, fontName, fontSize, fontColor=(255,255,255), text=''):
		GameObject.__init__(self,owner,position, name='console')
		self.text = text
		self.texts = text.split('\n')
		self.font = pygame.font.Font(fontName, fontSize)
		for i in range(len(self.texts)) :
			self.components['image'+str(i)] = GameComponentImage(self, self.font.render(self.texts[i], True, fontColor), (0.0, fontSize*i), True)
		self.fontName = fontName
		self.fontSize = fontSize
		self.fontColor = fontColor
		self.empty = self.font.render('', True, fontColor)
	def changeText(self, text) :
		self.text = text
		self.texts = text.split('\n')
		for i in range(len(self.texts)) :
			keyString = 'image' + str(i)
			imgComp = self.components.get(keyString, 0)
			if imgComp == 0 :
				self.components[keyString] = GameComponentImage(self, self.font.render(self.texts[i], True, self.fontColor), (0.0, self.fontSize*i), True)
			else :
				imgComp.original = self.font.render(self.texts[i], True, self.fontColor)
		for i in range(len(self.texts), len(self.components)) :
			self.components['image'+str(i)].original = self.empty
	def addText(self, text) :
		self.changeText(self.text + text)