from GameObjectButton import *
from GameObjectPlayer import *

NEXTSCENE_POP = 0
NEXTSCENE_ERASE = -1
NEXTSCENE_STACK = 1

class Scene():
	def __init__(self, screen, clock, player):
		self.screen = screen
		self.clock = clock
		self.cam = [0.0,0.0]
		self.objects = {}
		self.nextScene = self
		self.nextSceneState = NEXTSCENE_ERASE
		self.player = player
		self.dt = 0
	def NextSceneInit(self) :
		self.nextScene = self
		self.nextSceneState = NEXTSCENE_ERASE