#*****************************************************
#雲が動き、鳥が十字キーで動かせるプログラム
#*****************************************************
import sys
import pygame
import random
from pygame.locals import QUIT , Rect,\
    KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_RETURN

pygame.init()
pygame.key.set_repeat(5,5)

#画面サイズ
screenWidht = 1000
screenHeight = 600
SURFACE = pygame.display.set_mode((screenWidht,screenHeight))

#タイトルの設定
pygame.display.set_caption("小宮山陽大の大冒険")

#画像ロード
cloud = pygame.image.load("img/ocean.png")
chicken = [pygame.image.load("img/komiyama.png")]
#    pygame.image.load("img/bird_1.png"),\
#    pygame.image.load("img/bird_2.png"),\
#    pygame.image.load("img/bird_3.png")]

building = [pygame.image.load("img/castle01.png"),\
    pygame.image.load("img/akasaka.png"),\
    pygame.image.load("img/hokkaido.png")]

crow = pygame.image.load("img/tori.png")


#*****
#bird = pygame.image.load("img/bird_0.png")
#*****


#画像サイズの設定

cloudWidth = 235
cloudHeight = 150
birdwidth = 180
birdHeight = 180
buildingwidht=[95,42,45]
buildingheight=[200,210,84]
crowwidth = 640
crowHeigth = 640

#スコアの文字の設定
scoreboardFont = pygame.font.SysFont("Meiryo",60)

#ゲームオーバーの文字設定
gameoverFont = pygame.font.SysFont("Meiryo",100)
gameover = gameoverFont.render("Komiyama TEL:05058465174",\
    True,(255,0,0))
gameoverRect = gameover.get_rect(center =\
    (screenWidht/2,screenHeight/2))

class buildings():


#引数1:使用するビルの画像0~2
#引数2:ビルの移動速度

    def __init__(self,num,speed):
        self.number = num
        self.moveSpeed = speed
        self.pic = building[num]
        self.builX = screenWidht - ((num + 1)*500)
        self.builY = screenHeight - buildingheight[num] -40

    def buildingMoves(self):
        self.builX -=self.moveSpeed
        if self.builX <= (0 - buildingwidht[self.number]):
            self.builX = screenWidht

def main():

    start=0

        
    while True:

        #イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    start=0

        if start == 0:


            #データの初期
            #雲の初期値
            cloud_x = 0 

            #ビルの初期化
            building_0 = buildings(0,0.5)
            building_1 = buildings(1,0.5)
            building_2 = buildings(2,0.5)

            #鳥の初期値
            bird_x = 50
            bird_y = 200
            chickenimg = 0
            chickenimgCount = 0

            #カラスの初期値
            crow_x = screenWidht
            crow_y = random.randint(0,screenHeight-50)
            crowSpeedAdd = 0

            #スコアの初期化
            score = 0
            scoreCount = 0

            #ゲームを開始する
            start = 1

        if start == 1:
            #押されているキーをチェック(同時押しVer)
            pressed_keys = pygame.key.get_pressed()
            #押されているキーに応じて画像を移動
            if pressed_keys[K_LEFT]:
                bird_x -= 5
            if pressed_keys[K_RIGHT]:
                bird_x += 5
            if pressed_keys[K_UP]:
                bird_y -= 5
            if pressed_keys[K_DOWN]:
                bird_y += 5


                #押されているキーをチェック(単押しVer)
    #            elif event.type == KEYDOWN:
    #                if event.key == K_LEFT:
    #                    bird_x -= 5
    #                if event.key == K_RIGHT:
    #                    bird_x += 5
    #                if event.key == K_UP:
    #                    bird_y -= 5
    #                if event.key == K_DOWN:
    #                    bird_y += 5


            #メインプログラム
            #画面背景カラー
            SURFACE.fill((255,255,255))

            #地面の描写
            start_pos = (0,screenHeight-25)
            end_pos = (screenWidht,screenHeight-25)
            pygame.draw.line(SURFACE,(255,255,100),start_pos,end_pos,50)

            #雲の描写
            #画面端までいったら画像を右端からスタートする
            if cloud_x > 0 -cloudWidth:
                cloud_x -= 0.8

            else:
                cloud_x = screenWidht
            SURFACE.blit(cloud,(cloud_x,0))

            #ビルの描写
            building_0.buildingMoves()
            SURFACE.blit(building_0.pic,\
                (building_0.builX,50))

            building_1.buildingMoves()
            SURFACE.blit(building_1.pic,\
                (building_1.builX,100))

            building_2.buildingMoves()
            SURFACE.blit(building_2.pic,\
                (building_2.builX,100))

            #カラスの描写
            if crow_x < 0 -crowwidth:
                crow_x = screenWidht
                crow_y = random.randint(0,screenHeight-50)
                crowSpeedAdd +=1
            
            crow_x -=1+crowSpeedAdd
            SURFACE.blit(crow,(crow_x,crow_y))

            #鳥の描写
            #左右の画面端は反対側へ、上下の画面端は行き止まり
            if bird_x > screenWidht:
                bird_x = 0 -birdwidth
            if bird_x < 0 - birdwidth:
                bird_x = screenWidht
            if bird_y > screenHeight - birdHeight -25:
                bird_y = screenHeight - birdHeight -25
            if bird_y < 0 :
                bird_y = 0

            if chickenimgCount == 20:
                chickenimg = (chickenimg + 1)%4
                chickenimgCount = 0
            else:
                chickenimgCount += 1

            SURFACE.blit(chicken[0],(bird_x,bird_y))

            #当たり判定
            if (crow_x < bird_x + birdwidth) and \
                (bird_x < crow_x +crowwidth) and \
                (crow_y < bird_y + birdHeight) and \
                (bird_y < crow_y + crowHeigth):
                SURFACE.blit(gameover,gameoverRect)
                start = 2

            #スコアの表示
            scoreCount +=1
            if scoreCount == 20:
                score+=1
                scoreCount = 0

            scoreboard = scoreboardFont.render(str(score),\
                True,(0,0,0))
            SURFACE.blit(scoreboard,(0,0))

            #画面アップデート
            pygame.display.update()
    
    #if start == 1:
    #ゲームオーバー処理
    if start == 2:
        #イベント処理
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key==K_RETURN:
                    start=0

#while end
if __name__ == '__main__':
    main()