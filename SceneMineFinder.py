import pygame, math, sys
from pygame.locals import *
from Scene import *

MINESIZE = 40
TILE_MINE = -1
SCREEN_SIZE = (1200, 800)

class SceneMineFinder(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		self.tile = []
		self.show = []
		self.width = 0
		self.height = 0
		self.mineNum = 0
		self.screendelta = (0,0)
		self.CreateMap(9,9, mineNum=10)
		self.mineImage = pygame.image.load('Data/Mine/MineImage.bmp')
		self.coverImage = pygame.image.load('Data/Mine/CoverImage.bmp')
		self.flagImage = pygame.image.load('Data/Mine/FlagImage.bmp')
		self.digitImage = []
		for i in range(9) :
			self.digitImage.append(pygame.image.load('Data/Mine/DigitImage%d.bmp'%i))
	def isMine(self, x, y) :
		if 0 <= x and x < self.width and 0 <= y and y < self.height :
			return self.tile[x][y] == TILE_MINE
		return False
	def CreateMap(self, width, height, mineNum) :
		self.tile = [[0 for i in range(height)] for j in range(width)]
		self.show = [[0 for i in range(height)] for j in range(width)]
		self.mineNum = mineNum
		self.width = width
		self.height = height
		self.screendelta = (SCREEN_SIZE[0]/2 - MINESIZE*self.width/2,SCREEN_SIZE[1]/2 - MINESIZE*self.height/2)
		for mineIndex in range(mineNum) :
			while True :
				randomx = random.randint(0,width-1)
				randomy = random.randint(0,height-1)
				if self.tile[randomx][randomy] != TILE_MINE :
					self.tile[randomx][randomy] = TILE_MINE
					break
		for x in range(height) :
			for y in range(width) :
				if self.tile[x][y] != TILE_MINE :
					mineCount = 0
					if self.isMine(x-1,y-1) : mineCount += 1
					if self.isMine(x  ,y-1) : mineCount += 1
					if self.isMine(x+1,y-1) : mineCount += 1

					if self.isMine(x-1,y  ) : mineCount += 1
					if self.isMine(x+1,y  ) : mineCount += 1

					if self.isMine(x-1,y+1) : mineCount += 1
					if self.isMine(x  ,y+1) : mineCount += 1
					if self.isMine(x+1,y+1) : mineCount += 1
					
					self.tile[x][y] = mineCount
	def Show(self, x, y) :
		if not (0 <= x and x < self.width and 0 <= y and y < self.height) :
			return
		if self.show[x][y] == 1 : return
		self.show[x][y] = 1
		if self.tile[x][y] == 0 :
			self.Show(x-1,y-1)
			self.Show(x  ,y-1)
			self.Show(x+1,y-1)

			self.Show(x-1,y  )
			self.Show(x+1,y  )
			
			self.Show(x-1,y+1)
			self.Show(x  ,y+1)
			self.Show(x+1,y+1)
	def EndCheck(self) :
		for i in range(self.width) :
			for j in range(self.height) :
				if self.tile[i][j] == -1 :
					if self.show[i][j] != 2 :
						return False
				else :
					if self.show[i][j] != 1 :
						return False
		return True
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
					self.nextSceneState = NEXTSCENE_POP
			if event.type == pygame.MOUSEBUTTONDOWN :
				mousepos = list(pygame.mouse.get_pos())
				mousepos[0] -= self.screendelta[0]
				mousepos[1] -= self.screendelta[1]
				x = int(mousepos[0] / MINESIZE)
				y = int(mousepos[1] / MINESIZE)
				if 0 <= x and x < self.width and 0 <= y and y < self.height :
					if event.button == 1 :
						if self.show[x][y] == 0 :
							if self.tile[x][y] == TILE_MINE :
								self.CreateMap(9,9,10);
							else :
								self.Show(x,y)
					elif event.button == 3:
						if self.show[x][y] == 0 :
							self.show[x][y] = 2
						elif self.show[x][y] == 2:
							self.show[x][y] = 0
				if self.EndCheck() :
					print 'Mine End!'
					self.nextScene = 'WorldMap'
					self.player.pos[0] = 3745.0
					self.player.pos[1] = 2198.0
					self.player.story = 3
		if self.key_pressed[K_p] :
			self.nextScene = 'WorldMap'
			self.player.pos[0] = 3745.0
			self.player.pos[1] = 2198.0
			self.player.story = 2
	def Render(self) :
		self.screen.fill((0,0,0))
		for x in range(self.width) :
			for y in range(self.height) :
				pos = (x*MINESIZE + self.screendelta[0], y*MINESIZE + self.screendelta[1])
				if self.show[x][y] == 1 :
					if self.tile[x][y] == TILE_MINE :
						self.screen.blit(self.mineImage, pos)
					else :
						self.screen.blit(self.digitImage[self.tile[x][y]], pos)
				elif self.show[x][y] == 2 :
					self.screen.blit(self.flagImage, pos)
				elif self.show[x][y] == 0 :
					self.screen.blit(self.coverImage, pos)
		pygame.display.flip()