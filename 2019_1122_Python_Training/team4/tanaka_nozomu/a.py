import pygame
from pygame.locals import *
import math
import sys
import random
from pygame.locals import QUIT , Rect,  \
        KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_RETURN


# 画面
SCREEN = Rect(0, 0, 600, 500)
screenWidht = 600
screenHeight = 500
SURFACE = pygame.display.set_mode((screenWidht,screenHeight))  
FPSCLOCK = pygame.time.Clock()

#ステージカウント(複数ステージにしたい)
stage = 1 #グローバル変数にステージカウントを置く

# ブロックオブジェクト
class Block(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.left = SCREEN.left + x * self.rect.width
        self.rect.top = SCREEN.top + y * self.rect.height
# バーオブジェクト
class Smbc(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN.bottom - 20

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]  
        self.rect.clamp_ip(SCREEN)                     

#ボールオブジェクト
class Ball(pygame.sprite.Sprite):
    def __init__(self, filename, smbc, blocks, speed, angle_left, angle_right):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.dx = self.dy = 0  
        self.smbc = smbc  
        self.blocks = blocks 
        self.update = self.start 
        self.speed = speed 
        self.angle_left = angle_left 
        self.angle_right = angle_right 

    #　ボールリセット
    def start(self):
        self.rect.centerx = self.smbc.rect.centerx
        self.rect.bottom = self.smbc.rect.top

        # ボール発射
        if pygame.mouse.get_pressed()[0] == 1:
            self.dx = 0
            self.dy = -self.speed
            self.update = self.move

    def move(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        # 壁との反射
        if self.rect.left < SCREEN.left:    # 左側
            self.rect.left = SCREEN.left
            self.dx = -self.dx              # 反転
        if self.rect.right > SCREEN.right:  # 右側
            self.rect.right = SCREEN.right
            self.dx = -self.dx
        if self.rect.top < SCREEN.top:      # 上側
            self.rect.top = SCREEN.top
            self.dy = -self.dy

        # パドルとの反射(左端:135度方向, 右端:45度方向, それ以外:線形補間)
        # 2つのspriteが接触しているかどうかの判定
        if self.rect.colliderect(self.smbc.rect) and self.dy > 0:
            self.hit = 0                                # 連続ヒットを0に戻す
            (x1, y1) = (self.smbc.rect.left - self.rect.width, self.angle_left)
            (x2, y2) = (self.smbc.rect.right, self.angle_right)
            x = self.rect.left                          # ボールが当たった位置
            y = (float(y2-y1)/(x2-x1)) * (x - x1) + y1  # 線形補間
            angle = math.radians(y)                     # 反射角度
            self.dx = self.speed * math.cos(angle)
            self.dy = -self.speed * math.sin(angle)
        
        # ボールと衝突したブロックリストを取得（Groupが格納しているSprite中から、指定したSpriteと接触しているものを探索）
        blocks_collided = pygame.sprite.spritecollide(self, self.blocks, True)
        if blocks_collided:  # 衝突ブロックがある場合
            oldrect = self.rect
            for block in blocks_collided:
                # 左衝突
                if oldrect.left < block.rect.left and oldrect.right < block.rect.right:
                    self.rect.right = block.rect.left
                    self.dx = -self.dx
                    
                # 右衝突
                if block.rect.left < oldrect.left and block.rect.right < oldrect.right:
                    self.rect.left = block.rect.right
                    self.dx = -self.dx

                # 上衝突
                if oldrect.top < block.rect.top and oldrect.bottom < block.rect.bottom:
                    self.rect.bottom = block.rect.top
                    self.dy = -self.dy

                #　下衝突
                if block.rect.top < oldrect.top and block.rect.bottom < oldrect.bottom:
                    self.rect.top = block.rect.bottom
                    self.dy = -self.dy
                    
def main():

    #ゲームスピードのカウント
    count = 0

    pygame.init()
    screen = pygame.display.set_mode(SCREEN.size)
    # 描画用のスプライトグループ
    group = pygame.sprite.RenderUpdates()  
    # 衝突判定
    blocks = pygame.sprite.Group()   
    # スプライトグループに追加    
    Smbc.containers = group
    Ball.containers = group
    Block.containers = group, blocks

    # ゲームオーバーの文字設定
    gameoverFont = pygame.font.SysFont("Meiryo",100)
    gameover = gameoverFont.render("haha( ^ ~ ^ )", True, (255,0,255%(count+1)) )
    gameoverRect = gameover.get_rect(center = (screenWidht/2, screenHeight/2))

    # スコアの文字の設定
    scoreboardFont = pygame.font.SysFont("Meiryo",50)

    # スコア表示
    score = 0
    scoreCount = 0
    scoreCount += 1
    if scoreCount == 20:
        score += 1
        coreCount = 0

    scoreboard = scoreboardFont.render(str(score), True,(0,0,0))
    SURFACE.blit(scoreboard,(0,0))

    smbc = Smbc("smbc.png")

    for x in range(1, 15):
        for y in range(1, 11):
            Block("money.png", x, y)

    # ボールを作成
    ball = Ball("life.png",smbc, blocks, 5, 135, 45)
    
    clock = pygame.time.Clock()
    
    while True:
        count = count + 0.05
        #だんだん早くなるように
        clock.tick(60+2*count) 

        #背景
        screen.fill((177,255,212))
        # 全てのスプライトグループを更新
        group.update()
        # 全てのスプライトグループを描画       
        group.draw(screen)
        pygame.display.update()

        if ball.rect.top > SCREEN.bottom:
            SURFACE.blit(gameover,gameoverRect)

        # 画面アップデート
        pygame.display.update()



        # キーイベント（終了）
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                ball.update = ball.start
                

if __name__ == "__main__":
    main()