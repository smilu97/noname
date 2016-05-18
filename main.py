import pygame, math, sys
from pygame.locals import *
from SceneMainMenu import *
from SceneMapTest import *

SceneDic = {'MainMenu':SceneMainMenu, 'MapTest':SceneMapTest}

if __name__ == '__main__' :
	pygame.init()
	screen = pygame.display.set_mode((1000,500))
	clock = pygame.time.Clock()
	nowScene = SceneMainMenu(screen, clock)
	while True :
		nowScene.Frame()
		nowScene.Render()
		if nowScene.nextScene != nowScene :
			nowScene = SceneDic[nowScene.nextScene](screen, clock)
			