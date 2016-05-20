import math, sys

def RotatePosition(position, degree) :
	nx = position[0] * math.cos(degree) - position[1] * math.sin(degree)
	ny = position[0] * math.sin(degree) + position[1] * math.cos(degree)
	return (nx, ny)

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
		if type(obj) == type(dict()) :
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
			dlist .append(obj)
	return dlist