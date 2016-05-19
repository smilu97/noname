from GameComponentButton import *
from GameComponentImage import *
from GameComponentBoxCollider import *
from GameComponentCharacterController import *
from GameComponentCameraController import *
from GameComponentAnimator import *
from GameComponentSpeech import *

class GameObject():
	def __init__(self, owner, position=[0.0,0.0], components={}, name=''):
		self.owner = owner
		self.position = list(position)
		self.components = dict(components)
		self.name = str(name)
		self.static = False
	def Frame(self,dt):
		for compo in self.components.values() :
			compo.Frame(dt)
	def Render(self):
		for compo in self.components.values() :
			compo.Render()