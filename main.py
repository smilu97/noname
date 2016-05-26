import pygame, math, sys
from pygame.locals import *
from SceneMainMenu import *
from SceneMapTest import *
from SceneTetris import *
from SceneAvoider import *
from SceneDodge import *
from SceneMineFinder import *
from Player import *

SceneDic = {'MainMenu':SceneMainMenu, 'MapTest':SceneMapTest, 'Tetris':SceneTetris, \
	'Dodge':SceneDodge, 'MineFinder':SceneMineFinder}
SceneStack = []
if __name__ == '__main__' :
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	clock = pygame.time.Clock()
	player = Player()
	nowScene = SceneMainMenu(screen, clock, player)
	while True :
		nowScene.Frame()
		nowScene.Render()
		if nowScene.nextSceneState == NEXTSCENE_POP :
			if len(SceneStack) == 0 :
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