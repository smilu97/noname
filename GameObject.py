from GameComponentButton import *
from GameComponentImage import *
from GameComponentBoxCollider import *
from GameComponentCharacterController import *
from GameComponentCameraController import *
from GameComponentAnimator import *
from GameComponentSpeech import *
from GameComponentBulletController import *
from GameComponentCharacterGun import *
from GameComponentCircleCollider import *
from GameComponentTopViewController import *

class GameObject():
	def __init__(self, owner, position=[0.0,0.0], components={}, name=''):
		self.owner = owner
		self.position = list(position)
		self.components = dict(components)
		self.name = str(name)
		self.static = False
	def Frame(self,dt):
		FrameAll(self.components.values(), dt)
	def Render(self):
		RenderAll(self.components.values())