import sys
import pygame
import random
from pygame.locals import QUIT , Rect,  \
        KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_RETURN

pygame.init()

screenWidth = 400
screenHeight = 300

SURFACE = pygame.display.set_mode((screenWidth,screenHeight))
FPSCLOCK = pygame.time.Clock()

scoreboardFont = pygame.font.SysFont(None,50)

def main():

    pointer_x = 100
    pointer_y = 100
    score = 0
    judge = 0

    while True:
        SURFACE.fill((0,0,0,))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
        pygame.draw.circle(SURFACE, (0,0,255), (200, 150), 100)
        pygame.draw.circle(SURFACE, (255,255,255), (200, 175), 75)

        for cir_pos in range(175, 226, 50):
            pygame.draw.circle(SURFACE, (0,0,0), (cir_pos, 100), 25)

        for cir_pos in range(175, 226, 50):
            pygame.draw.circle(SURFACE, (255,255,255), (cir_pos, 100), 24)

        pygame.draw.line(SURFACE, (0,0,0), (200, 130), (200, 220))

        pygame.draw.circle(SURFACE, (255, 0, 0), (200, 120), 10)

        for cir_pos in range(190, 211, 20):
            pygame.draw.circle(SURFACE, (0,0,0), (cir_pos, 100), 5, 3)

        pygame.draw.arc(SURFACE, (0,0,0), (140,100,120,120), 3.14, 6.28, 1 )        

        if judge == 0:
            pygame.draw.circle(SURFACE, (100,100,100), (pointer_x, pointer_y), 5)
            pointer_x += random.randint(-10,10)
            pointer_y += random.randint(-10,10)
            if pointer_x > screenWidth:
                pointer_x = 0
            if pointer_x < 0:
                pointer_x = screenWidth
            if pointer_y > screenHeight:
                pointer_y = 0
            if pointer_y < 0:
                pointer_y = screenHeight

            #判定
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_DOWN] and pointer_x >= 195 and pointer_x <= 205 and pointer_y >= 95 and pointer_x <= 105:
                socre += 1
            elif pressed_keys[K_DOWN] and pointer_x >= 180 and pointer_x <= 220 and pointer_y >= 80 and pointer_x <= 120:
                judge = 1
        
        #ゲームオーバー
        if judge == 1:
            gameoverFont = pygame.font.SysFont(None,150)
            gameover = gameoverFont.render("DORAEMON ", True, (255,0,0) )
            gameoverRect = gameover.get_rect(center = (screenWidth/2, screenHeight/2))
            SURFACE.blit(gameover,gameoverRect)

        scoreboard = scoreboardFont.render(str(score),True,(255,255,255))
        SURFACE.blit(scoreboard,(0,0))

        pygame.display.update()
        FPSCLOCK.tick(500)

if __name__ == '__main__':
    main()    
