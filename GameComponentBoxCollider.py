import pygame, math, sys, random
from pygame.locals import *
from GameComponent import *

class GameComponentBoxCollider(GameComponent):
	def __init__(self, owner, rect=np.array((0.0,0.0,0.0,0.0))):
		GameComponent.__init__(self, owner)
		self.index = len(self.owner.owner.colliderList)
		self.owner.owner.colliderList.append(self)
		self.rect = np.array(rect)
		self.colliderType = 'box'
		self.static = False
	def kill(self) :
		cList = self.owner.owner.colliderList
		for compo in cList[self.index+1:] :
			compo.index -= 1
		del cList[self.index]
	def GetHowColliding(self, delta, otherCollider) :
		epsilon = 0.0000001
		if otherCollider.colliderType == 'box' :
			other = otherCollider.GetWorldRect()
			prev = (other[0]-delta[0], other[1]-delta[1], other[2]-delta[0], other[3]-delta[1])
			mine = self.GetWorldRect()
			isDown = isRight = False
			if mine[3]-epsilon <= other[1] : # Down
				return False
			if other[3] <= mine[1]+epsilon : # Up
				return False
			if mine[2]-epsilon <= other[0] : # Right
				return False
			if other[2] <= mine[0] + epsilon : # Left 
				return False
			rdx = rdy = False
			if mine[3] <= prev[1] : # Down
				rdy = other[1] - mine[3]
			elif prev[3] <= mine[1] : # Up
				rdy = other[3] - mine[1]	
			if mine[2] <= prev[0] : # Right
				rdx = other[0] - mine[2]
			elif prev[2] <= mine[0] : # Left 
				rdx = other[2] - mine[0]
			if rdx != False :
				mdx = other[0] - prev[0]
				ddx = rdx / mdx
				ddx = 1 - ddx
			if rdy != False :
				mdy = other[1] - prev[1]
				ddy = rdy / mdy
				ddy = 1 - ddy
			if rdx == False and rdy != False :
				return (ddy-epsilon, 1)
			if rdx != False and rdy == False :
				return (ddx-epsilon, 0)
			if rdx == False and rdy == False :
				print mine
				print prev
				print other
			if ddx > ddy :
				return (ddx-epsilon, 0)
			else :
				return (ddy-epsilon, 1)	
		elif otherCollider.colliderType == 'circle' :
			other = otherCollider.GetWorldPosition()
			prev = (other[0]-delta[0], other[1]-delta[1])
			mine = self.GetWorldRect()
			other_radius = otherCollider.radius
			if mine[2]-epsilon <= other[0]-other_radius : # Right
				return False
			if mine[0]+epsilon > other[0]+other_radius : # Left
				return False
			if mine[3]-epsilon <= other[1]-other_radius : # Down
				return False
			if mine[1]+epsilon > other[0]+other_radius : # Up
				return False
			if abs(other[0] - mine[0]) < abs(other[0] - mine[2]) :
				bx = mine[0]
			else :
				bx = mine[2]
			if abs(other[1] - mine[1]) < abs(other[1] - mine[3]) :
				by = mine[1]
			else :
				by = mine[3]
			dx = bx - other[0]
			dy = by - other[1]
			dl = other_radius - math.sqrt(dx**2 + dy**2)
			if 0 <= dl :
				tangent = delta[1]/delta[0]
				A = 1 + tangent**2
				B = 2*(prev[0]-other[0] + tangent*(prev[1]-other[1]))
				C = (prev[0]-other[0])**2 + (prev[1]-other[1])**2 - other_radius**2
				S = math.sqrt(B**2 - 4*A*C)
				ans_m = (-B - S) / (2*A)
				ans_M = (-B + S) / (2*A)
				if abs(ans_m) < abs(ans_M) :
					ans = ans_m
				else :
					ans = ans_M
				return ans/delta[0]
			return False
	def GetIsColliding(self, otherCollider) :
		epsilon = 0.0000001
		if otherCollider.colliderType == 'box' :
			mine = self.GetWorldRect()
			other = otherCollider.GetWorldRect()
			isDown = isRight = False
			if mine[3]-epsilon <= other[1] : # Down
				return False
			if other[3] <= mine[1]+epsilon : # Up
				return False
			if mine[2]-epsilon <= other[0] : # Right
				return False
			if other[2] <= mine[0] + epsilon : # Left 
				return False
			return True
		elif otherCollider.colliderType == 'circle' :
			other = otherCollider.GetWorldPosition()
			mine = self.GetWorldRect()
			other_radius = otherCollider.radius
			if mine[2]-epsilon <= other[0]-other_radius : # Right
				return False
			if mine[0]+epsilon > other[0]+other_radius : # Left
				return False
			if mine[3]-epsilon <= other[1]-other_radius : # Down
				return False
			if mine[1]+epsilon > other[1]+other_radius : # Up
				return False
			return True
	def Frame(self,dt):
		pass
	def Render(self):
		pass