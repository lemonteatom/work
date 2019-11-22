# ***********************************************************
# カラスが飛びスコアが加算され、
# カラスに当たるとゲームオーバーになるプログラム
# ***********************************************************

import sys
import pygame
import random
import TitleGraphic
from pygame.locals import QUIT , Rect,  \
        KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_RETURN,K_SPACE

pygame.init()
pygame.key.set_repeat(5,5)


#画面サイズ
screenWidth = 1000
screenHeight = 600
SURFACE = pygame.display.set_mode((screenWidth,screenHeight))    
FPSCLOCK = pygame.time.Clock()
# タイトルの設定
pygame.display.set_caption("Flying Bird")

# 画像ロード
cloud = pygame.image.load("img/cloud.png")
chicken = [pygame.image.load("img/bird_0.png"), \
    pygame.image.load("img/bird_1.png"), \
    pygame.image.load("img/bird_2.png"), \
    pygame.image.load("img/bird_3.png"), \
    pygame.image.load("img/dead.png")]

building = [pygame.image.load("img/building1.png"), \
    pygame.image.load("img/building2.png"), \
    pygame.image.load("img/building3.png")]

#敵の画像をもらう
crow = pygame.image.load("img/crow.png")
firebird = pygame.image.load("img/bluebird_enjou.png")
firebird = pygame.transform.smoothscale(firebird,(50,50))
enemies = [pygame.image.load("img/crow.png"),firebird]


#弾の画像をもらう
bullet = pygame.image.load("img/bullet.png")
bullet = pygame.transform.smoothscale(bullet,(25,25))
bombEffect = pygame.image.load("img/bakuhatsu.png")
bombEffect = pygame.transform.smoothscale(bombEffect,(75,75))

#ハートの画像をもらう
heart = pygame.image.load("img/heart_shiny.png")
heart = pygame.transform.smoothscale(heart,(50,50))

#爆弾の画像をもらう
bomb = pygame.image.load("img/bakudan.png")
bomb = pygame.transform.smoothscale(bomb,(50,50))

# 画像サイズの設定
cloudWidth = 235
cloudHeight = 150
birdWidth = 70
birdHeight = 60
buildingwidth = [95,42,45]
buildingheight = [200,210,84]
crowWidth = 50
crowHeigth = 39
bulletHeight = 25
bulletWidth = 25
bombsize = 50

# スコアの文字の設定
scoreboardFont = pygame.font.SysFont("Meiryo",50)

# 時間の文字の設定
timeboardFont = pygame.font.SysFont("Meiryo",50)

# 撃墜数の文字の設定
defeatboardFont = pygame.font.SysFont("Meiryo",50)

# クリアの文字設定
clearFont = pygame.font.SysFont("Meiryo",100)
clear = clearFont.render("Clear \ YOU ACHIEVED 1000", \
    True, (255,255,0) )
clearRect = clear.get_rect(center = \
    (screenWidth/2, screenHeight/2)) 
    
# ゲームオーバーの文字設定
gameoverFont = pygame.font.SysFont("Meiryo",100)
gameover = gameoverFont.render("GAME OVER \ Push Enter", \
    True, (255,0,0) )
gameoverRect = gameover.get_rect(center = \
    (screenWidth/2, screenHeight/2))


class Hearts():
    heartTime = 0 
    const = 1500
    def __init__(self,pos_x,pos_y,speed=1,number=0,collision_flag=True):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.moveSpeed = speed
        self.number = number
        self.pic = heart
        self.collision_flag = collision_flag
        
    def heartMoves(self):
        self.pos_x -= self.moveSpeed
        
        if self.pos_y <= 0:
            self.collision_flag = not self.collision_flag
        if self.pos_y >= 600:
            self.collision_flag = not self.collision_flag

        if self.collision_flag:
            self.pos_y -= (self.const*2)/3000
        else:
            self.pos_y += (self.const*2)/3000

class Bombs():
    bombTime = 0
    def __init__(self,pos_x,pos_y,speed=1.5):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.moveSpeed = speed

    def bombMoves(self):
        self.pos_y += self.moveSpeed  
            
class Enemies():
    enemieTime = 0
    def __init__(self,pos_x,pos_y,speed=2):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.moveSpeed = speed

    def enemieMoves(self):
        self.pos_x -= self.moveSpeed

class Buildings():

    # 引数1：使用するビルの画像0～2　
    # 引数2：ビルの移動速度 
    def __init__(self,num,speed):
        self.number = num
        self.moveSpeed = speed
        self.pic = building[num]
        self.builX = screenWidth - ((num + 1) * 500)
        self.builY = screenHeight - buildingheight[num] - 40

    def buildingMoves(self):
        self.builX -= self.moveSpeed
        if self.builX <= (0 - buildingwidth[self.number]):
            self.builX = screenWidth

class Bullets():
    BulletCounts = 0
    bulletTime = 0
    #引数1:x座標
    #引数2:y座標
    #引数3:スピード(default:1)
    def __init__(self,pos_x,pos_y,speed=5):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.movespeed = speed
        Bullets.BulletCounts = Bullets.BulletCounts + 1 
    
def main():
    stage_flag = 0
    time = 0
    defeat_flag = 0
    defeatcount = 0
    init_lifepoint = 3
    clearscore = 1000
    buildingList = []
    bulletList = []
    enemieList = []
    bombList = []
    heartList = []
    while True:
        time = pygame.time.get_ticks() / 1000
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN :
                    stage_flag = 0
        if stage_flag == 0:

            # データの初期値
            # 雲の初期値
            cloud_x = 0

            # ビルの初期化
            buildingList.clear()
            buildingList.append(Buildings(0,0.5))
            buildingList.append(Buildings(1,0.5))
            buildingList.append(Buildings(2,0.5))

            # 鳥の初期値
            bird_x = 30
            bird_y = 200
            chickenimg = 0
            chickenimgCount = 0

            # カラスの初期値
            crow_x = screenWidth
            crow_y = random.randint(0,screenHeight-50)
            crowSpeedAdd = 0

            #敵と弾の初期化
            bulletList.clear()
            enemieList.clear()
            bombList.clear()

            # スコアの初期化
            score = 0
            scoreCount = 0
            defeatcount = 0

            # ライフの初期化
            lifepoint = init_lifepoint
            # ゲームを開始する
            stage_flag = 1

        if stage_flag == 1:
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

            # 地面の指定
            stage_flag_pos = (0,screenHeight-25)
            end_pos = (screenWidth,screenHeight-25)

            # 雲のコントロール
            # 画面端までいったら画像を左端からスタートする
            if cloud_x > 0 - cloudWidth:
                cloud_x -= 0.8
            else:                       
                cloud_x = screenWidth
            

            # ビルの移動
            for b in buildingList:
                b.buildingMoves()

            # カラスの移動
            if crow_x < 0 - crowWidth:
                crow_x = screenWidth
                crow_y = random.randint(0,screenHeight-50)
                crowSpeedAdd += 0

            crow_x -= 1 + crowSpeedAdd

            # 鳥の移動
            # 左右の画面端は反対側へ、上下の画面端は行き止まり
            if bird_x > screenWidth :
                bird_x = 0 - birdWidth
            if bird_x < 0 - birdWidth :
                bird_x = screenWidth
            if bird_y > screenHeight - birdHeight -25 :
                bird_y = screenHeight - birdHeight -25
            if bird_y < 0 :
                bird_y = 0
            
            #鳥のアニメーションをコントロール

            if chickenimgCount == 20:
                chickenimg = (chickenimg + 1 )% 4
                chickenimgCount = 0
            else:
                chickenimgCount += 1

            #ミサイルの生成  
            if pressed_keys[K_SPACE]:
                if  time - Bullets.bulletTime >= 0.5:     
                    bulletList.append(Bullets(bird_x,bird_y))
                    Bullets.bulletTime = time
            
            #ミサイルの移動
            for b in bulletList:
                b.pos_x = b.pos_x + b.movespeed 
            
            #敵の生成
            if time - Enemies.enemieTime >= 2.0:
                enemieList.append(Enemies(screenWidth,random.randint(0,screenHeight-50)))
                Enemies.enemieTime = time
            
            #敵の移動
            for e in enemieList:
                e.enemieMoves()

            #爆弾の生成
            if time - Bombs.bombTime >= 2.5:
                bombList.append(Bombs(random.randint(0,screenWidth-50),0))
                Bombs.bombTime = time
            
            #爆弾の移動
            for b in bombList:
                b.bombMoves()

            #ハートの生成
            if time - Hearts.heartTime >= 10.0:
                heartList.append(Hearts(screenWidth,random.randint(0,screenHeight-50)))
                Hearts.heartTime = time

            #ハートの移動
            for h in heartList:
                h.heartMoves()

            # あたり判定
            if (crow_x < bird_x + birdWidth) and  \
                (bird_x < crow_x + crowWidth) and  \
                (crow_y < bird_y + birdHeight) and  \
                (bird_y < crow_y + crowHeigth):
                lifepoint -= 1
                crow_x = screenWidth
                crow_y = random.randint(0,screenHeight-50)
                #GameOverFlagを立てる
                if lifepoint <= 0:
                    stage_flag = 2

            # エネミーの当たり判定
            for e in enemieList:
                if(e.pos_x < bird_x + birdWidth) and  \
                (bird_x < e.pos_x + crowWidth) and  \
                (e.pos_y < bird_y + birdHeight) and  \
                (bird_y < e.pos_y + crowHeigth):
                    lifepoint -= 1
                    tmp = e
                    enemieList.remove(tmp)
                    #GameOverFlagを立てる
                    if lifepoint <= 0:
                        stage_flag = 2
            
            # ボムの当たり判定だよ～
            for b in bombList:
                if(b.pos_x < bird_x + birdWidth) and  \
                (bird_x < b.pos_x + bombsize) and  \
                (b.pos_y + bombsize > bird_y) and \
                (bird_y + birdHeight > b.pos_y ):
                    lifepoint -= 1
                    tmp = b
                    bombList.remove(tmp)
                    #GameOverFlagを立てる
                    if lifepoint <= 0:
                        stage_flag = 2
            
            # ミサイルの当たり判定
            for b in bulletList:
                if (crow_x < b.pos_x + bulletWidth) and  \
                    (b.pos_x < crow_x + crowWidth) and \
                    (crow_y < b.pos_y + bulletHeight) and  \
                    (b.pos_y < crow_y + crowHeigth):
                    pygame.time.wait(50)
                    defeat_flag = 1
                    defeatcount += 1
                    crow_x = screenWidth
                    crow_y = random.randint(0,screenHeight-50)
                    tmp = b 
                    bulletList.remove(tmp)
                    score += 50

            #　ハートの当たり判定
            for h in heartList:
                if(h.pos_x < bird_x + birdWidth) and  \
                (bird_x < h.pos_x + crowWidth) and  \
                (h.pos_y < bird_y + birdHeight) and  \
                (bird_y < h.pos_y + crowHeigth):
                    pygame.time.wait(100)
                    lifepoint += 1
                    tmp = h 
                    heartList.remove(tmp)               

            # スコアの計算とSurface作成
            scoreCount += 1
            if scoreCount == 20:
                score += 1
                scoreCount = 0

            scoreboard = scoreboardFont.render( "SCORE:"+ str(score), \
                True,(0,0,0))

            #　時間のSurface作成
            timeboard = timeboardFont.render( "TIME:" + str(int(time)), \
                True,(0,0,0))
            
            #　撃墜数のSurface作成
            defeatboard = defeatboardFont.render("KILL:" + str(defeatcount), \
                True,(255,0,0))

        #ゲームオーバー処理--------------------------------------------------------------
        if stage_flag == 2:
            chickenimg = 4
            if bird_y < 600:
                bird_y += 1  
        
            # イベント処理
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN :
                        stage_flag = 0
                        pygame.init()

        #クリア判定---------------------------------
        if score >= clearscore:
            stage_flag = 3
        
        if stage_flag == 3:
            # イベント処理
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN :
                        stage_flag = 0
                        pygame.init()
        #描画-----------------------------------------------------------------
        #色
        SURFACE.fill((40,128,215))
        #地面 
        pygame.draw.line(SURFACE,(0,255,0),stage_flag_pos,end_pos,50)
        #雲
        SURFACE.blit(cloud,(cloud_x,0))
        #建物
        for b in buildingList:
            SURFACE.blit(b.pic, \
            (b.builX,b.builY))
        #カラス（敵1）
        SURFACE.blit(enemies[0],(crow_x,crow_y))
        #敵
        for e in enemieList:
            SURFACE.blit(enemies[1],(e.pos_x,e.pos_y))
        #自機
        SURFACE.blit(chicken[chickenimg],(bird_x,bird_y))
        #ミサイル
        for b in bulletList:
            SURFACE.blit(bullet,(b.pos_x,b.pos_y))
            if defeat_flag == 1:
                SURFACE.blit(bombEffect,(b.pos_x,b.pos_y))
                defeat_flag = 0
        
        #ハート
        for h in heartList:
            SURFACE.blit(h.pic,(h.pos_x,h.pos_y))
        #爆弾
        for b in bombList:
            SURFACE.blit(bomb,(b.pos_x,b.pos_y))
        #スコアボード
        SURFACE.blit(scoreboard,(0,0))
        #タイムボード
        SURFACE.blit(timeboard,(850,550))
        #撃墜数
        SURFACE.blit(defeatboard,(0,50)) 
        #ライフポイント
        for h in range(0,lifepoint):
            SURFACE.blit(heart,(0+(50*h),550))
        #ゲームオーバー画面
        if stage_flag == 2:
            SURFACE.blit(gameover,gameoverRect)  
        #クリア画面
        if stage_flag == 3:
            SURFACE.blit(clear,clearRect)
        #アプデ
        pygame.display.update()
        #描画ここまで---------------------------------------------------------------    

# while end
if __name__ == '__main__':
    TitleGraphic.main()
    main()