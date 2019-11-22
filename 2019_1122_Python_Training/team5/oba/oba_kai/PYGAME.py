import sys
import pygame
import random
from pygame.locals import QUIT , Rect,  \
        KEYDOWN, K_LEFT, K_RIGHT,K_SPACE,K_RETURN

pygame.init()
pygame.key.set_repeat(5,5)
screenWidth = 400
screenHeight = 400
SURFACE = pygame.display.set_mode((screenWidth,screenHeight))
FPSCLOCK = pygame.time.Clock()

# ゲームオーバーの文字設定
gameoverFont = pygame.font.SysFont("Meiryo",30)
gameover = gameoverFont.render("GAME OVER \ Push Enter", \
    True, (255,0,0) )
gameoverRect = gameover.get_rect(center = \
    (screenWidth/2, screenHeight/2))

#ゲームクリアの文字設定
gameclearFont = pygame.font.SysFont("Meiryo",30)
gameclear = gameoverFont.render("GAME CLEAR \ Push Enter", \
    True, (255,0,0) )
gameclearRect = gameclear.get_rect(center = \
    (screenWidth/2, screenHeight/2))

def main():
    
    start = 0
    
    while True:
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    start = 0

        if start == 0:
            #バーの初期位置
            pos_y = 375
            pos_start_x = 170
            pos_end_x = 230

            #ボールの初期位置
            ball_x = int((pos_start_x + pos_end_x)/2)
            ball_y = pos_y - 5
            ball_move = 0    
            right_left = 0
            up_down = 0

            #ブロック初期判定値
            judge1 = 0
            judge2 = 0
            judge3 = 0
            judge4 = 0
            judge5 = 0
            judge6 = 0
            judge7 = 0
            judge8 = 0   
            judge9 = 0
            judge10 = 0              


            #ゲームを開始する
            start = 1

        if start == 1:
            # 押されているキーをチェック (同時押しVer)
            pressed_keys = pygame.key.get_pressed()
            # 押されているキーに応じて画像を移動
            if pressed_keys[K_LEFT]:
                pos_start_x -= 2
                pos_end_x -= 2
            if pressed_keys[K_RIGHT]:
                pos_start_x += 2
                pos_end_x += 2
            if pressed_keys[K_SPACE]:
                ball_move = 1

            #背景
            SURFACE.fill((0,0,0))

            #バーの描画
            pygame.draw.line(SURFACE,(255,255,255),(pos_start_x,pos_y),(pos_end_x,pos_y),5)


            #ボールの描画
            my_list = [1,2,3,4,5]
            if ball_move == 1:
                if right_left == 0 and up_down == 0:
                    ball_x += random.choice(my_list)
                    ball_y -= 1
                if right_left == 0 and up_down == 1:
                    ball_x += random.choice(my_list)
                    ball_y += 1
                if right_left == 1 and up_down == 0:                    
                    ball_x -= random.choice(my_list)
                    ball_y -= 1
                if right_left == 1 and up_down == 1:
                    ball_x -= random.choice(my_list)
                    ball_y += 1
                
                pygame.draw.circle(SURFACE,(255,0,0),(ball_x,ball_y),5,5)

                if ball_x >= screenWidth:
                    right_left = 1
                if ball_x <= 0:
                    right_left = 0
                
                if ball_y < 0:
                    up_down = 1
                if (ball_y >= pos_y) and (pos_start_x <= ball_x <= pos_end_x) :
                    up_down = 0
                    right_left = random.randint(0,1)

            #ブロックの描画
            rect1 = Rect(0,0,40,40)
            rect2 = Rect(40,0,40,40)
            rect3 = Rect(80,0,40,40)
            rect4 = Rect(120,0,40,40)
            rect5 = Rect(160,0,40,40)
            rect6 = Rect(200,0,40,40)
            rect7 = Rect(240,0,40,40)
            rect8 = Rect(280,0,40,40)
            rect9 = Rect(320,0,40,40)
            rect10 = Rect(360,0,40,40)                        

            if judge1 == 0:
                if (0 <= ball_x < 40) and (0 <= ball_y <= 40) :
                    judge1 = 1
                    up_down = 1
                    right_left = random.randint(0,1)
            
            if judge2 == 0:
                if (40 <= ball_x < 80) and (0 <= ball_y <= 40) :
                    judge2 = 1
                    up_down = 1
                    right_left = random.randint(0,1)

            if judge3 == 0:
                if (80 <= ball_x < 120) and (0 <= ball_y <= 40) :
                    judge3 = 1
                    up_down = 1
                    right_left = random.randint(0,1)

            if judge4 == 0:
                if (120 <= ball_x <= 160) and (0 <= ball_y <= 40) :
                    judge4 = 1
                    up_down = 1
                    right_left = random.randint(0,1)
                
            if judge5 == 0:
                if (160 <= ball_x < 200) and (0 <= ball_y <= 40) :
                    judge5 = 1
                    up_down = 1
                    right_left = random.randint(0,1)

            if judge6 == 0:    
                if (200 <= ball_x < 240) and (0 <= ball_y <= 40) :
                    judge6 = 1
                    up_down = 1
                    right_left = random.randint(0,1)

            if judge7 == 0:
                if (240 <= ball_x < 280) and (0 <= ball_y <= 40) :
                    judge7 = 1
                    up_down = 1
                    right_left = random.randint(0,1)

            if judge8 == 0:
                if (280 <= ball_x <= 320) and (0 <= ball_y <= 40) :
                    judge8 = 1
                    up_down = 1
                    right_left = random.randint(0,1)

            if judge9 == 0:
                if (320 <= ball_x < 360) and (0 <= ball_y <= 40) :
                    judge9 = 1
                    up_down = 1
                    right_left = random.randint(0,1)

            if judge10 == 0:
                if (360 <= ball_x <= 400) and (0 <= ball_y <= 40) :
                    judge10 = 1
                    up_down = 1
                    right_left = random.randint(0,1)

            if judge1 == 0:
                pygame.draw.rect(SURFACE,(225,225,225),rect1,5)
            if judge2 == 0:
                pygame.draw.rect(SURFACE,(225,225,225),rect2,5)
            if judge3 == 0:
                pygame.draw.rect(SURFACE,(225,225,225),rect3,5)
            if judge4 == 0:
                pygame.draw.rect(SURFACE,(225,225,225),rect4,5)
            if judge5 == 0:
                pygame.draw.rect(SURFACE,(225,225,225),rect5,5)
            if judge6 == 0:
                pygame.draw.rect(SURFACE,(225,225,225),rect6,5)
            if judge7 == 0:
                pygame.draw.rect(SURFACE,(225,225,225),rect7,5)
            if judge8 == 0:
                pygame.draw.rect(SURFACE,(225,225,225),rect8,5)            
            if judge9 == 0:
                pygame.draw.rect(SURFACE,(225,225,225),rect9,5)
            if judge10 == 0:
                pygame.draw.rect(SURFACE,(225,225,225),rect10,5)

            #ゲームオーバー判定
            if ball_y > pos_y:
                SURFACE.blit(gameover,gameoverRect)
                start = 2

            #ゲームクリア判定
            if judge1 == 1 and judge2 == 1 and judge3 == 1 and judge4 == 1 and judge5 == 1 and judge6 == 1 and judge7 == 1 and judge8 == 1 and judge9 == 1 and judge10 == 1:
                SURFACE.blit(gameclear,gameclearRect)
                start == 3

            pygame.display.update()
            FPSCLOCK.tick(100)

        if start == 2 or 3:
            # イベント処理
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN :
                        start = 0


# while end
if __name__ == '__main__':
    main()