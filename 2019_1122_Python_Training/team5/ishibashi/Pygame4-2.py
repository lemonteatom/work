import sys
import pygame
from pygame.locals import QUIT,Rect,MOUSEBUTTONDOWN

pygame.init()
SURFACE = pygame.display.set_mode((400,200))
FPSCLOCK=pygame.time.Clock()

def main():

    sysfont = pygame.font.SysFont("Meiryo",100)
    start_button = pygame.image.load("start.png")
    stop_button = pygame.image.load("stop.png")
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN :
                break
        #画面の色
        SURFACE.fill((0,0,0))

        #スタート、ストップボタンの表示
        SURFACE.blit(start_button,(100,20))
        SURFACE.blit(stop_button,(200,20))

        #秒、ミリ秒の取得
        time =  pygame.time.get_ticks() /1000
        minute = int (time /60)
        second = int (time % 60)
        msecond = round ((time % 60 - second) *100)

        #数値ををstr化する。
        strMinute = str (minute)
        strSecond = str (second)
        strMSecond = str (msecond)

        string  = strMinute +" : "+strSecond + " : "+ strMSecond

        board = sysfont.render(string, True , (255,255,255))
        SURFACE.blit(board,(100,100))

        print(second,":",msecond)
  
      #おまじない
        pygame.display.update()
        FPSCLOCK.tick(100)

if __name__ == "__main__":
    main()