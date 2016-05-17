from GameComponentButton import *
from GameComponentImage import *

class GameObject():
	def __init__(self, owner, position=[0,0]):
		self.owner = owner
		self.position = position
		self.components = []
	def Frame(self):
		for compo in self.components :
			compo.Frame()
	def Render(self):
		for compo in self.components :
			compo.Render()