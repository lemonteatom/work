import sys
import pygame
import random
from pygame.locals import QUIT , Rect, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_RETURN, K_x, K_z, KMOD_LSHIFT

pygame.init()
pygame.key.set_repeat(5,5)
FPSCLOCK = pygame.time.Clock()

#画面サイズ
screenWidht = 1500
screenHeight = 800
SURFACE = pygame.display.set_mode((screenWidht,screenHeight))    

# タイトル設定
pygame.display.set_caption("Aegis Bird")

# 画像ロード
cloud = pygame.image.load("img/cloud.png")
chicken = [pygame.image.load("img/bird_0.png"), \
    pygame.image.load("img/bird_1.png"), \
    pygame.image.load("img/bird_2.png"), \
    pygame.image.load("img/bird_3.png")]

building = [pygame.image.load("img/building1.png"), \
    pygame.image.load("img/building2.png"), \
    pygame.image.load("img/building3.png")]

crow1 = pygame.image.load("img/missile.png")
crow2 = pygame.image.load("img/missile.png")
crow3 = pygame.image.load("img/missile.png")
crow4 = pygame.image.load("img/missile.png")
crow5 = pygame.image.load("img/missile.png")
crow6 = pygame.image.load("img/missile.png")
crow7 = pygame.image.load("img/missile.png")
crow8 = pygame.image.load("img/missile.png")
crow9 = pygame.image.load("img/missile.png")
crow10 = pygame.image.load("img/missile.png")

aimMissile = pygame.image.load("img/aim9.png")

aim9 = pygame.image.load("img/aim9l.jpg")

# 画像サイズ
cloudWidth = 235
cloudHeight = 150
birdWidth = 70
birdHeight = 60
buildingwidht = [95,42,45]
buildingheight = [200,210,84]
crowWidth = 100
crowHeigth = 40
BombWidth = 200
BombHeight = 200
missileWidth =100
missileHight =40

# スコア文字
scoreboardFont = pygame.font.SysFont("Meiryo",50)

# ゲームオーバー文字
gameoverFont = pygame.font.SysFont("Meiryo",100)
gameover = gameoverFont.render("Miss! \ Push Enter", True, (255,0,0) )
gameoverRect = gameover.get_rect(center = \
    (screenWidht/2, screenHeight/2)) #センターに表示

#バードストライク処理
gameover2 = gameoverFont.render("Bird Strike! \ Push Enter", True, (255,0,0) )
gameoverRect2 = gameover.get_rect(center = (screenWidht/2, screenHeight/2)) #センターに表示

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
    start = 0

    while True:

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN :
                    start = 0
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

            bomb_x = bird_x + 1000
            bomb_y = bird_y + 25

            crowSpeedAdd = 1

            # カラスの初期値1
            crow1_x = screenWidht
            crow1_y = random.randint(0,screenHeight-50)
            # カラスの初期値2
            crow2_x = screenWidht + 150
            crow2_y = random.randint(0,screenHeight-50)
            # カラスの初期値3
            crow3_x = screenWidht + 300
            crow3_y = random.randint(0,screenHeight-50)
            # カラスの初期値4
            crow4_x = screenWidht + 450
            crow4_y = random.randint(0,screenHeight-50)
            # カラスの初期値5
            crow5_x = screenWidht + 600
            crow5_y = random.randint(0,screenHeight-50)

            crow6_x = screenWidht + 750
            crow6_y = random.randint(0,screenHeight-50)

            crow7_x = screenWidht + 900
            crow7_y = random.randint(0,screenHeight-50)

            crow8_x = screenWidht + 1050
            crow8_y = random.randint(0,screenHeight-50)

            crow9_x = screenWidht + 1200
            crow9_y = random.randint(0,screenHeight-50)

            crow10_x = screenWidht + 1350
            crow10_y = random.randint(0,screenHeight-50)

            #ミサイル初期値
            aimMissile_x = screenWidht + 1500
            aimMissile_y = random.randint(0,screenHeight-50)

            #ミサイル初期位置
            missile_x = 2000
            missile_y = 2000

            # スコアの初期化
            score = 0
            scoreCount = 0

            # ゲームを開始する
            start = 1

            #発射の状態
            fire = False
            #ミサイル表示時間
            missileTimer = 0

            #難易度初期値
            difficulty = 0

            #撃墜数
            killCount = 0

            #クールタイム初期値
            charge = 100

        if start == 1:
            # 押されているキーをチェック (同時押しVer)
            pressed_keys = pygame.key.get_pressed()
            # 押されているキーに応じて画像を移動
            if pressed_keys[K_LEFT]:
                bird_x -= 2
            if pressed_keys[K_RIGHT]:
                bird_x += 2
            if pressed_keys[K_UP]:
                bird_y -= 2
            if pressed_keys[K_DOWN]:
                bird_y += 2

            if (pressed_keys[K_LEFT]) and(pressed_keys[K_z]) :
                bird_x -= 3
            if (pressed_keys[K_RIGHT]) and(pressed_keys[K_z]) :
                bird_x += 3
            if (pressed_keys[K_UP] )and(pressed_keys[K_z]) :
                bird_y -= 3
            if (pressed_keys[K_DOWN]) and(pressed_keys[K_z]) :
                bird_y += 3

            if pressed_keys[K_x]:
                if charge >= 100:
                    fire = True


            # メインプログラム
            # 画面背景カラー
            SURFACE.fill((215,255,255)) 

            # 地面の描写
            start_pos = (0,screenHeight-25)
            end_pos = (screenWidht,screenHeight-25)
            pygame.draw.line(SURFACE,(81,68,59),start_pos,end_pos,50)

            # 雲の描写
            # 画面端までいったら画像を左端からスタートする
            if cloud_x > 0 - cloudWidth:
                cloud_x -= 0.8
            else:                       
                cloud_x = screenWidht
            SURFACE.blit(cloud,(cloud_x,0))

            # ビルの描写
            building_0.buildingMoves()
            SURFACE.blit(building_0.pic, (building_0.builX,building_0.builY))

            building_1.buildingMoves()
            SURFACE.blit(building_1.pic, \
                (building_1.builX,building_1.builY))

            building_2.buildingMoves()
            SURFACE.blit(building_2.pic, \
                (building_2.builX,building_2.builY))

            # カラスの描写
            if crow1_x < 0 - crowWidth:
                crow1_x = screenWidht
                crow1_y = random.randint(0,screenHeight-50)

            if crow2_x < 0 - crowWidth:
                crow2_x = screenWidht
                crow2_y = random.randint(0,screenHeight-50)

            if crow3_x < 0 - crowWidth:
                crow3_x = screenWidht
                crow3_y = random.randint(0,screenHeight-50)

            if crow4_x < 0 - crowWidth:
                crow4_x = screenWidht
                crow4_y = random.randint(0,screenHeight-50)

            if crow5_x < 0 - crowWidth:
                crow5_x = screenWidht
                crow5_y = random.randint(0,screenHeight-50)
            
            if crow6_x < 0 - crowWidth:
                crow6x = screenWidht
                crow6_y = random.randint(0,screenHeight-50)

            if crow7_x < 0 - crowWidth:
                crow7_x = screenWidht
                crow7_y = random.randint(0,screenHeight-50)

            if crow8_x < 0 - crowWidth:
                crow8_x = screenWidht
                crow8_y = random.randint(0,screenHeight-50)

            if crow9_x < 0 - crowWidth:
                crow9_x = screenWidht
                crow9_y = random.randint(0,screenHeight-50)

            if crow10_x < 0 - crowWidth:
                crow10_x = screenWidht
                crow10_y = random.randint(0,screenHeight-50)

            if aimMissile_x < -500 :
                aimMissile_x = screenWidht
                aimMissile_y = random.randint(0,screenHeight + 50)

            crow1_x -= 1 + crowSpeedAdd
            crow2_x -= 1 + crowSpeedAdd
            crow3_x -= 1 + crowSpeedAdd
            crow4_x -= 1 + crowSpeedAdd
            crow5_x -= 1 + crowSpeedAdd
            crow6_x -= 1 + crowSpeedAdd
            crow7_x -= 1 + crowSpeedAdd
            crow8_x -= 1 + crowSpeedAdd
            crow9_x -= 1 + crowSpeedAdd
            crow10_x -= 1 + crowSpeedAdd
            aimMissile_x -= 1 + 3

            SURFACE.blit(crow1,(crow1_x,crow1_y))
            SURFACE.blit(crow2,(crow2_x,crow2_y))
            SURFACE.blit(crow3,(crow3_x,crow3_y))
            SURFACE.blit(crow4,(crow4_x,crow4_y))
            SURFACE.blit(crow5,(crow5_x,crow5_y))
            SURFACE.blit(crow6,(crow6_x,crow6_y))
            SURFACE.blit(crow7,(crow7_x,crow7_y))
            SURFACE.blit(crow8,(crow8_x,crow8_y))
            SURFACE.blit(crow9,(crow9_x,crow9_y))
            SURFACE.blit(crow10,(crow10_x,crow10_y))
            SURFACE.blit(aimMissile,(aimMissile_x, aimMissile_y))



            #照準の描画:円
            center_pos = (bird_x + 800, bird_y + 125)
            pygame.draw.circle(SURFACE,(0,0,0),center_pos,25,1)
            #照準の描写：横
            start_pos = (bird_x + 750, bird_y + 125)
            end_pos = (bird_x + 850, bird_y + 125)
            pygame.draw.line(SURFACE,(0,0,0),start_pos,end_pos,1)
            #照準の描写：縦
            start_pos = (bird_x + 800, bird_y + 75)
            end_pos = (bird_x + 800, bird_y + 175)
            pygame.draw.line(SURFACE,(0,0,0),start_pos,end_pos,1)

            # 鳥の描写
            # 左右の画面端は反対側へ、上下の画面端は行き止まり
            if bird_x > screenWidht - birdWidth -25 :
                bird_x = screenWidht - birdWidth -25
            if bird_x < 0 :
                bird_x = 0
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

            #ミサイルの描写
            SURFACE.blit(aim9,(missile_x,missile_y))

            if (fire == True):
                missile_x = bird_x + 750
                missile_y = bird_y + 75
                missileTimer = 10
                charge = 0
                fire = False

            #チャージタイマー
            if charge < 100:
                charge +=0.5

            if missileTimer <= 0:
                missile_x = 2000
                missile_y = 2000

            
            # 判定
            if (crow1_x < bird_x + birdWidth) and (bird_x < crow1_x + crowWidth) and (crow1_y < bird_y + birdHeight) and (bird_y < crow1_y + crowHeigth):
                SURFACE.blit(gameover,gameoverRect)
                start = 2

            if (crow2_x < bird_x + birdWidth) and (bird_x < crow2_x + crowWidth) and (crow2_y < bird_y + birdHeight) and (bird_y < crow2_y + crowHeigth):
                SURFACE.blit(gameover,gameoverRect)
                start = 2

            if (crow3_x < bird_x + birdWidth) and (bird_x < crow3_x + crowWidth) and (crow3_y < bird_y + birdHeight) and (bird_y < crow3_y + crowHeigth):
                SURFACE.blit(gameover,gameoverRect)
                start = 2

            if (crow4_x < bird_x + birdWidth) and (bird_x < crow4_x + crowWidth) and (crow4_y < bird_y + birdHeight) and (bird_y < crow4_y + crowHeigth):
                SURFACE.blit(gameover,gameoverRect)
                start = 2

            if (crow5_x < bird_x + birdWidth) and (bird_x < crow5_x + crowWidth) and (crow5_y < bird_y + birdHeight) and (bird_y < crow5_y + crowHeigth):
                SURFACE.blit(gameover,gameoverRect)
                start = 2

            if (crow6_x < bird_x + birdWidth) and (bird_x < crow6_x + crowWidth) and (crow6_y < bird_y + birdHeight) and (bird_y < crow6_y + crowHeigth):
                SURFACE.blit(gameover,gameoverRect)
                start = 2

            if (crow7_x < bird_x + birdWidth) and (bird_x < crow7_x + crowWidth) and (crow7_y < bird_y + birdHeight) and (bird_y < crow7_y + crowHeigth):
                SURFACE.blit(gameover,gameoverRect)
                start = 2

            if (crow8_x < bird_x + birdWidth) and (bird_x < crow8_x + crowWidth) and (crow8_y < bird_y + birdHeight) and (bird_y < crow8_y + crowHeigth):
                SURFACE.blit(gameover,gameoverRect)
                start = 2

            if (crow9_x < bird_x + birdWidth) and (bird_x < crow9_x + crowWidth) and (crow9_y < bird_y + birdHeight) and (bird_y < crow9_y + crowHeigth):
                SURFACE.blit(gameover,gameoverRect)
                start = 2

            if (crow10_x < bird_x + birdWidth) and (bird_x < crow10_x + crowWidth) and (crow10_y < bird_y + birdHeight) and (bird_y < crow10_y + crowHeigth):
                SURFACE.blit(gameover,gameoverRect)
                start = 2

            if (aimMissile_x < bird_x + birdWidth) and (bird_x < aimMissile_x + missileWidth) and (aimMissile_y < bird_y + birdHeight) and (bird_y < aimMissile_y + missileHight):
                SURFACE.blit(gameover2,gameoverRect2)
                start = 2

            #撃墜判定
            if (missile_x < crow1_x) and (crow1_x < missile_x + 100) and (missile_y < crow1_y) and (crow1_y < missile_y + 100):
                crow1_x += 1000
                crow1_y = random.randint(0,screenHeight-50)
                scoreCount += 1
                killCount += 1

            if (missile_x < crow2_x) and (crow2_x < missile_x + 100) and (missile_y < crow2_y) and (crow2_y < missile_y + 100):
                crow2_x += 1000
                crow2_y = random.randint(0,screenHeight-50)
                scoreCount += 1
                killCount += 1

            if (missile_x < crow3_x) and (crow3_x < missile_x + 100) and (missile_y < crow3_y) and (crow3_y < missile_y + 100):
                crow3_x += 1000
                crow3_y = random.randint(0,screenHeight-50)
                scoreCount += 1
                killCount += 1

            if (missile_x < crow4_x) and (crow4_x < missile_x + 100) and (missile_y < crow4_y) and (crow4_y < missile_y + 100):
                crow4_x += 1000
                crow4_y = random.randint(0,screenHeight-50)
                scoreCount += 1
                killCount += 1

            if (missile_x < crow5_x) and (crow5_x < missile_x + 100) and (missile_y < crow5_y) and (crow5_y < missile_y + 100):
                crow5_x += 1000
                crow5_y = random.randint(0,screenHeight-50)
                scoreCount += 1
                killCount += 1

            if (missile_x < crow6_x) and (crow6_x < missile_x + 100) and (missile_y < crow6_y) and (crow6_y < missile_y + 100):
                crow6_x += 1000
                crow6_y = random.randint(0,screenHeight-50)
                scoreCount += 1
                killCount += 1

            if (missile_x < crow7_x) and (crow7_x < missile_x + 100) and (missile_y < crow7_y) and (crow7_y < missile_y + 100):
                crow7_x += 1000
                crow7_y = random.randint(0,screenHeight-50)
                scoreCount += 1
                killCount += 1

            if (missile_x < crow8_x) and (crow8_x < missile_x + 100) and (missile_y < crow8_y) and (crow8_y < missile_y + 100):
                crow8_x += 1000
                crow8_y = random.randint(0,screenHeight-50)
                scoreCount += 1
                killCount += 1

            if (missile_x < crow9_x) and (crow9_x < missile_x + 100) and (missile_y < crow9_y) and (crow9_y < missile_y + 100):
                crow9_x += 1000
                crow9_y = random.randint(0,screenHeight-50)
                scoreCount += 1
                killCount += 1

            if (missile_x < crow10_x) and (crow10_x < missile_x + 100) and (missile_y < crow10_y) and (crow10_y < missile_y + 100):
                crow10_x += 1000
                crow10_y = random.randint(0,screenHeight-50)
                scoreCount += 1
                killCount += 1

            #難易度実装
            if (scoreCount%10 == 0) and (scoreCount != 0):
                crowSpeedAdd += 1
                scoreCount = 0
                difficulty += 1


            scoreboard = scoreboardFont.render(("difficulty:" + str(difficulty)), True,(0,0,0))
            SURFACE.blit(scoreboard,(0,0))
            killScore = scoreboardFont.render(("Kill Count:" + str(killCount)), True,(0,0,0))
            SURFACE.blit(killScore,(0,50))
            chargeTime= scoreboardFont.render(("Charge:" + str(charge) + "%"), True,(0,0,0))
            SURFACE.blit(chargeTime,(0,100))

            # 画面アップデート
            pygame.display.update()
            FPSCLOCK.tick(2000)

            #ミサイルタイマー
            if missileTimer > 0:
                missileTimer -=1
                        

        # if start == 1:
        #ゲームオーバー処理 
        if start == 2:
            # イベント処理
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN :
                        start = 0

        if start == 3:
            # イベント処理
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN :
                        start = 0

# while end
if __name__ == '__main__':
    main()