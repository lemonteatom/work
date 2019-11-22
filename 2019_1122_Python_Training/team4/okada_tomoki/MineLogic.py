import tkinter
import random
import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN


pygame.init()
SURFACE = pygame.display.set_mode((500,500))
FPSCLOCK = pygame.time.Clock()

masList= []
lineList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lineList1=list(lineList)
lineList2=list(lineList)
lineList3=list(lineList)
lineList4=list(lineList)
lineList5=list(lineList)
lineList6=list(lineList)
lineList7=list(lineList)
lineList8=list(lineList)
lineList9=list(lineList)
lineList10=list(lineList)
lineList11=list(lineList)
lineList12=list(lineList)
lineList13=list(lineList)
lineList14=list(lineList)
lineList15=list(lineList)
lineList16=list(lineList)
lineList17=list(lineList)
lineList18=list(lineList)
lineList19=list(lineList)
lineList20=list(lineList)
lineList21=list(lineList)

masList.append(lineList)
masList.append(lineList1)
masList.append(lineList2)
masList.append(lineList3)
masList.append(lineList4)
masList.append(lineList5)
masList.append(lineList6)
masList.append(lineList7)
masList.append(lineList8)
masList.append(lineList9)
masList.append(lineList10)
masList.append(lineList11)
masList.append(lineList12)
masList.append(lineList13)
masList.append(lineList14)
masList.append(lineList15)
masList.append(lineList16)
masList.append(lineList17)
masList.append(lineList18)
masList.append(lineList19)
masList.append(lineList20)
masList.append(lineList21)

a=0
b=True
while b:
    x=random.randint(1,20)
    y=random.randint(1,20)
    if masList[x][y] == 9:
        a=a-1
    else:
        masList[x][y]=9
        a=a+1
    if a==40:
        b=False

c=1
for i in range(20):
    d=1
    e=0
    for j in range(20):
        if masList[c][d]!=9:
            if masList[c-1][d-1]==9:
                e=e+1
            if masList[c-1][d]==9:
                e=e+1
            if masList[c-1][d+1]==9:
                e=e+1
            if masList[c][d-1]==9:
                e=e+1
            if masList[c][d+1]==9:
                e=e+1
            if masList[c+1][d-1]==9:
                e=e+1
            if masList[c+1][d]==9:
                e=e+1
            if masList[c+1][d+1]==9:
                e=e+1
            masList[c][d]=e
            sysfont = pygame.font.SysFont("Meiryo",10)
            y=str(e)
            z = y.encode("utf-8")
            message = sysfont.render(z,True,(0,150,150))
            x=12*d
            y=12*c+100
            message_rect = message.get_rect(center = (x,y))
            masList[c][d]
    c=c+1



#メインルーチン
mousepos= []

while True:
    
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type ==MOUSEBUTTONDOWN:
            mousepos.append(event.pos)

    SURFACE.fill((150,150,150))
    #縦線
    for xpos in range(0,500, 25):
        pygame.draw.line(SURFACE, 0xFFFFFF,
        (xpos, 100), (xpos, 500))
    #横線
    for ypos in range(100,500,25):
        pygame.draw.line(SURFACE, 0xFFFFFF,
        (0, ypos), (500, ypos))
            
    for pos in mousepos:
        pygame.draw.circle(SURFACE, (255,0,0), pos, 5)
    pygame.display.update()
    FPSCLOCK.tick(100)
    
if __name__ == '__main__':
    main()





