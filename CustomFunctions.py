import math, sys
import numpy as np

FRAME_RATE = 60

def RotatePosition(position, degree) :
	cosValue = math.cos(degree)
	sinValue = math.sin(degree)
	rmat = np.array([[cosValue, -sinValue],[sinValue, cosValue]])
	return np.dot(rmat, position)

def FrameAll(objs, dt) :
	for obj in objs :
		if type(obj) == type(list()) :
			FrameAll(obj, dt)
		elif type(obj) == type(dict()) :
			FrameAll(obj.values(), dt)
		else :
			obj.Frame(dt)
def RenderAll(objs) :
	for obj in objs :
		if type(obj) == type(list()) :
			RenderAll(obj)
		elif type(obj) == type(dict()) :
			RenderAll(obj.values())
		else :
			obj.Render()
def DecomposeList(li) :
	dlist = []
	for obj in li :
		if type(obj) == type(list()) :
			dlist += DecomposeList(obj)
		if type(obj) == type(dict()) :
			dlist += DecomposeList(obj.values())
		else :
			dlist.append(obj)
	return dlist
def RerangeAngle(angle) :
	while angle > math.pi :
		angle -= 2*math.pi
	while angle < -math.pi :
		angle += 2*math.pi
	return angle