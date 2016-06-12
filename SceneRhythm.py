# -*- coding: utf-8 -*-

import pygame, math, sys
from pygame.locals import *
from Scene import *

class SceneRhythm(Scene):
    def __init__(self, screen, clock, player):
        Scene.__init__(self, screen, clock, player)
        self.note = [(3000.0*i,(i%4)+1) for i in range(100)]
        self.noteType = []
        self.count = 0
        self.pos = []
        self.uparrowImage = pygame.image.load('Data/arrow/up.png')
        self.downarrowImage = pygame.image.load('Data/arrow/down.png')
        self.rightarrowImage = pygame.image.load('Data/arrow/right.png')
        self.leftarrowImage = pygame.image.load('Data/arrow/left.png')
        self.font = pygame.font.Font('ttf/NanumGothic.ttf', 25)
        self.point = 0
    def Frame(self) :
        dt = self.clock.tick(FRAME_RATE)
        self.count += dt
        key = pygame.key.get_pressed() # 키들이 눌려있는지 저장하는 Dictionary
        self.pos = []
        self.noteType = []
        for i in range(len(self.note)) :
            self.pos.append((self.note[i][0]-self.count)/3000*1000)
            self.noteType.append(self.note[i][1])
            if self.pos[-1] > 1000 :
                break
        popcount = 0
        for i in self.pos :
            if i < -3000 :
                popcount += 1
            else :
                break
        self.note = self.note[popcount:] 
        for event in pygame.event.get() :
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    self.nextSceneState = NEXTSCENE_POP
                elif event.key == K_RIGHT :
                    finded = False
                    for i in range(popcount, len(self.pos)) :
                        if  -40 < self.pos[i] and self.pos[i] < 0 and self.noteType[i] == 2 :
                            del self.note[i]
                            self.point += 10
                            finded = True
                            break
                    if finded == False :
                        self.point -= 10
                elif event.key == K_LEFT :
                    finded = False
                    for i in range(popcount, len(self.pos)) :
                        if  -40 < self.pos[i] and self.pos[i] < 0 and self.noteType[i] == 4 :
                            del self.note[i]
                            self.point += 10
                            finded = True
                            break
                    if finded == False :
                        self.point -= 10
                elif event.key == K_UP :
                    finded = False
                    for i in range(popcount, len(self.pos)) :
                        if  -40 < self.pos[i] and self.pos[i] < 0 and self.noteType[i] == 1 :
                            del self.note[i]
                            self.point += 10
                            finded = True
                            break
                    if finded == False :
                        self.point -= 10
                elif event.key == K_DOWN :
                    finded = False
                    for i in range(popcount, len(self.pos)) :
                        if  -40 < self.pos[i] and self.pos[i] < 0 and self.noteType[i] == 3 :
                            del self.note[i]
                            self.point += 10
                            finded = True
                            break
                    if finded == False :
                        self.point -= 10
                    
            elif event.type == MOUSEBUTTONDOWN :
                mousepos = event.pos # 마우스 커서 위치
                if event.button == 1:
                    # TODO : 마우스 왼쪽 버튼 입력시 (pass는 지워도 됨)
                    pass
                elif event.button == 3:
                    # TODO : 마우스 오른쪽 버튼 입력시
                    pass
    def Render(self) : 
        self.screen.fill((0,0,0))
        for i in range(len(self.pos)) :
            if self.noteType[i] == 1 :
                self.screen.blit(self.uparrowImage, (self.pos[i],0))
            if self.noteType[i] == 2 :
                self.screen.blit(self.rightarrowImage, (self.pos[i],0))
            if self.noteType[i] == 3 :
                self.screen.blit(self.downarrowImage, (self.pos[i],0))
            if self.noteType[i] == 4 :
                self.screen.blit(self.leftarrowImage, (self.pos[i],0))
        self.screen.blit(self.font.render('score : %d' % self.point, True, (255,255,255)), (0,50))
        # TODO : screen.blit등을 이용해서 여기서 렌더링
        pygame.display.flip()