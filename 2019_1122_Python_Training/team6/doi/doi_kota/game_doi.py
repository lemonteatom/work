
import sys
import pygame
import random
from pygame.locals import*


pygame.init()
pygame.key.set_repeat(5,5)

#画面サイズ
screenWidht = 1000
screenHeight = 600
SURFACE = pygame.display.set_mode((screenWidht,screenHeight))    

# タイトルの設定
pygame.display.set_caption("シューティング")

# 画像ロード
inu = pygame.image.load("img/inu.png")
chicken = [pygame.image.load("img/bird_0.png"), \
    pygame.image.load("img/bird_1.png"), \
    pygame.image.load("img/bird_2.png"), \
    pygame.image.load("img/bird_3.png")]
ball = pygame.image.load("img/ball.png")
beam = pygame.image.load("img/beam.png")
robo = pygame.image.load("img/robo1.png")


# 画像サイズの設定
inuWidth = 235
inuHeight = 150
birdWidth = 70
birdHeight = 60
roboWidth = 100
roboHeight = 200
beamWidth = 90
beamHeight = 50
ballWidth = 25
ballHeight = 25

# スコアの文字の設定
scoreboardFont = pygame.font.SysFont("Meiryo",50)

# ゲームオーバーの文字設定
gameoverFont = pygame.font.SysFont("Meiryo",100)
gameover = gameoverFont.render("GAME OVER \ Push Enter", \
    True, (255,0,0) )
gameoverRect = gameover.get_rect(center = \
    (screenWidht/2, screenHeight/2))

class Ball():

    # 引数1：使用するビルの画像0～2　
    # 引数2：ビルの移動速度 
    def __init__(self,pos_x,pos_y,speed=8):
        self.movespeed = speed
        self.pos_x = pos_x
        self.pos_y = pos_y

        

def main():
    start = 0
    ballList = []

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
            inu_x = 0

            
            # 鳥の初期値
            bird_x = 30
            bird_y = 200
            chickenimg = 0
            chickenimgCount = 0
            # ロボの初期値
            robo_x = 600 
            robo_y = 80


            # ビームの初期値
            beam_x = screenWidht
            beam_y = random.randint(0,screenHeight-50)
            beamSpeedAdd = 0

            #ボールの初期値
            ball_X = 0
            ball_Y = 0

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
            SURFACE.fill((0,0,0)) 

            # 地面の描写
            start_pos = (0,screenHeight-25)
            end_pos = (screenWidht,screenHeight-25)
            pygame.draw.line(SURFACE,(230,234,230),start_pos,end_pos,50)

            # 雲の描写
            # 画面端までいったら画像を左端からスタートする
            if inu_x > 0 - inuWidth:
                inu_x -= 0.8
            else:                       
                inu_x = screenWidht
            SURFACE.blit(inu,(inu_x,0))


            # ビームの描写
            if beam_x < 0 - beamWidth:
                beam_x = screenWidht
                beam_y = random.randint(0,screenHeight-50)

            beam_x -= 20
            SURFACE.blit(beam,(beam_x,beam_y))
            
            #ロボの描写
            SURFACE.blit(robo,(robo_x,robo_y))

            #ボールの描写
            if pressed_keys[K_SPACE]:
                ballList.append(Ball(bird_x+70,bird_y+20))
            
            for b in ballList:
                b.pos_x = b.pos_x + b.movespeed
            
            for b in ballList:
                SURFACE.blit(ball,(b.pos_x,b.pos_y))

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
            if (beam_x < bird_x + birdWidth) and  \
                (bird_x < beam_x + beamWidth) and  \
                (beam_y < bird_y + birdHeight) and  \
                (bird_y < beam_y + beamHeight):
                SURFACE.blit(gameover,gameoverRect)
                start = 2
            
            for b in ballList:
            # あたり判定（ロボ）
                if (b.pos_x < robo_x + roboWidth) and  \
                    (robo_x < b.pos_x + ballWidth) and  \
                    (b.pos_y < robo_y + roboHeight) and  \
                    (robo_y < b.pos_y + ballHeight):
                    score += 0.01

                elif(b.pos_x < robo_x + roboWidth) and  \
                    (robo_x < b.pos_x + ballWidth) and  \
                    (b.pos_y  > robo_y + 300) and  \
                    (robo_y < b.pos_y + ballHeight):
                    score += 0.005
                
            

            # スコアの表示
            #scoreCount += 1
            #if scoreCount == 20:
            #    score += 1
            #    scoreCount = 0

            scoreboard = scoreboardFont.render(str(round(score)), \
                True,(255,255,255))
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