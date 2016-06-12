import math, sys, os, random
import numpy as np

outlist = []
time = 0

def save() :
	outstring = ''
	for li in outlist :
		for ch in li :
			outstring += str(ch) + ' '
		outstring = outstring[:-1]
		outstring += '\n'
	outstring = outstring[:-1]
	ofile = open('Data/AvoidScenario/output.txt', 'w')
	ofile.write(outstring)
	ofile.close()

if __name__ == '__main__' :
	############# 0
	time = 0
	for x in range(410, 800, 70) :
		outlist.append([time, 1, x, 210, math.pi/2])
	############ 1000~10000
	for tm in np.arange(1000, 10001, 500) :
		time = tm
		makeRoundCurtain(1, (random.randint(400,800), random.randint(200,600)), (0, math.pi*2), 10, 40)
	############ 10000~20000
	for tm in np.arange(10000, 20000, 500) :
		time = tm
		for i in range(5) :
			outlist.append([time, 0, random.randint(400,800), 205, math.pi/2])
	
	# End
	save()



