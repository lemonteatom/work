#ゲームプログラム

import sys
import pygame
import random
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_RETURN

pygame.init()
pygame.key.set_repeat(5,5)

#画面サイズ
screenWidht = 1000
screenHeight = 600
SURFACE = pygame.display.set_mode((screenWidht, screenHeight))

#タイトルの設定
pygame.display.set_caption("鳥が動くプログラム")

#画像ロード
cloud = pygame.image.load("FlyingBird/FlyingBird/img/cloud.png")
chicken = [pygame.image.load("FlyingBird/FlyingBird/img/bird_0.png"),pygame.image.load("FlyingBird/FlyingBird/img/bird_1.png"),pygame.image.load("FlyingBird/FlyingBird/img/bird_2.png"),pygame.image.load("FlyingBird/FlyingBird/img/bird_3.png"),pygame.image.load("FlyingBird/FlyingBird/img/dead.png")]
building = [pygame.image.load("FlyingBird/FlyingBird/img/building1.png"),pygame.image.load("FlyingBird/FlyingBird/img/building2.png"),pygame.image.load("FlyingBird/FlyingBird/img/building3.png")]
crow = pygame.image.load("FlyingBird/FlyingBird/img/crow.png")
human = pygame.image.load("FlyingBird/FlyingBird/img/human.png")

#画像サイズの設定
cloudWidth = 235
cloudHeight = 150
birdWidth = 70
birdHeight = 60
buildingWidth = [95, 42 ,45]
buildingHeight = [200, 210 ,84]
crowWidth = 50
crowHeight = 39
humanWidth = 230
humanHeight = 150

#スコアの文字設定
scoreboardFont = pygame.font.SysFont("Meiryo", 50)

#ゲームオーバーの文字設定
gameoverFont = pygame.font.SysFont("Meiryo", 80)
gameover = gameoverFont.render("GAME OVER \ Retry?Push Enter", True , (204,102,153))
gameoverRect = gameover.get_rect(center = (screenWidht / 2 ,screenHeight/ 2))

class buildings():

    #引数1:使用するビルの画像0～2
    #引数2:ビルの移動速度
    def __init__(self, num ,speed):
        self.number = num
        self.moveSpeed = speed
        self.pic = building[num]
        self.builX = screenWidht - ((num + 1) * 500)
        self.builY = screenHeight - buildingHeight[num] -40

    def buildingMoves(self):
        self.builX -= self.moveSpeed
        if self.builX <= (0 - buildingWidth[self.number]):
            self.builX = screenWidht

def main():
    start = 0

    while True:
    
        #イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    start = 0
        if start == 0:

            #データの初期化
            #雲の初期値
            cloud_x = 0

            #ビルの初期化
            building_0 = buildings(0, 0.5)
            building_1 = buildings(1, 0.5)
            building_2 = buildings(2, 0.5)

            #鳥の初期値
            bird_x = 30
            bird_y = 200
            chickenimg = 0
            chickenimgCount = 0

            #カラスの初期値
            crow_x = screenWidht
            crow_y = random.randint(0, screenHeight - 50)
            crowSpeedAdd = 0

            #飛ぶ人の初期化
            human_x = screenWidht
            human_y = random.randint(0, screenHeight - 150)
            humanSpeedAdd = 0

            #スコアの初期化
            score = 0
            scoreCount = 0

            #背景色の初期値
            colorCount = 0
            colorNumber = 0

            #ゲームを開始する
            start = 1

        if start == 1:
            #押されているキーをチェック(同時押しVer)
            pressed_keys = pygame.key.get_pressed()

            #押されているキーに応じて画像を移動
            if pressed_keys [K_LEFT]:
                bird_x -= 5
            if pressed_keys [K_RIGHT]:
                bird_x += 5
            if pressed_keys [K_UP]:
                bird_y -= 5
            if pressed_keys [K_DOWN]:
                bird_y += 5

            #メインプログラム
            #画面背景カラーリストを作成
            color = [(0,0,51),(0,0,102),(0,51,255),(0,153,204),(255,255,153),(255,153,51),(255,51,0),(204,51,0),(153,102,153),(102,51,153)]
            if colorCount == 200:
                colorNumber += 1
                colorCount = 0
                if colorNumber >= len(color) :
                    colorNumber = 0

            colorCount += 1
            SURFACE.fill(color[colorNumber])

            #地面の描写
            start_pos = (0, screenHeight-25)
            end_pos = (screenWidht, screenHeight-25)
            pygame.draw.line(SURFACE, (153,255,102), start_pos, end_pos ,50)

            #雲の描写
            #画面左端に行ったら画像を右端からスタートする
            if cloud_x > 0 - cloudWidth:
                cloud_x -= 0.8
            else:
                cloud_x = screenWidht
            SURFACE.blit(cloud,(cloud_x, 0))

            #ビルの描写
            building_0.buildingMoves()
            SURFACE.blit(building_0.pic,(building_0.builX,building_0.builY))

            building_1.buildingMoves()
            SURFACE.blit(building_1.pic,(building_1.builX,building_1.builY))

            building_2.buildingMoves()
            SURFACE.blit(building_2.pic,(building_2.builX,building_2.builY))

            #カラスの描写
            if crow_x < 0 - crowWidth:
                crow_x = screenWidht
                crow_y = random.randint(0, screenHeight - 50)
                crowSpeedAdd += 1

            crow_x -= 1 + crowSpeedAdd
            SURFACE.blit(crow,(crow_x,crow_y))

            #飛ぶ人の描写
            if human_x < 0 -humanWidth:
                human_x = screenWidht
                human_y = random.randint(0, screenHeight - 150)
                humanSpeedAdd += 0

            human_x -= 1 + humanSpeedAdd
            SURFACE.blit(human,(human_x, human_y))

            #鳥の描写
            #左右の画面端は反対側へ、上下の画面端は行き止まり
            if bird_x > screenWidht:
                bird_x = 0 - birdWidth
            if bird_x < 0 -birdWidth:
                bird_x = screenWidht
            if bird_y > screenHeight - birdHeight - 25:
                bird_y = screenHeight - birdHeight - 25
            if bird_y < 0:
                bird_y = 0

            if chickenimgCount == 20:
                chickenimg = (chickenimg + 1) % 4
                chickenimgCount = 0
            else:
                chickenimgCount += 1

            SURFACE.blit(chicken[chickenimg], (bird_x, bird_y))

            #あたり安定(カラス)
            if (crow_x < bird_x + birdWidth) and (bird_x < crow_x + crowWidth) and (crow_y < bird_y + birdHeight) and (bird_y < crow_y + crowHeight):
                SURFACE.blit(chicken[4], (bird_x, bird_y))
                SURFACE.blit(gameover, gameoverRect)
                SURFACE.blit(scoreboard,(screenWidht / 2, 380))
                start = 2

            #あたり安定(飛ぶ人)
            if (human_x < bird_x + birdWidth) and (bird_x < human_x + crowWidth) and (human_y < bird_y + birdHeight) and (bird_y < human_y + humanHeight):
                SURFACE.blit(chicken[4], (bird_x, bird_y))
                SURFACE.blit(gameover, gameoverRect)
                SURFACE.blit(scoreboard,(screenWidht / 2, 380))
                start = 2

            #スコアの表示
            scoreCount += 1
            if scoreCount == 20:
                score += 1
                scoreCount = 0
            
            scoreboard = scoreboardFont.render(str(score),True, (0,0,0))
            SURFACE.blit(scoreboard,(0,0))

            #画面アップデート
            pygame.display.update()

    #if start == 1:
    #ゲームオーバー処理
    if start == 2:
        #イベント処理
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    start = 0

#while end
if __name__ == '__main__':
    main()