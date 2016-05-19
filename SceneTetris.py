import pygame, math, sys
from pygame.locals import *
from Scene import *
import random

tetri = []
tetri.append([[0,0],[1,0],[0,1],[1,1]]) # nemo
tetri.append([[0,0],[-1,0],[0,1],[0,2]]) # gguck 1
tetri.append([[0,0],[1,0],[0,1],[0,2]]) # gguck 2
tetri.append([[0,0],[0,-1],[-1,0],[1,0]]) # fuck you
tetri.append([[0,0],[0,-1],[0,1],[0,2]]) # long
tetri.append([[0,0],[0,-1],[1,0],[1,1]]) # gguck gguck 1
tetri.append([[0,0],[0,-1],[-1,0],[-1,1]]) # gguck gguck 2

BLOCK = 1
NONBLOCK = 0
WIDTH = 10
HEIGHT = 20
BLOCKSIZE = 30

class Tile :
	def __init__(self) :
		self.dat = []
		for i in range(WIDTH) :
			self.dat.append([0]*HEIGHT)
		self.nowtetri_shape = []
		self.nowtetri_pos = [0,0]
		self.nowtetri_positions = []
	def shapeToPosition(self, position, shape) :
		positions = []
		for i in range(4) :
			pos = [position[0]+shape[i][0], position[1]+shape[i][1]]
			if (not (0 <= pos[0] and pos[0] < WIDTH)) or (not (0 <= pos[1] and pos[1] < HEIGHT)) :
				return [-1]
			positions.append(pos)
		return positions
 	def check(self, positions, value) :
 		for pos in positions :
 			if self.dat[pos[0]][pos[1]] != value :
 				return False
 		return True
	def setTetri(self, positions, value = BLOCK) :
		for pos in positions :
			self.dat[pos[0]][pos[1]] = value
	def makeTetri(self, position, shape, value = BLOCK) :
		positions = self.shapeToPosition(position, shape)
		if len(positions) == 1 :
			return False
		if self.check(positions, NONBLOCK) : #OK
			self.setTetri(positions, BLOCK)
			self.nowtetri_pos = position
			self.nowtetri_shape = shape
			self.nowtetri_positions = positions
			return True
		else :
			return False
	def makeRotateShape(self, shape) :
		newShape = []
		for i in range(4) :
			newX = shape[i][1] * (-1)
			newY = shape[i][0]
			newShape.append([newX, newY])
		return newShape
	def RotateTetri(self) :
		if len(self.nowtetri_shape) == 0 : return
		if self.check(self.nowtetri_positions, BLOCK) :
			self.setTetri(self.nowtetri_positions, NONBLOCK)
		else :
			return False
		newShape = self.makeRotateShape(self.nowtetri_shape)
		newPositions = self.shapeToPosition(self.nowtetri_pos, newShape)
		if len(newPositions) == 1 :
			self.setTetri(self.nowtetri_positions, BLOCK)
			return False
		if self.check(newPositions, NONBLOCK) :
			self.nowtetri_positions = newPositions
			self.nowtetri_shape = newShape
			self.setTetri(self.nowtetri_positions, BLOCK)
			return True
		else :
			self.setTetri(self.nowtetri_positions, BLOCK)
			return False
	def move(self, x, y) :
		if not self.check(self.nowtetri_positions, BLOCK) :
			return False
		self.setTetri(self.nowtetri_positions, NONBLOCK)
		newPosition = [x, y]
		newPositions = self.shapeToPosition(newPosition, self.nowtetri_shape)
		if len(newPositions) == 1 :
			self.setTetri(self.nowtetri_positions, BLOCK)
			return False
		if self.check(newPositions, NONBLOCK) :
			self.nowtetri_pos = newPosition
			self.nowtetri_positions = newPositions
			self.setTetri(self.nowtetri_positions, BLOCK)
			return True
		else :
			self.setTetri(self.nowtetri_positions, BLOCK)
			return False

screen = pygame.display.set_mode((360, 660))
clock = pygame.time.Clock()


class System :
	def __init__(self) :
		self.blockSprite = pygame.image.load('Data/Tetris/block.bmp')
		self.nonblockSprite = pygame.image.load('Data/Tetris/nonblock.bmp')
	def printBlock(self,position) :
		screen.blit(self.blockSprite, (position[0], position[1], position[0]+BLOCKSIZE, position[1]+BLOCKSIZE))
	def printNonblock(self, position) :
		screen.blit(self.nonblockSprite, (position[0], position[1], position[0]+BLOCKSIZE, position[1]+BLOCKSIZE))	
	def printScreen(self, tile) :
		for i in range(WIDTH+2) :
			self.printBlock([BLOCKSIZE*i, 0])
			self.printBlock([BLOCKSIZE*i, BLOCKSIZE*(HEIGHT+1)])
		for i in range(HEIGHT+1) :
			self.printBlock([0,BLOCKSIZE*(i+1)])
			self.printBlock([BLOCKSIZE*(WIDTH+1), BLOCKSIZE*(i+1)])
		for x in range(WIDTH) :
			for y in range(HEIGHT) :
				if tile.dat[x][y] == BLOCK :
					self.printBlock([BLOCKSIZE*(x+1), BLOCKSIZE*(y+1)])
				elif tile.dat[x][y] == NONBLOCK :
					self.printNonblock([BLOCKSIZE*(x+1), BLOCKSIZE*(y+1)])
	def checkCompleteLine(self, tile) :
		for i in range(HEIGHT) :
			filled = True
			for j in range(WIDTH) :
				if tile.dat[j][i] == NONBLOCK :
					filled = False
					break
			if filled :
				for k in range(i, 0, -1) :
					for l in range(WIDTH) :
						tile.dat[l][k] = tile.dat[l][k-1]


class SceneTetris(Scene):
	def __init__(self, screen, clock, player):
		Scene.__init__(self, screen, clock, player)
		self.gm = System()
		self.tile = Tile()
		self.tile.makeTetri([5,2], tetri[random.randint(0,6)])
		self.counter = 0

	def Frame(self):
		self.counter += clock.tick(30)
		if self.counter > 1000 :
			if not self.tile.move(self.tile.nowtetri_pos[0], self.tile.nowtetri_pos[1]+1) :
				self.gm.checkCompleteLine(self.tile)
				self.tile.makeTetri([5,2], tetri[random.randint(0,6)])
			self.counter -= 1000
		for event in pygame.event.get() :
			if event.type == KEYDOWN :
				if not hasattr(event, 'key') : continue
				if event.key == K_ESCAPE :
					self.nextSceneState = NEXTSCENE_POP
				if event.key == K_RIGHT :
					self.tile.move(self.tile.nowtetri_pos[0]+1, self.tile.nowtetri_pos[1])
				if event.key == K_LEFT :
					self.tile.move(self.tile.nowtetri_pos[0]-1, self.tile.nowtetri_pos[1])
				if event.key == K_DOWN :
					if not self.tile.move(self.tile.nowtetri_pos[0], self.tile.nowtetri_pos[1]+1) :
						self.gm.checkCompleteLine(self.tile)
						self.tile.makeTetri([5,2], tetri[random.randint(0,6)])
				if event.key == K_UP :
					self.tile.RotateTetri()
				if event.key == K_SPACE :
					while self.tile.move(self.tile.nowtetri_pos[0], self.tile.nowtetri_pos[1]+1) :
						continue
					self.gm.checkCompleteLine(self.tile)
					self.tile.makeTetri([5,2], tetri[random.randint(0,6)])
		screen.fill((0,0,0))
		self.gm.printScreen(self.tile)
		pygame.display.flip()
	def Render(self):
		pass









