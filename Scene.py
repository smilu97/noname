from GameObjectButton import *

class Scene():
	def __init__(self, screen, clock):
		self.screen = screen
		self.clock = clock
		self.cam = [0,0]
		self.objects = {}
		self.nextScene = self
		