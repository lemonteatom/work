import sys
import pygame
import random
from pygame.locals import QUIT , Rect,  \
        KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_RETURN,  \
            MOUSEBUTTONDOWN

pygame.init()
pygame.key.set_repeat(5,5)
FPSCLOCK = pygame.time.Clock()

#画面サイズ
screenWidht = 1000
screenHeight = 600
SURFACE = pygame.display.set_mode((screenWidht,screenHeight))   
FPSCLOCK = pygame.time.Clock()

# タイトルの設定
pygame.display.set_caption("鳥を育てるゲーム")

# 画像ロード
#egg = [pygame.image.load(""), \
#    pygame.image.load("img/bird_1.png"), \
#    pygame.image.load("img/bird_2.png")

chick_birth = pygame.image.load("img/chick_birth.png")
chick_sleep = pygame.image.load("img/tarehiyoko.png")
chick_youchien = pygame.image.load("img/youchien_hiyoko.png")

#chicken = pygame.image.load(""), \
#    pygame.image.load(""), \
#    pygame.image.load(""), \
#    pygame.image.load("")

tomato = pygame.image.load("img/tomato.png")

# 画像サイズの設定
chick_birthWidth = 152
chick_birthHeight = 126
chick_sleep_birthWidth = 5
chick_sleep_birthWidth = 5
chick_youchien_birthWidth = 5
chick_youchien_birthWidth = 5
tomatoWidth = 44
tomatoHeight = 36

def main():

    frag = 0
    count = 0

    #データの初期値
    #ひよこの初期値
    chick_birth_x = 410
    chick_birth_y = 420
    #トマトの初期値
    tomato_x = 0
    tomato_y = 0

    mousepos = []
    tomatoFrag = 0

    while True:
    
    # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mousepos.append(event.pos)
                tomatoPos = event.pos
                tomatoFrag = 1

    #ゲームを開始する
        frag = 1

        if frag == 1:
        # 押されているキーをチェック (同時押しVer)
            pressed_keys = pygame.key.get_pressed()
        # 押されているキーに応じて画像を移動
            if pressed_keys[K_LEFT]:
                chick_birth_x -= 5
            if pressed_keys[K_RIGHT]:
                chick_birth_x += 5
            if pressed_keys[K_UP]:
                chick_birth_y -= 5
            if pressed_keys[K_DOWN]:
                chick_birth_y += 5

        # メインプログラム
        # 画面背景カラー
            SURFACE.fill((217,204,255)) 

            # 地面の描写
            start_pos = (0,screenHeight-25)
            end_pos = (screenWidht,screenHeight-25)
            pygame.draw.line(SURFACE,(214,170,122),start_pos,end_pos,50)

            #ひよこの描写
            # 左右の画面端は反対側へ、上下の画面端は行き止まり
            if chick_birth_x > screenWidht :
                chick_birth_x = 0 - chick_birthWidth
            if chick_birth_x < 0 - chick_birthWidth :
                chick_birth_x = screenWidht
            if chick_birth_y > screenHeight - chick_birthHeight -25 :
                chick_birth_y = screenHeight - chick_birthHeight -25
            if chick_birth_y < 0 :
                chick_birth_y = 0

            SURFACE.blit(chick_birth,(chick_birth_x,chick_birth_y))

            if tomatoFrag == 1:
                #トマトの初期値
                tomato_x = tomatoPos[0]
                tomato_y = tomatoPos[1]
                tomatoFrag = 2

            if tomatoFrag == 2:
                for pos in mousepos:
                    SURFACE.blit(tomato,tomatoPos)

                #あたり判定
                if (tomato_x < chick_birth_x + chick_birthWidth) and  \
                    (chick_birth_x < tomato_x + tomatoWidth) and  \
                    (tomato_y < chick_birth_y + chick_birthHeight) and  \
                    (chick_birth_y < tomato_y + tomatoHeight):
                    tomatoFrag = 0
                    count += 1


        # 画面アップデート
        pygame.display.update()
        FPSCLOCK.tick(10) 

    # while end
if __name__ == '__main__':
    main()