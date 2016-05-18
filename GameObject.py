from GameComponentButton import *
from GameComponentImage import *

class GameObject():
	def __init__(self, owner, position=[0,0], components={}):
		self.owner = owner
		self.position = position
		self.components = components
	def Frame(self):
		for compo in self.components.values() :
			compo.Frame()
	def Render(self):
		for compo in self.components.values() :
			compo.Render()