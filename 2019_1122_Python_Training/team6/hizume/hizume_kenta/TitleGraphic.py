from pygame.locals import *
import pygame
import sys

hand = pygame.image.load("img/hand.png")
friedchicken = pygame.image.load("img/food_fried_chicken.png")
friedchicken = pygame.transform.smoothscale(friedchicken,(200,400))

def main():
    pygame.init()    
    screen = pygame.display.set_mode((1000, 600))    
    pygame.display.set_caption("Flying Bird")    
    
    startbutton = pygame.Rect(250,400,500,100)

    #STEP1.フォントの用意  
    titlefont = pygame.font.SysFont(None,200)
    startfont = pygame.font.SysFont(None,100)

    #STEP2.テキストの設定
    titlelogo = titlefont.render("Frying Bard",True,(255,255,0))
    starttext = startfont.render("START",True,(255,255,255))
    
    
    running = True
    #メインループ
    while True:
        screen.fill((255,0,0))  #背景

        #スタートボタン描画
        pygame.draw.rect(screen, (0, 0, 255), startbutton)

        #チキン描画
        #screen.blit(friedchicken,(50,100))
        #手の描画
        screen.blit(hand,(300,450))
        #文字描画
        screen.blit(starttext, (400,420))
        screen.blit(titlelogo, (100,150))

        #アプデ
        pygame.display.update()

        #イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                pygame.quit()  
                sys.exit() 
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startbutton.collidepoint(event.pos):
                    print("START")
                    return 0;
                    
                    
if __name__=="__main__":
    main()