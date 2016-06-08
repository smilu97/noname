from GameObjectButton import *
from GameObjectPlayer import *
from GameObjectBullet import *
from GameObjectText import *
from GameObjectPortal import *

NEXTSCENE_POP = 0
NEXTSCENE_ERASE = -1
NEXTSCENE_STACK = 1

class Scene():
	def __init__(self, screen, clock, player):
		self.screen = screen
		self.clock = clock
		self.cam = np.array([0.0,0.0])
		self.objects = {}
		self.nextScene = self
		self.nextSceneState = NEXTSCENE_ERASE
		self.player = player
		self.dt = 0
		self.dumpTime = False
		self.spriteGroup = pygame.sprite.Group()
		self.colliderList = []
		# self.background = pygame.Surface()
		# pygame.gfxdraw.box(self.background,(0,0,1600,800),(0,0,0))

		# Console
		console = GameObjectText(self, [0.0,400.0], 'comicsansms', 15, text='Console')
		console.static = True
		console.name = 'console'
		self.console = console
		self.objects['console'] = console
	def NextSceneInit(self) :
		self.nextScene = self
		self.nextSceneState = NEXTSCENE_ERASE
	def Render(self) :
		self.screen.fill((0,0,0))
		RenderAll(self.objects.values())
		self.spriteGroup.draw(self.screen)
		pygame.display.flip()
	def statInConsole(self) :
		bContainer = self.objects['bulletContainer']
		consoleString =  'len of spriteGroup     : ' + str(len(self.spriteGroup)) + '\n'
		consoleString += 'len of bulletContainer : ' + str(len(bContainer)) + '\n'
		consoleString += 'len of colliderList    : ' + str(len(self.colliderList)) + '\n'
		self.objects['console'].changeText(consoleString)