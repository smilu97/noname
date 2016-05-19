import pygame, math, sys
from pygame.locals import *
from GameComponent import *

class GameComponentBoxCollider(GameComponent):
	def __init__(self, owner, rect=(0.0,0.0,0.0,0.0)):
		GameComponent.__init__(self, owner)
		self.rect = rect
		self.colliderType = 'box'
	def GetHowColliding(self, prevRect, otherRect) :
		epsilon = 0.001
		myRect = self.GetWorldRect()
		isDown = isRight = False
		if myRect[3] <= otherRect[1] : # Down
			return False
		if otherRect[3] <= myRect[1] : # Up
			return False
		if myRect[2] <= otherRect[0] : # Right
			return False
		if otherRect[2] <= myRect[0] : # Left 
			return False
		rdx = rdy = False
		if myRect[3] <= prevRect[1] : # Down
			rdy = otherRect[1] - myRect[3]
		elif prevRect[3] <= myRect[1] : # Up
			rdy = otherRect[3] - myRect[1]	
		if myRect[2] <= prevRect[0] : # Right
			rdx = otherRect[0] - myRect[2]
		elif prevRect[2] <= myRect[0] : # Left 
			rdx = otherRect[2] - myRect[0]
		if rdx != False :
			mdx = otherRect[0] - prevRect[0]
			ddx = mdx / rdx
			ddx = 1 - ddx
		if rdy != False :
			mdy = otherRect[1] - prevRect[1]
			ddy = mdy / rdy
			ddy = 1 - ddy
		if rdx == False and rdy != False :
			return (ddy-epsilon, 1)
		if rdx != False and rdy == False :
			return (ddx-epsilon, 0)
		if ddx > ddy :
			return (ddx-epsilon, 0)
		else :
			return (ddy-epsilon, 1)		
	def Frame(self,dt):
		pass
	def Render(self):
		pass