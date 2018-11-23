#!/usr/bin/env python



import pygame,datetime
from pygame import *

hits=0

class noteline():

    def __init__(self, line):
            self.font = pygame.font.SysFont('Arial', 25)
            self.noli = pygame.surface(len(line),100)
            self.notes = []
            c = 0
            for n in line:
                self.notes.append(n)
                self.noli.blit(self.font.render(n, True, (255,0,0)), (c, 50))
                c = c + 10

    def getNoLi():
        return self.noli

    def setNoteColor(note, color):
        self.notes[note]
        self.noli.blit(self.font.render(self.notes[note],True,color),(note*10,50))
        pygame.display.update()

def hit():
    global hits
    hits = hits + 1


def miss(note):
    notelinesurface.setNoteColor(note,(255,0,0))

def reset():
    global lapresult
    results.append(lapresult)
    lapresult = []
    i = 0
    lapstart = pygame.time.get_ticks

def storeResult(result):
    resultFile = open(datetime.datetime.now().strftime("ph-%Y-%m-%d_%H:%M:%S"),"w")
    for line in result:
        for inp in line:
            resultFile.write(str(inp[0]) + "," + str(inp[1]) + "," + str(inp[2]) + "\n")
        resultFile.write("#END_OF_LAP")
    resultFile.close()

notes = [3,3,2,1,5,3,3,2,3,1,2,3,4,2,5,4,3,3,2,1,2,1]
hm = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
i=0

lapstart=0
lapresult=[]

clock = pygame.time.Clock()
pygame.init()

mixer.init()
note_c2 = mixer.Sound("Piano.mf.C2.aiff")
note_d2 = mixer.Sound("Piano.mf.D2.aiff")
note_e2 = mixer.Sound("Piano.mf.E2.aiff")
note_f2 = mixer.Sound("Piano.mf.F2.aiff")
note_g2 = mixer.Sound("Piano.mf.G2.aiff")

width, height = 600,400
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Piano Hero')
pygame.font.init()
font = pygame.font.SysFont('helvetica',20)
hittextsurface = font.render('0',False,(0,200,0))
# noteline1 = noteline(notes)
pygame.draw.rect(screen,(255,0,255),(50,50,300,100))
screen.fill((255,255,255))
c = 0
for n in notes:
    screen.blit(font.render(str(n), True, (0,0,0)), (50+c, 50))
    c = c + 20
# screen.blit(notelinesurface)
# screen.blit(hittextsurface,(10,200))
pygame.display.update()

results = []
run = True
while run:
    for event in pygame.event.get():
        if i == len(notes) - 1:
            reset()
        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                run = False
            elif event.key == K_UP:
                lapresult.append((False,pygame.time.get_ticks() - lapstart,-1))
                note_d2.play()
                if notes[i] == 2:
                    lapresult[i] = (True,lapresult[i][1],lapresult[i][2])
                    hits = hits + 1
                    hm[i] = True
                #     i = i + 1
                # else:
                #     i = i + 1
            elif event.key == K_DOWN:
                lapresult.append((False,pygame.time.get_ticks() - lapstart,-1))
                note_f2.play()
                if notes[i] == 4:
                    lapresult[i] = (True,lapresult[i][1],lapresult[i][2])
                    hits = hits + 1
                    hm[i] = True
                #     i = i + 1
                # else:
                #     i = i + 1
            elif event.key == K_RIGHT:
                lapresult.append((False,pygame.time.get_ticks() - lapstart,-1))
                note_e2.play()
                if notes[i] == 3:
                    lapresult[i] = (True,lapresult[i][1],lapresult[i][2])
                    hits = hits + 1
                    hm[i] = True
                #     i = i + 1
                # else:
                #     i = i + 1
            elif event.key == K_LEFT:
                lapresult.append((False,pygame.time.get_ticks() - lapstart,-1))
                note_c2.play()
                if notes[i] == 1:
                    lapresult[i] = (True,lapresult[i][1],lapresult[i][2])
                    hits = hits + 1
                    hm[i] = True
                #     i = i + 1
                # else:
                #     i = i + 1
            elif event.key == K_SPACE:
                lapresult.append((False,pygame.time.get_ticks() - lapstart,-1))
                note_g2.play()
                if notes[i] == 5:
                    lapresult[i] = (True,lapresult[i][1],lapresult[i][2])
                    hits = hits + 1
                    hm[i] = True
                #     i = i + 1
                # else:
                #     i = i + 1
            elif event.key == K_g:
                lapresult.append((False,pygame.time.get_ticks() - lapstart,-1))
                note_g2.play()
                if notes[i] == 6:
                    lapresult[i] = (True,lapresult[i][1],lapresult[i][2])
                    hits = hits + 1
                    hm[i] = True
                #     i = i + 1
                # else:
                #     i = i + 1
        elif event.type == pygame.KEYUP:
            print(i)
            if i < len(lapresult):
                lapresult[i] = (lapresult[i][0],lapresult[i][1],pygame.time.get_ticks() - lapresult[i][1])
            if event.key == K_UP:
                i = i + 1
            elif event.key == K_DOWN:
                i = i + 1
            elif event.key == K_RIGHT:
                i = i + 1
            elif event.key == K_LEFT:
                i = i + 1
            elif event.key == K_SPACE:
                i = i + 1
            elif event.key == K_g:
                i = i + 1
        screen.fill((255,255,255))
        hittextsurface = font.render(str(hits),False,(0,200,0))
        c = 0
        for n in notes:
            color = (0,0,0)
            if c <= 20 * i:
                color = (255,0,0)
                if hm[i] == True:
                    color = (0,255,0)
            screen.blit(font.render(str(n), True, color), (50+c, 50))
            c = c + 20
        screen.blit(hittextsurface,(0,0))
        pygame.display.update()
results.append(lapresult)
storeResult(results)
exit()
