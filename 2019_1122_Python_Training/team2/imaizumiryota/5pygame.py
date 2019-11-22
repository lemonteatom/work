



import sys
import pygame
import random
from pygame.locals import QUIT,Rect,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN,K_RETURN


pygame.init()
pygame.key.set_repeat(5,5)

#画面サイズ
screenWidth=1000
screenHeight=600
SURFACE = pygame.display.set_mode((screenWidth,screenHeight))

#タイトルの設定
pygame.display.set_caption("鳥が動くゲーム")

#画面ロード
cloud = pygame.image.load("img/cloud.png")
bird = pygame.image.load("img/figure_sleeping.png")
chicken = [pygame.image.load("img/figure_sleeping.png"),pygame.image.load("img/figure_sleeping.png") \
            ,pygame.image.load("img/figure_sleeping.png"),pygame.image.load("img/figure_sleeping.png"),]
building =[pygame.image.load("img/building1.png"),pygame.image.load("img/building2.png"),pygame.image.load("img/building3.png")]
crow = pygame.image.load("img/crow.png")
company = pygame.image.load("img/company.PNG")
beer = pygame.image.load("img/eeeeel.png")

#画面サイズの設定
cloudWidth = 235
cloudHeirht = 150
birdWidth = 70
birdHeight=60
buildingwidth = [95,42,45]
buildingheight = [200,210,84]
crowWidth = 50
crowHeigth = 39
companyWidth = 0
companyHeight = 0
beerWidth = 0
beerHeight = 0

#スコアの表示
scoreboardFont = pygame.font.SysFont("Meiryo",50)

#lifeの表示
lifeboardFont = pygame.font.SysFont("Meiryo",50)

#game over表示
gameoverFont = pygame.font.SysFont("Meiryo",100)
gameover = gameoverFont.render("GAME OVER \ PUSH ENTER", True, (255,0,0))
gameoverRect = gameover.get_rect(center = (screenWidth/2,screenHeight/2))

#おめでとうと表示
congFont = pygame.font.SysFont("Meiryo",150)
cong = congFont.render("Congratulations!", True, (255,215,0))
congRect = cong.get_rect(center = (screenWidth/2,screenHeight/2))

class buildings():
    #引数１:使用するビルの画像０－２
    #引数２:ビルの移動速度
    def __init__(self,num,speed):
        self.number = num
        self.moveSpeed = speed
        self.pic = building[num]
        self.builX = screenWidth - ((num+1)*500)
        self.builY = screenHeight - buildingheight[num] - 40

    def buildingMoves(self):
        self.builX -= self.moveSpeed
        if self.builX <= (0 - buildingwidth[self.number]):
            self.builX = screenWidth

def main():

    #データの初期化

    start = 0
    life = 0
    logo =pygame.image.load("img/zimu.png")
    SURFACE.blit(logo , (0,0))
    while True:
        #event
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        start = 0
        if start == 0:
                #雲の初期化
                cloud_x = 0
                #鳥の初期化
                bird_x = 30
                bird_y = 200
                chickenimg = 0
                chickenimgCount = 0
                #ビルの初期化
                building_0 = buildings(0,0.5)
                building_1 = buildings(1,0.5)
                building_2 = buildings(2,0.5)
                #カラスの初期化
                crow_x = screenWidth
                crow_y = random.randint(0,screenHeight-50)
                crowSpeedAdd = 0
                #弊社の初期化
                company_x = screenWidth
                company_y = random.randint(0,screenHeight-50)
                companySpeedAdd = 0
                #スコアの処理
                score = 0
                scoreCount = 0
                #ビーるの初期化
                beer_x = screenWidth
                beer_y = random.randint(0,screenHeight-50)
                beerSpeedAdd = 0

                #ゲームを開始する
                start = 1
                life = 0

        if start == 1:
                #押されているキーをCHK
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

                #メインプログラム
                #画面背景カラー
                SURFACE.fill((40,128,215))

                #画面の描写
                start_pos = (0,screenHeight-25)
                end_pos = (screenWidth,screenHeight-25)
                pygame.draw.line(SURFACE,(0,255,0),start_pos,end_pos,50)

                #drow cloud
                #画面端までいったら画像を右端からスタートする
                if cloud_x > 0-cloudWidth:
                    cloud_x -= 0.8
                else:
                    cloud_x = screenWidth
                    SURFACE.blit(cloud,(cloud_x,0))
                #drow building
                building_0.buildingMoves()
                SURFACE.blit(building_0.pic,(building_0.builX,building_0.builY))
                building_1.buildingMoves()
                SURFACE.blit(building_1.pic,(building_1.builX,building_1.builY))
                building_2.buildingMoves()
                SURFACE.blit(building_2.pic,(building_2.builX,building_2.builY))

                #drow crow
                if crow_x < 0 - crowWidth:
                    crow_x = screenWidth
                    crow_y = random.randint(0,screenHeight-50)
                    crowSpeedAdd += 0.5
                crow_x -= 0.5 + crowSpeedAdd
                SURFACE.blit(crow,(crow_x,crow_y))

                #drow company
                if company_x < 0 - companyWidth:
                    company_x = screenWidth
                    company_y = random.randint(0,screenHeight-50)
                    companySpeedAdd += 1
                company_x -= 1 + companySpeedAdd
                SURFACE.blit(company,(company_x,company_y))

                #drow beer
                if beer_x < 0 - beerWidth:
                    beer_x = screenWidth
                    beer_y = random.randint(0,screenHeight-50)
                    beerSpeedAdd += 0.5
                beer_x -= 0.5 + beerSpeedAdd
                SURFACE.blit(beer,(beer_x,beer_y))

                #drow bird
                #左右の画面端は反対側へ、上下の画面端は行き止まり
                if bird_x > screenWidth:
                    bird_x = 0 - birdWidth
                if bird_x < 0 - birdWidth:
                    bird_x = screenWidth
                if bird_y > screenHeight - birdHeight -25:
                    bird_y = screenHeight - birdHeight -25
                if bird_y < 0:
                    bird_y = 0
                
                if chickenimgCount == 20:
                    chickenimg = (chickenimg + 1) % 4
                    chickenimgCount = 0
                else:
                    chickenimgCount += 1

                SURFACE.blit(chicken[chickenimg],(bird_x,bird_y))

                #あたり判定(カラス)
                if (crow_x < bird_x + birdWidth) and \
                    (bird_x < crow_x + crowWidth) and \
                    (crow_y < bird_y + birdHeight) and \
                    (bird_y < crow_y + crowHeigth):
                    SURFACE.blit(gameover,gameoverRect)
                    start = 2
                

                #あたり判定（弊社）
                if (company_x < bird_x + birdWidth) and \
                    (bird_x < company_x + companyWidth) and \
                    (company_y < bird_y + birdHeight) and \
                    (bird_y < company_y + companyHeight):
                    SURFACE.blit(gameover,gameoverRect)
                    start = 2

                #あたり判定（ビール）
                if (beer_x < bird_x + birdWidth) and \
                    (bird_x < beer_x + beerWidth) and \
                    (beer_y < bird_y + birdHeight) and \
                    (bird_y < beer_y + beerHeight):
                    beer_x = screenWidth
                    beer_y = random.randint(0,screenHeight-50)
                    life += 1

                #スコアの表示
                scoreCount += 1
                if scoreCount == 20:
                    score += 1
                    scoreCount = 0
                scoreboard = scoreboardFont.render(str(score),True,(0,0,0))
                SURFACE.blit(scoreboard,(0,0))

                #lifeの表示
                
                scoreboard = scoreboardFont.render(str(life),True,(255,0,0))
                SURFACE.blit(scoreboard,(0,100))

                #"life"という文字の表示
                message = lifeboardFont.render("life",True,(255,0,0))
                life_rect = message.get_rect(center = (30,90))
                SURFACE.blit(message,life_rect)
                #弊社との一騎打ち
                if life > 3:
                    crow_x < 0 - crowWidth
                    crow_x = screenWidth
                    crow_y = random.randint(0,screenHeight-50)
                    crowSpeedAdd -= 0.5
                    crow_x -= 0.5 + crowSpeedAdd
                    SURFACE.blit(crow,(crow_x,crow_y))

                #ゲームクリア
                if life > 9:
                    SURFACE.blit(cong,congRect)
                    start = 2
                #画面アップロード
                pygame.display.update()

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