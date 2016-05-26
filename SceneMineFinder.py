import pygame, math, sys
from pygame.locals import *
from Scene import *

TILE_MINE = -1
TILE_NOMINE = 1
MINESIZE = 40

class SceneMineFinder(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		self.tile = []
		self.checked = []
		self.width = 0
		self.height = 0
		self.mineNum = 0
		self.minePos = []
		self.nonMinePos = []

		self.CreateMap(10,10, mineNum=10)
		self.mineImage = pygame.image.load('Data/MineImage.bmp')
		self.nomineImage = pygame.image.load('Data/NomineImage.bmp')
	def CreateMap(self, width, height, mineNum) :
		self.tile = [[TILE_NOMINE for i in range(width)] for j in range(height)] # height x width
		self.checked = [[0 for i in range(width)] for j in range(height)] # height x width
		self.mineNum = mineNum
		self.width = width
		self.height = height
		for mineIndex in range(mineNum) :
			while True :
				randomx = random.randint(0,width-1)
				randomy = random.randint(0,height-1)
				if self.tile[randomx][randomy] != TILE_MINE :
					self.tile[randomx][randomy] = TILE_MINE
					self.minePos.append((randomx,randomy))
					break
		for x in range(height) :
			for y in range(width) :
				if self.tile[x][y] == TILE_NOMINE :
					self.nonMinePos.append((x,y))
	def Frame(self):
		self.dt = self.clock.tick(60)
		if not self.dumpTime :
			self.dumpTime = True
			self.dt = 0
		self.events = pygame.event.get()
		self.key_pressed = pygame.key.get_pressed()
		for event in self.events :
			if hasattr(event, 'key') and event.type == KEYDOWN :
				if event.key == K_ESCAPE :
					sys.exit(0)
			if event.type == pygame.MOUSEBUTTONDOWN :
				mousepos = pygame.mouse.get_pos()
				y = int(mousepos[0] / MINESIZE)
				x = int(mousepos[1] / MINESIZE)
				# TODO : [x][y]
	def Render(self) :
		self.screen.fill((0,0,0))
		for x in range(self.height) :
			for y in range(self.width) :
				if self.checked[x][y] == 1 :
					if self.tile[x][y] == TILE_MINE :
						self.screen.blit(self.mineImage, (y*MINESIZE, x*MINESIZE))
					elif self.tile[x][y] == TILE_NOMINE :
						self.screen.blit(self.nomineImage, (y*MINESIZE, x*MINESIZE))
				elif self.checked[x][y] == 0 :
					self.screen.blit(self.blockImage, (y*MINESIZE, x*MINESIZE))
				elif self.checked[x][y] == 2 :
					# TODO : Flag
					pass
		pygame.display.flip()