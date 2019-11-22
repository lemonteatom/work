import sys
import pygame
from pygame.locals import *

pygame.init()




def main():
    
    num=int(input("num"))
    screenWidht=40*num
    screenHeight=40*num
    SURFACE = pygame.display.set_mode((screenWidht, screenHeight))
    pygame.display.set_caption("title")
    FPSCLOCK = pygame.time.Clock()
    
    #masu = [[0]*num for i in range(num) ]
    ocero = [[0]*num for i in range(num) ]

    for i in range(num):
        for j in range(num):
            #masu[i][j] = (20+40*i, 20+40*j)
            ocero[i][j] = 0

    # white = 1, black = -1
    ocero[num//2-1][num//2-1] = 1
    ocero[num//2-1][num//2] = -1
    ocero[num//2][num//2-1] = -1
    ocero[num//2][num//2] = 1


    white = [255, 255, 255]
    black = [0, 0, 0]
    back = [102,255,51]
    
    flag = 0


    count = 0   
    mousepos = []
    color =1
    while True:
        
        for event  in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                count +=1
                y = event.pos[0]
                x = event.pos[1]

                
                a = y//40
                b = x//40
                flag = 100
                
                flag1 = 0
                flag2 = 0
                flag3 = 0
                flag4 = 0
                flag5 = 0
                flag6 = 0
                flag7 = 0
                flag8 = 0

            if flag == 100 :
                #おいてあるとこ conti
                if ocero[a][b] !=0:
                    continue

                #周りになにもないとこ cont
                # 上に探査
                a1 = a
                b1 = b
                a1 = a1 -1
                if a ==0:
                    flag1 =10
                elif ocero[a1][b1] == 0 or ocero[a1][b1] == ocero[a][b]:
                    flag1 =10

                
                #　下に探査
                a1 = a
                b1 = b
                a1 = a1 +1
                if a == num-1:
                    flag2 =10
                elif ocero[a1][b1] == 0 or ocero[a1][b1] == ocero[a][b]:
                    flag2 =10
                
                # 左に探査
                a1 = a
                b1 = b
                b1 = b1 -1
                if b==0:
                    flag3 =10
                elif ocero[a1][b1] == 0 or ocero[a1][b1] == ocero[a][b]:
                    flag3 =10
                # 右に探査
                a1 = a
                b1 = b
                b1 = b1 +1
                if b==num-1:
                    flag4 =10
                elif ocero[a1][b1] == 0 or ocero[a1][b1] == ocero[a][b]:
                    flag4 =10
                
                # 左下に探査
                a1 = a
                b1 = b
                a1 = a1 -1
                b1 = b1 -1
                if a==0 or b==0:
                    flag5 =10
                elif ocero[a1][b1] == 0 or ocero[a1][b1] == ocero[a][b]:
                    flag5 =10

                # 左上に探査
                a1 = a
                b1 = b
                a1 = a1 +1
                b1 = b1 -1
                if a==num-1 or b==0:
                    flag6 =10
                elif ocero[a1][b1] == 0 or ocero[a1][b1] == ocero[a][b]:
                    flag6 =10

                # 右下に探査
                a1 = a
                b1 = b
                a1 = a1 -1
                b1 = b1 +1
                if a==0 or b ==num-1:
                    flag7 =10
                elif ocero[a1][b1] == 0 or ocero[a1][b1] == ocero[a][b]:
                    flag7 =10

                # 右上に探査
                a1 = a
                b1 = b
                a1 = a1 +1
                b1 = b1 +1
                if a==num-1 or b==num-1:
                    flag8 =10
                elif ocero[a1][b1] == 0 or ocero[a1][b1] == ocero[a][b]:
                    flag8 =10
                
                if flag1==10 and flag2==10 and flag3==10 and flag4 ==10 and flag5==10 and flag6==10 and flag7==10 and flag8 ==10:
                    continue


                #ここから入れ替え

                ocero[a][b] = color
                
                
                # 上に探査
                a1 = a
                b1 = b
                flag = 0
                while  a1 -1>=0 and flag == 0:
                    a1 = a1 -1
                    if ocero[a1][b1] == color:
                        flag = 1
                    elif ocero[a1][b1] == 0:
                        flag =10

                if flag == 1:
                    a2 =a
                    b2 =b
                    replace =0
                    while a2 != a1:
                        ocero[a2][b2] = color
                        a2 = a2 -1
                        replace +=1
                        print("r1")
                if flag !=1 or replace <=1:
                    flag1 =50
                    print("f1")

                    
                #　下に探査
                a1 = a
                b1 = b
                flag = 0
                while  a1 +1 < num and flag == 0:
                    a1 = a1 +1
                    if ocero[a1][b1] == color:
                        flag = 1
                        
                    elif ocero[a1][b1] == 0:
                        flag =10
                

                if flag == 1:
                    a2 =a
                    b2 =b
                    replace =0
                    while a2 != a1:
                        ocero[a2][b2] = color
                        a2 = a2 +1
                        replace +=1
                        print("r2")
                if flag !=1 or replace <=1:
                    flag2 =50
                    print("f2")

                

                # 左に探査
                a1 = a
                b1 = b
                flag = 0
                while  b1 -1>=0 and flag == 0:
                    b1 = b1 -1
                    if ocero[a1][b1] == color:
                        flag = 1
                    elif ocero[a1][b1] == 0:
                        flag =10
                if flag == 1:
                    a2 =a
                    b2 =b
                    replace = 0
                    while b2 != b1:
                        ocero[a2][b2] = color
                        b2 = b2 -1
                        replace += 1
                        print("r3")
                if flag !=1 or replace <=1:
                    flag3 =50
                    print("f3")
                
                
                # 右に探査
                a1 = a
                b1 = b
                flag = 0
                while  b1 + 1 < num and flag == 0:
                    b1 = b1 +1
                    if ocero[a1][b1] == color:
                        flag = 1
                    elif ocero[a1][b1] == 0:
                        flag =10
                if flag == 1:
                    a2 =a
                    b2 =b
                    replace =0
                    while b2 != b1:
                        ocero[a2][b2] = color
                        b2 = b2 +1
                        replace +=1
                        print("r4")
                if flag !=1 or replace <=1:
                    flag4 =50
                    print("f4")
                

                # 左下に探査
                a1 = a
                b1 = b
                flag = 0
                while  a1 -1 >= 0 and b1 -1>= 0 and flag == 0:
                    a1 = a1 -1
                    b1 = b1 -1
                    if ocero[a1][b1] == color:
                        flag = 1
                    elif ocero[a1][b1] == 0:
                        flag =10
                if flag == 1:
                    a2 =a
                    b2 =b
                    replace =0
                    while b2 != b1:
                        ocero[a2][b2] = color
                        a2 = a2 -1
                        b2 = b2 -1
                        replace +=1
                        print("r5")
                    print(replace)
                if flag !=1 or replace <=1:
                    flag5 =50
                    print("F5")

                # 左上に探査
                a1 = a
                b1 = b
                flag = 0
                while  a1 +1 < num and b1 -1>= 0 and flag == 0:
                    a1 = a1 +1
                    b1 = b1 -1
                    if ocero[a1][b1] == color:
                        flag = 1
                    elif ocero[a1][b1] == 0:
                        flag =10
                if flag == 1:
                    a2 =a
                    b2 =b
                    replace =0
                    while b2 != b1:
                        ocero[a2][b2] = color
                        a2 = a2 +1
                        b2 = b2 -1
                        replace +=1
                        print("r6")
                        
                if flag !=1 or replace <=1:
                    flag6 =50
                    print("F6")


                # 右下に探査
                a1 = a
                b1 = b
                flag = 0
                while  a1-1 >= 0 and b1 +1 < num and flag == 0:
                    a1 = a1 -1
                    b1 = b1 +1
                    if ocero[a1][b1] == color:
                        flag = 1
                    elif ocero[a1][b1] == 0:
                        flag =10
                if flag == 1:
                    a2 =a
                    b2 =b
                    replace =0
                    while b2 != b1:
                        ocero[a2][b2] = color
                        a2 = a2 -1
                        b2 = b2 +1
                        replace +=1
                        print("r7")
                if flag !=1 or replace <=1:
                    flag7 =50
                    print("f7")


                # 右上に探査
                a1 = a
                b1 = b
                flag = 0
                while  a1+ 1 < num and b1 +1 < num and flag == 0:
                    a1 = a1 +1
                    b1 = b1 +1
                    if ocero[a1][b1] == color:
                        flag = 1
                    elif ocero[a1][b1] == 0:
                        flag =10
                if flag == 1:
                    a2 =a
                    b2 =b
                    replace =0
                    while b2 != b1:
                        ocero[a2][b2] = color
                        a2 = a2 +1
                        b2 = b2 +1
                        replace +=1
                        print("r8")
                if flag !=1 or replace <=1:
                    flag8 =50
                    print("f8")

                if flag1==50 and flag2==50 and flag3==50 and flag4 ==50 and flag5==50 and flag6==50 and flag7==50 and flag8 ==50:
                    ocero[a][b] = 0
                    continue
                
                    

                color = color* (-1)
        if pressed_keys[K_SPACE]:
            color = color*(-1)
            print("press")

        #勝ち負け判定
        whiteScore =0
        blackScore =0
        for i in range(num):
            for j in range(num):
                if ocero[i][j]==0 :
                    exit
                elif ocero[i][j] ==1:
                    whiteScore +=1
                else:
                    blackScore +=1
        
        SURFACE.fill((102,255,51))

        
        




        for xpos in range(0, 40*num, 40):
            pygame.draw.line(SURFACE, 0xFFFFFF, (xpos, 0), (xpos, 40*num))
        
        for ypos in range(0, 40*nuｍ, 40):
            pygame.draw.line(SURFACE, 0xFFFFFF, (0,ypos), (40*num, ypos))
        
        for i in range(num):
            for j in range(num):
                if ocero[i][j]  >0:
                    pygame.draw.circle(SURFACE, white, (20+40*i, 20+40*j), 20,0)
                    
                elif ocero[i][j] < 0:
                    pygame.draw.circle(SURFACE, black, (20+40*i, 20+40*j), 20,0)
                    
        
        if whiteScore+blackScore== num*num:
            if whiteScore > blackScore:
                win = "White"
            elif whiteScore < blackScore:
                win = "Black"
            else:
                win = "Draw"
            # 文字設定
            gameoverFont = pygame.font.SysFont("Meiryo",3*num)
            gameover = gameoverFont.render(("white:"+ str(whiteScore) + "  black:" + str(blackScore) + "  Winer:"+win),True, (255,0,0) )
            gameoverRect = gameover.get_rect(center = (screenWidht/2, screenHeight/2))

            SURFACE.blit(gameover,gameoverRect)


        


        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()
