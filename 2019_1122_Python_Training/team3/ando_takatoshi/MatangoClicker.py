import sys
import pygame
import random
from pygame.locals import QUIT, MOUSEBUTTONDOWN, \
        KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

#初期設定
plevel = 1
click = 0
coler = []
bossmatango = 0
bossclick = 0
hevenclick = 0
godclick = 0
initflag = 0
redm = "???"
greenm = "???"
bluem = "???"
whitem = "???"
blackm = "???"
#初期設定変数

pygame.init()
SURFACE = pygame.display.set_mode((800,600))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("MatangoClicker")

def story():
    bigfont = pygame.font.SysFont("Meiryo",80)
    gamefont = pygame.font.SysFont("Meiryo",40)
    mouseflag = 0
    #global宣言
    global initflag
    global plevel
    global click
    global coler
    global bossmatango
    global bossclick 
    global hevenclick
    global godclick
    global redm
    global greenm
    global bluem
    global whitem
    global blackm
    while True:
        SURFACE.fill((255,255,255))
        maze = pygame.image.load("maze1.png")
        SURFACE.blit(maze,(0,0))
        
        #表示メッセージ管理
        gamesmess = gamefont.render("Blue START & Red COAL       coler:", True, (255,255,255))
        SURFACE.blit(gamesmess, (20,50))

        for event in pygame.event.get():
            mouseh = pygame.mouse.get_pos()
            getcol = SURFACE.get_at(mouseh)
            gamesmess = gamefont.render("Blue START & Red COAL       coler:" + str(getcol), True, (255,255,255))
            SURFACE.blit(gamesmess, (20,50))
            if mouseflag == 1:
                if getcol == (1,1,1):
                    SURFACE.fill((255,1,1))
                    click = 0
                    main()
                elif getcol == (255,1,1):
                    click = click*2
                    main()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN: 
                if getcol == (1,1,255):
                    mouseflag = 1

            elif event.type == KEYDOWN:
                if event.key == K_LEFT :
                    main()
        
        pygame.display.update()
        FPSCLOCK.tick(60)


#実績画面用メソッド
def games():
    bigfont = pygame.font.SysFont("Meiryo",80)
    gamefont = pygame.font.SysFont("Meiryo",40)
    #global宣言
    global initflag
    global plevel
    global click
    global coler
    global bossmatango
    global bossclick 
    global hevenclick
    global godclick
    global redm
    global greenm
    global bluem
    global whitem
    global blackm

    massage2 = gamefont.render("", True, (255,255,255))
    massage3 = gamefont.render("", True, (255,255,255))
    massage4 = gamefont.render("", True, (255,255,255))
    massage5 = gamefont.render("", True, (255,255,255))

    while True:
        SURFACE.fill((50,50,50))
        
        #表示メッセージ管理
        gamesmess = bigfont.render("Achievements", True, (255,255,255))
        massage2 = gamefont.render("Player Level: " + str(plevel), True, (255,255,255))
        massage3 = gamefont.render("Rare Matango: " + redm +" : "+ greenm +" : "+ bluem +" : "+ whitem +" : "+ blackm, True, (255,255,255))
        
        if bossmatango == 0:
            massage4 = gamefont.render("Buy Matango: None", True, (255,255,255))
            massage5 = gamefont.render("Press Right: GameWindow", True, (255,0,255))
        elif bossmatango == 1:
            massage4 = gamefont.render("Buy Matango: BossMatango", True, (255,255,255))
            massage5 = gamefont.render("Press Right: GameWindow", True, (255,0,255))
        elif bossmatango == 2:
            massage4 = gamefont.render("Buy Matango: BossMatango & HevenMatango", True, (255,255,255))
            massage5 = gamefont.render("Press Right: GameWindow", True, (255,0,255))
        elif bossmatango == 3:
            massage4 = gamefont.render("BossMatango & HevenMatango & God_Matango", True, (255,255,255))
            massage5 = bigfont.render("Thanks for Playing!!!", True, (255,30,30))
        #表示メッセージ管理

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT :
                    main()


        SURFACE.blit(gamesmess, (20,50))
        SURFACE.blit(massage2,(40,180))
        SURFACE.blit(massage3,(40,260))
        SURFACE.blit(massage4,(40,340))
        SURFACE.blit(massage5,(100,450))

        pygame.display.update()
        FPSCLOCK.tick(10)


def main():

    #初期設定
    sysfont = pygame.font.SysFont("Meiryo",50)
    infont = pygame.font.SysFont("Meiryo",40)
    #global宣言
    global initflag
    global plevel
    global click
    global coler
    global bossmatango
    global bossclick 
    global hevenclick
    global godclick
    global redm
    global greenm
    global bluem
    global whitem
    global blackm

    if initflag == 0:
        #プレイヤーレベル
        plevel = 1
        #クリック数フォント
        click = 0
        #メインルーチン
        coler = []
        bossmatango = 0
        bossclick = 0
        hevenclick = 0
        godclick = 0
        initflag += 1
    
    clicknum = sysfont.render(str(click), True, (0,0,0))
    massage2 = sysfont.render("", True, (255,255,255))
    massage3 = sysfont.render("", True, (255,255,255))
    massage4 = sysfont.render("", True, (255,255,255))
    massage5 = sysfont.render("", True, (255,255,255))

    while True:
        SURFACE.fill((255,255,255))
        

        #自動化機器購入用メッセージ
        if bossmatango == 0:
            massage4 = infont.render("PRESS UP = BUY BossMatango - 500 matango ", True, (0,0,0))
            massage5 = infont.render("PRESS RIGHT: Archivements", True, (0,0,0))
        elif bossmatango == 1:
            massage5 = infont.render("BossMatango is Here ", True, (0,0,0))
            massage4 = infont.render("PRESS UP = BUY HevenMatango - 20000 matango ", True, (0,0,0))
            bossclick +=1
        elif bossmatango == 2:
            massage5 = infont.render("HevenMatango is Here ", True, (0,0,0))
            massage4 = infont.render("PRESS UP = BUY GOD_Matango - 777777 matango ", True, (0,0,0))
            hevenclick +=3
        elif bossmatango == 3:
            massage5 = infont.render("God_Matango is Here ", True, (0,0,0))
            massage4 = infont.render("Sorry.You are god.", True, (0,0,0))
            godclick +=1
        
        if bossclick >= 2 :
            click +=7
            clicknum = sysfont.render(str(click), True, (0,0,0))
            bossclick = 0

        if hevenclick >= 3 :
            click +=77
            clicknum = sysfont.render(str(click), True, (0,0,0))
            hevenclick = 0
        
        if godclick >= 4 :
            click +=77777
            clicknum = sysfont.render(str(click), True, (0,0,0))
            godclick = 0


        #LEVEL UP用メッセージ
        if bossmatango == 0:
            if click >= plevel*100 :
                massage3 = infont.render("PRESS DOWN = +CLICK LEVEL UP! -half matango", True, (255,0,0))
            else:
                massage3 = sysfont.render("more click!", True, (255,0,0))
        elif bossmatango == 1:
            if click >= plevel*70 :
                massage3 = infont.render("PRESS DOWN = +CLICK LEVEL UP! -half matango", True, (255,0,0))
            else:
                massage3 = sysfont.render("more click!", True, (255,0,0))
        elif bossmatango == 2:
            if click >= plevel*40 :
                massage3 = infont.render("PRESS DOWN = +CLICK LEVEL UP! -half matango", True, (255,0,0))
            else:
                massage3 = sysfont.render("more click!", True, (255,0,0))
        elif bossmatango == 3:
            if  click >= plevel*50000 :
                massage3 = infont.render("PRESS DOWN = +CLICK LEVEL UP!", True, (255,0,0))
            else:
                massage3 = sysfont.render("more click!", True, (255,0,0))
        #LEVELUP用メッセージ
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN: 
                
                a = random.randint(1,255)
                b = random.randint(1,255)
                c = random.randint(1,255)
                coler.append([event.pos, a, b, c])

                #表示メッセージ
                if a > 245 and b < 12 and c < 12:
                    makedm = str(("Red Matango!",(a,b,c),"rankSS"))
                    redm = "RED"
                elif a < 12 and b > 245 and c < 12:
                    makedm = str(("Green Matango!",(a,b,c),"rankSS"))
                    greenm = "GREEN"
                elif a < 12 and b < 12 and c > 245:
                    makedm = str(("Blue Matango!",(a,b,c),"rankSS"))
                    bluem = "BLUE"
                elif a > 235 and b > 235 and c > 235:
                    makedm = str(("White Matango!",(a,b,c),"rankA"))
                    whitem = "WHITE"
                elif a < 25 and b < 25 and c < 25:
                    makedm = str(("Black Matango!",(a,b,c),"rankB"))
                    blackm = "BLACK"
                else:
                    makedm = str(("Matango was born!",(a,b,c),"rankC"))

                massage2 = sysfont.render(makedm, True, (a,b,c))
                #表示メッセージ

                if bossmatango == 0:
                    click += plevel
                if bossmatango == 1:
                    click += plevel*2
                if bossmatango == 2:
                    click += plevel*10
                if bossmatango == 3:
                    click += plevel**2

                clicknum = sysfont.render(str(click), True, (0,0,0))
                #押されているキーをチェック (単押しVer)
            elif event.type == KEYDOWN:
                if event.key == K_DOWN :
                    if bossmatango == 0:
                        if click >= plevel*100:
                            click -= plevel*100
                            plevel +=1
                            del coler[::2]
                    if bossmatango == 1:
                        if click >= plevel*70:
                            click -= plevel*70
                            plevel +=1
                            del coler[::2]
                    if bossmatango == 2:
                        if click >= plevel*40:
                            click -= plevel*40
                            plevel +=1
                            del coler[::2]
                    if bossmatango == 3:
                        if click >= plevel*50000:
                            click -= plevel*50000
                            plevel +=19
                            del coler[::1]

                elif event.key == K_UP :
                    if bossmatango == 0:
                        if click >= 500:
                            click -= 500
                            bossmatango = 1
                            SURFACE.fill((255,0,0))
                            del coler[::1]
                    if bossmatango == 1:
                        if click >= 20000:
                            click -= 20000
                            bossmatango = 2
                            SURFACE.fill((0,255,0))
                            del coler[::1]
                    if bossmatango == 2:
                        if click >= 777777:
                            click -= 777777
                            bossmatango = 3
                            SURFACE.fill((0,0,255))
                            del coler[::1]

                elif event.key == K_RIGHT :
                    games()

                elif event.key == K_LEFT :
                    story()

                
        for pos in coler:
            pygame.draw.circle(SURFACE, (pos[1], pos[2], pos[3]), pos[0], 8)
            SURFACE.blit(clicknum,(0,0))
            SURFACE.blit(massage2,(40,30))
            SURFACE.blit(massage3,(70,500))
            SURFACE.blit(massage4,(40,400))
            SURFACE.blit(massage5,(40,350))

        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()