import sys
import pygame
import random
from pygame.locals import QUIT, Rect, MOUSEBUTTONDOWN, \
    KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_RETURN

#おまじない
pygame.init()
#
pygame.key.set_repeat(5,5)
#画面サイズ設定
screenW = 1200
screenH = 600
SURFACE = pygame.display.set_mode((screenW, screenH))
#タイトル
pygame.display.set_caption("Flying Bard")
#更新間隔
FPSCLOCK = pygame.time.Clock()

#画像ロード
bird = [pygame.image.load("img/bird_0.png"),
pygame.image.load("img/bird_1.png"),
pygame.image.load("img/bird_2.png"),
pygame.image.load("img/bird_3.png"),
]

dead = pygame.image.load("img/dead.png")

building = [pygame.image.load("img/building1.png"),
pygame.image.load("img/building2.png"),
pygame.image.load("img/building3.png"),
]

cloud = pygame.image.load("img/cloud.png")
cloud1 = pygame.image.load("img/cloud1.png")

crow1 = pygame.image.load("img/karasu.png")
crow2 = pygame.image.load("img/karasu.png")
crow3 = pygame.image.load("img/karasu.png")


#画像サイズ
cloudW = 235
cloudH = 150
cloud1W = 235
cloud1H = 150
birdW = 70
birdH = 60
builW = [95, 42, 45]
builH = [200, 210, 84]
crow1W = 50
crow1H = 30
crow2W = 50
crow2H = 30
crow3W = 50
crow3H = 30


#スコア
scoreFont = pygame.font.SysFont("Meiryo", 50)

#ゲームオーバー
gameoverFont = pygame.font.SysFont("Meiryo", 100)
gameover = gameoverFont.render("GAME OVER", True, (255, 255, 0))
gameoverRect = gameover.get_rect(center = (screenW/2, screenH/2))

#ユーザネーム設定
args = sys.argv
print(args)
if len(sys.argv) == 1:
    name = "Player"
else:
    name = str(args[1])

class buildings():

    #画像、移動速度
    def __init__(self, num, speed):
        self.num = num
        self.speed = speed
        self.pic = building[num]
        self.builX = screenW - ((num + 1) * 500)
        self.builY = screenH - builH[num] - 40

    def buildingMoves(self):
        self.builX -= self.speed
        if self.builX <= (0 - builW[self.num]):
            self.builX = screenW

"""
def userName():
    name = input("あなたの名前を入力してね！")
    userName = pygame.font.SysFont("Meiryo", 100)
    messeage = sysfont.render(name + "さん、ようこそ！", True, (0,0,255))
    messeage_rect = messeage.get_rect(center = (screenW/2, screenH/2))
"""


#メイン関数
def main():
    start = 0
    #userName()

    while True:
        #マウス・キーボード操作
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    start = 0

        if start == 0:

            #データの初期値
            #鳥
            bird_x = random.randint(0, screenH - 50)
            bird_y = random.randint(0, screenH - 50)
            chickenimg = 0
            chickenimgCount = 0

            #カラス
            crow1_x = screenW
            crow1_y = random.randint(0, screenH - 50)
            crow1SpeedAdd = 0

            crow2_x = screenW - 400
            crow2_y = random.randint(0, screenH - 70)
            crow2SpeedAdd = 0

            crow3_x = screenW - 800
            crow3_y = random.randint(0, screenH - 70)
            crow3SpeedAdd = 0

            #ビルクラス（画像、移動速度）
            buil_0 = buildings(0,0.5)
            buil_1 = buildings(1,0.5)
            buil_2 = buildings(2,0.5)

            #雲
            cloud_x = 0
            cloud1_x = 300

            #スコア
            score = 0
            scoreCount = 0

            start = 1
        
        if start == 1:

            #キー押しチェック
            pressed_keys = pygame.key.get_pressed()
            #画像移動
            if pressed_keys[K_LEFT]:
                bird_x -= 5
            if pressed_keys[K_RIGHT]:
                bird_x += 5
            if pressed_keys[K_UP]:
                bird_y -= 5
            if pressed_keys[K_DOWN]:
                bird_y += 5
        

            #背景色設定
            SURFACE.fill((148, 0, 211))

            #地面
            start_pos = (0, screenH - 25)
            end_pos = (screenW, screenH - 25)
            pygame.draw.line(SURFACE, (0,255, 0), start_pos, end_pos, 50)

            #雲
            if cloud_x > 0 - cloudW:
                cloud_x -= 3
            else:
                cloud_x = screenW
            SURFACE.blit(cloud,(cloud_x, 0))
            
            if cloud1_x > 0 - cloud1W:
                cloud1_x -= 3
            else:
                cloud1_x = screenW
            SURFACE.blit(cloud,(cloud1_x, 150))

            #ビル
            buil_0.buildingMoves()
            SURFACE.blit(buil_0.pic, (buil_0.builX, buil_0.builY))

            buil_1.buildingMoves()
            SURFACE.blit(buil_1.pic, (buil_1.builX, buil_1.builY))

            buil_0.buildingMoves()
            SURFACE.blit(buil_2.pic, (buil_2.builX, buil_2.builY))

            #カラス
            if crow1_x < 0 - crow1W:
                crow1_x = screenW
                crow1_y = random.randint(0, screenH - 50)
                crow1SpeedAdd += 0.5

            crow1_x -= 1 + crow1SpeedAdd
            SURFACE.blit(crow1, (crow1_x, crow1_y))

            if crow2_x < 0 - crow2W:
                crow2_x = screenW
                crow2_y = random.randint(0, screenH - 60)
                crow2SpeedAdd += 0.6

            crow2_x -= 1 + crow2SpeedAdd
            SURFACE.blit(crow2, (crow2_x, crow2_y))

            if crow3_x < 0 - crow3W:
                crow3_x = screenW
                crow3_y = random.randint(0, screenH - 50)
                crow3SpeedAdd += 0.7

            crow3_x -= 1 + crow3SpeedAdd
            SURFACE.blit(crow3, (crow3_x, crow3_y))
        
            #鳥
            if bird_x > screenW:
                bird_x = 0 - birdW

            if bird_x < 0 - birdW:
                bird_x = screenW

            if bird_y > screenH:
                bird_y = 0 - birdH

            if bird_y < 0 :
                bird_y = screenH
            

            if chickenimgCount == 20:
                chickenimg = (chickenimg + 1) % 4
                chickenimgCount = 0
            else:
                chickenimgCount += 1
            
            SURFACE.blit(bird[chickenimg], (bird_x,bird_y))

            #当たり判定
            if (crow1_x < bird_x + birdW) and (bird_x < crow1_x + crow1W) and \
                (crow1_y < bird_y + birdH) and (bird_y < crow1_y + crow1H):
                SURFACE.blit(dead, (bird_x,bird_y))
                SURFACE.blit(gameover, gameoverRect)                
                scoreBoard = scoreFont.render(name+"'s SCORE: "+str(score), True, (255, 0, 0))
                SURFACE.blit(scoreBoard, (screenW/2 - 200, screenH/2 + 40))

                start = 2

            if (crow2_x < bird_x + birdW) and (bird_x < crow2_x + crow2W) and \
                (crow2_y < bird_y + birdH) and (bird_y < crow2_y + crow2H):
                SURFACE.blit(dead, (bird_x,bird_y))
                SURFACE.blit(gameover, gameoverRect)
                scoreBoard = scoreFont.render(name+"'s SCORE: "+str(score), True, (255, 0, 0))
                SURFACE.blit(scoreBoard, (screenW/2 - 200, screenH/2 + 40))

                start = 2

            if (crow3_x < bird_x + birdW) and (bird_x < crow3_x + crow3W) and \
                (crow3_y < bird_y + birdH) and (bird_y < crow3_y + crow3H):
                SURFACE.blit(dead, (bird_x,bird_y))
                SURFACE.blit(gameover, gameoverRect)
                scoreBoard = scoreFont.render(name+"'s SCORE: "+str(score), True, (255, 0, 0))
                SURFACE.blit(scoreBoard, (screenW/2 - 200, screenH/2 + 40))

                start = 2


            #スコアの表示
            scoreCount += 1
            if scoreCount == 20:
                score += 1
                scoreCount = 0

            pygame.display.update()
            #FPSCLOCK.tick(100)

        #if start == 1:
            

        if start == 2:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        start = 0

#メイン関数の実行
if __name__ == '__main__':
    main()