# ***********************************************************
# カラスが飛びスコアが加算され、
# カラスに当たるとゲームオーバーになるプログラム
# ***********************************************************

import sys
import pygame
import random
from pygame.locals import QUIT , Rect,  \
        KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_RETURN

pygame.init()
pygame.key.set_repeat(5,5)

#画面サイズ
screenWidht = 1000
screenHeight = 600
SURFACE = pygame.display.set_mode((screenWidht,screenHeight))    

# タイトルの設定
pygame.display.set_caption("JOKER ESCAPE")

# 画像ロード
cloud = pygame.image.load("img/cloud.png")
chicken = [pygame.image.load("img/jokerイラスト.jpg"), \
    pygame.image.load("img/jokerイラスト1.jpg"), \
    pygame.image.load("img/jokerイラスト2.jpg"), \
    pygame.image.load("img/jokerイラスト3.jpg")]

building = [pygame.image.load("img/building1.png"), \
    pygame.image.load("img/building2.png"), \
    pygame.image.load("img/building3.png")]

crow = pygame.image.load("img/bat.jpg")

opening = pygame.image.load("img/joker.jpg")

ending = pygame.image.load("img/end.png")

# 画像サイズの設定
cloudWidth = 154
cloudHeight = 98
birdWidth = 76
birdHeight = 135
buildingwidht = [95,63,90]
buildingheight = [200,315,168]
crowWidth = 98
crowHeigth = 54

# スコアの文字の設定
scoreboardFont = pygame.font.SysFont("Meiryo",50)

# ゲームオーバーの文字設定
gameoverFont = pygame.font.SysFont("Meiryo",200)
gameover = gameoverFont.render("GAME OVER", \
    True, (225, 230, 0) )
gameoverRect = gameover.get_rect(center = \
    (screenWidht/2, screenHeight/2))


class buildings():

    # 引数1：使用するビルの画像0～2　
    # 引数2：ビルの移動速度 
    def __init__(self,num,speed):
        self.number = num
        self.moveSpeed = speed
        self.pic = building[num]
        self.builX = screenWidht - ((num + 1) * 500)
        self.builY = screenHeight - buildingheight[num] - 40

    def buildingMoves(self):
        self.builX -= self.moveSpeed
        if self.builX <= (0 - buildingwidht[self.number]):
            self.builX = screenWidht


def main():
    start = 3

    

    while True:

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    start = 0

        if start == 3:
            SURFACE.fill((30,30,30)) 
            SURFACE.blit(opening,(screenWidht/2 - 435/2,screenHeight/2 - 658/2))

            sysfont = pygame.font.SysFont("Meiryo", 420) 
            message = sysfont.render("JOKER", True, (225, 230, 0)) #（文字,文字を滑らかにするか否か,色）
            message_rect = message.get_rect(center = (500,300))  #文字の存在する範囲のRect値を指定
            SURFACE.blit(message, message_rect)

            # SURFACE.blit(SURFACE.blit,(100,100))
            pygame.display.update()   

        if start == 0:

            # データの初期値
            # 雲の初期値
            cloud_x = 0

            # ビルの初期化
            building_0 = buildings(0,0.5)
            building_1 = buildings(1,0.5)
            building_2 = buildings(2,0.5)

            # 鳥の初期値
            bird_x = 30
            bird_y = 200
            chickenimg = 0
            chickenimgCount = 0

            # カラスの初期値
            crow_x = screenWidht
            crow_y = random.randint(0,screenHeight - 50)
            crowSpeedAdd = 0

            # スコアの初期化
            score = 0
            scoreCount = 0

            # ゲームを開始する
            start = 1

        if start == 1:
            # 押されているキーをチェック (同時押しVer)
            pressed_keys = pygame.key.get_pressed()
            # 押されているキーに応じて画像を移動
            if pressed_keys[K_LEFT]:
                bird_x -= 5
            if pressed_keys[K_RIGHT]:
                bird_x += 5
            if pressed_keys[K_UP]:
                bird_y -= 5
            if pressed_keys[K_DOWN]:
                bird_y += 5

            # メインプログラム
            # 画面背景カラー
            SURFACE.fill((30,30,30)) 

            # 地面の描写
            start_pos = (0,screenHeight-25)
            end_pos = (screenWidht,screenHeight-25)
            pygame.draw.line(SURFACE,(66,112,6),start_pos,end_pos,50)

            # 雲の描写
            # 画面端までいったら画像を左端からスタートする
            if cloud_x > 0 - cloudWidth:
                cloud_x -= 0.8
            else:                       
                cloud_x = screenWidht
            SURFACE.blit(cloud,(cloud_x,0))

            # ビルの描写
            building_0.buildingMoves()
            SURFACE.blit(building_0.pic, \
                (building_0.builX,building_0.builY))

            building_1.buildingMoves()
            SURFACE.blit(building_1.pic, \
                (building_1.builX,building_1.builY))

            building_2.buildingMoves()
            SURFACE.blit(building_2.pic, \
                (building_2.builX,building_2.builY))

            # カラスの描写
            if crow_x < 0 - crowWidth:
                crow_x = screenWidht
                crow_y = random.randint(0,screenHeight-50)
                crowSpeedAdd += 1

            crow_x -= 1 + crowSpeedAdd
            SURFACE.blit(crow,(crow_x,crow_y))

            # 鳥の描写
            # 左右の画面端は反対側へ、上下の画面端は行き止まり
            if bird_x > screenWidht :
                bird_x = 0 - birdWidth
            if bird_x < 0 - birdWidth :
                bird_x = screenWidht
            if bird_y > screenHeight - birdHeight -25 :
                bird_y = screenHeight - birdHeight -25
            if bird_y < 0 :
                bird_y = 0
            
            if chickenimgCount == 20:
                chickenimg = (chickenimg + 1 )% 4
                chickenimgCount = 0
            else:
                chickenimgCount += 1

            SURFACE.blit(chicken[chickenimg],(bird_x,bird_y))

            # あたり判定
            if (crow_x < bird_x + birdWidth) and  \
                (bird_x < crow_x + crowWidth) and  \
                (crow_y < bird_y + birdHeight) and  \
                (bird_y < crow_y + crowHeigth):
                SURFACE.blit(ending,(screenWidht/2 - 1000/2,screenHeight/2 - 601/2))
                SURFACE.blit(gameover,gameoverRect)
                start = 2

            # スコアの表示
            scoreCount += 1
            if scoreCount == 20:
                score += 1
                scoreCount = 0

            scoreboard = scoreboardFont.render(str(score), \
                True,(225, 230, 0))
            SURFACE.blit(scoreboard,(0,0))

            # 画面アップデート
            pygame.display.update()

        # if start == 1:
        #ゲームオーバー処理 
        if start == 2:
            # イベント処理
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN :
                        start = 0

# while end
if __name__ == '__main__':
    main()