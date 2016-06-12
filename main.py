# -*- coding: utf-8 -*-

import pygame, math, sys
from pygame.locals import *
from SceneMainMenu import *
from SceneMapTest import *
from SceneTetris import *
from SceneAvoider import *
from SceneDodge import *
from SceneMineFinder import *
from SceneRhythm import *
from SceneWorldMap import *
from SceneProlog import *
from SceneClassRoom import *
from SceneEpilog import *
from Player import *

SCREEN_SIZE = (1200,800)

SceneDic = {'MainMenu':SceneMainMenu, 'MapTest':SceneMapTest, 'Tetris':SceneTetris, \
	'Dodge':SceneDodge, 'MineFinder':SceneMineFinder, 'Avoider':SceneAvoider, 'Rhythm':SceneRhythm, \
	'Prolog':SceneProlog, 'WorldMap':SceneWorldMap, 'ClassRoom':SceneClassRoom, 'Epilog':SceneEpilog}
SceneStack = []
if __name__ == '__main__' :
	pygame.init()
	pygame.display.set_caption('ProHanyangEr')
	screen = pygame.display.set_mode(SCREEN_SIZE)
	clock = pygame.time.Clock()
	player = Player()
	nowScene = SceneMainMenu(screen, clock, player)
	while True :
		nowScene.Frame()
		nowScene.Render()
		if nowScene.nextSceneState == NEXTSCENE_POP :
			if len(SceneStack) == 0 :
				pygame.quit()
				sys.exit(0)
			nowScene = SceneStack.pop()
			nowScene.dumpTime = False
		if nowScene.nextScene != nowScene :
			if nowScene.nextSceneState == NEXTSCENE_ERASE :
				nowScene = SceneDic[nowScene.nextScene](screen, clock, player)
			elif nowScene.nextSceneState == NEXTSCENE_STACK :
				nextScene = nowScene.nextScene
				nowScene.NextSceneInit()
				SceneStack.append(nowScene)
				nowScene = SceneDic[nextScene](screen, clock, player)
		for event in pygame.event.get() :
			if event.type == QUIT :
				pygame.quit()
				exit(0)	