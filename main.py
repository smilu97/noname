import pygame, math, sys
from pygame.locals import *
from SceneMainMenu import *

if __name__ == '__main__' :
	pygame.init()
	screen = pygame.display.set_mode((1000,500))
	clock = pygame.time.Clock()
	nowScene = SceneMainMenu(screen, clock)
	while True :
		nowScene.Frame()
		nowScene.Render()
