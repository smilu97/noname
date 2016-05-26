import math, sys, os

outlist = []
time = 0
def makeRoundCurtain(btype, pos, angle, num, radius=40) :
	theta = angle[0]
	deltaAngle = (angle[1]-angle[0])/num
	while theta <= angle[1] :
		outlist.append([time, btype, pos[0] + radius*math.cos(theta), pos[1] + radius*math.sin(theta), theta])
		theta += deltaAngle

def save() :
	outstring = ''
	for li in outlist :
		for ch in li :
			outstring += str(ch) + ' '
		outstring = outstring[:-1]
		outstring += '\n'
	outstring = outstring[:-1]
	ofile = open('Data/BulletScenario/output.txt', 'w')
	ofile.write(outstring)
	ofile.close()

if __name__ == '__main__' :
	############# 0
	time = 0
	for x in range(0, 1600, 100) :
		outlist.append([time, 1, x, 0, math.pi/2])
	############# 1000
	time = 1000
	makeRoundCurtain(1, (600, 100), (0, math.pi*2), 20, 40)
	############# 2000
	time = 2000
	makeRoundCurtain(1, (200, 100), (0, math.pi), 10, 40)
	makeRoundCurtain(1, (1000, 100), (0, math.pi), 10, 40)
	# End
	save()



