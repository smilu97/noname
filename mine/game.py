import pygame, math, sys, random
from pygame.locals import* 

import random


def settile(tile):
    count = 0
    while count<10:   #setmine
        ranminea = random.randint(1,10)
        ranmineb = random.randint(1,10)
        if tile[ranminea][ranmineb] != mine:
            tile[ranminea][ranmineb] = mine

        if tile[ranminea][ranmineb] == mine :
            while True :
                ranminea = random.randint(1,10)
                ranmineb = random.randint(1,10)
                if tile[ranminea][ranmineb] != mine:
                    tile[ranminea][ranmineb] = mine
                    break

    for a in range(0,11): #empty tile
        for b in range(0,11):
            if tile[a][b] != mine :
                tile[a][b] == 0

    return tile




def countcheck(tile[a][b]) :
    clickC = 0
    if tile[a][b] == nothing :
        if tile[a-1][b-1] == mine:
            clickC += 1  # 1,3
        if tile[a-1][b] == mine:
            clickC += 1  # 2,3
        if tile[a-1][b+1] == mine:
            clickC += 1  # 3,3
        if tile[a][b-1] == mine:
            clickC += 1  # 1,2
        if tile[a][b+1] == mine:
            clickC += 1   # 3,2
        if tile[a+1][b-1] == mine:
            clickC += 1  #1,1
        if tile[a+1][b] == mine:
            clickC += 1 #1,2
        if tile[a+1][b+1] == mine:
            clickC += 1   #1,3

    if tile[a][b] == mine :
        clickC = mine

    tile[a][b] = clickC

    return tile[a][b]

            # around number


def check(tile[a][b]):
    countcheck(tile[a][b])
    if countcheck(tile[a][b]) == 0 :
        dx=0
        dy=0
        while True :
            countcheck(tile[a-dx][b-dy])  #first check, fourth
            if countcheck(tile[a-dx][b-dy]) != 0 :  # first check
                break
            if countcheck(tile[a-dx][b-dy]) == 0 :   #first check
                while True :  #second check
                    dx = 0
                    dy = 0
                    countcheck(tile[a-dx][b-dy])
                    if countcheck(tile[a-dx][b-dy]) != 0:
                        break
                    if b-dy == 0 :
                        break
                    dy += 1

                while True :  #third check
                    dx = 0
                    dy = 0
                    countcheck(tile[a-dx][b-dy])
                    if countcheck(tile[a-dx][b-dy]) != 0:
                        break
                    if b-dy == 11 :
                        break
                    dy -= 1

            if a-dx == 0 :
                break

            dx += 1


        dx=0
        dy=0

        while True :
            countcheck(tile[a-dx][b-dy])  #first check, fifth
            if countcheck(tile[a-dx][b-dy]) != 0 :  # first check
                break
            if countcheck(tile[a-dx][b-dy]) == 0 :   #first check
                while True :  #second check
                    dx = 0
                    dy = 0
                    countcheck(tile[a-dx][b-dy])
                    if countcheck(tile[a-dx][b-dy]) != 0:
                        break
                    if b-dy == 0 :
                        break
                    dy += 1

                while True :  #third check
                    dx = 0
                    dy = 0
                    countcheck(tile[a-dx][b-dy])
                    if countcheck(tile[a-dx][b-dy]) != 0:
                        break
                    if b-dy == 11 :
                        break
                    dy -= 1

            if a-dx == 11 :
                break

            dx -= 1

    return tile

SCREEN_SIZE	= (1000,500)
FRAME_RATE = 60
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

tile = []

while True :
	clock.tick(FRAME_RATE)
	
	key = pygame.key.get_pressed()
	# 키들이 눌려있는지 저장하는 Dictionary

	for event in pygame.event.get():
		if event.type == KEYDOWN
			if event.key == 
			if event.key == K_ESCAPE :
				sys.exit(0)
		elif event.type == MOUSEBOTTONDOWN :
			pos = ecent.pos
			if event.botton == 1:
				pass
			elif event.botton == 3:
				pass
	screen.fill((0,0,0))
	
			
