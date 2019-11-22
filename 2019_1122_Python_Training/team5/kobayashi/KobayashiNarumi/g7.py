import sys
import pygame
import random
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_RETURN

pygame.init()
pygame.key.set_repeat(5,5)

screenwidth = 600
screenHeight = 840
SURFACE = pygame.display.set_mode((screenwidth,screenHeight))

pygame.display.set_caption("散歩")
#画像ロード
#cloud = pygame.image.load("img/scloud.png")
chicken = [pygame.image.load("img/sdog.png")]
#building = [pygame.image.load("img/building1.png"),pygame.image.load("img/building2.png"),pygame.image.load("img/building3.png")]
crow = pygame.image.load("img/hari.png")

#画像サイズ
#cloudwidth = 106
#cloudHeight = 67
birdWidth = 63
birdHeight = 114
#buildingwidht = [95,42,45]
#buildingheight = [200,210,84]
crowWidth = 50
crowHeight = 39

#文字

scoreboardFont = pygame.font.SysFont("Meiryo",50)

gameoverFont = pygame.font.Font("姫明朝ともえごぜんmini.otf",30)
gameover = gameoverFont.render(" 満足  まだ散歩する",True,(255,0,0))
gameoverRect = gameover.get_rect(center = (screenwidth/2,screenHeight/2))


#class buildings():
 #   def __init__(self,num,speed):
  #      self.number = num
   #     self.moveSpeed = speed
    #    self.pic = building[num]
     #   self.builX = ((num + 1) * 70)
      #  self.builY = screenHeight - buildingheight[num] - 40

#    def buildingMoves(self):
 #       self.builY -= self.moveSpeed
  #      if self.builX <= (0 - buildingwidht[self.number]):
   #         self.builX = screenwidth


def main():
    start = 0

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    start = 0
        if start == 0:

            #データ初期化
 #           cloud_x = screenHeight
  #          cloud_y = random.randint(0,screenHeight-50)
            #ビル初期化
 #           building_0 = buildings(0,0.5)
  #          building_1 = buildings(1,0.5)
   #         building_2 = buildings(2,0.5)

            #鳥初期化
            bird_x = 250
            bird_y = 15
            chickenimg = 0
            chickenimgCount = 0

            #カラス初期化
            crow_x = random.randint(0,screenwidth)
            crow_y = screenHeight
            crowSpeedAdd = 0

            score = 0
            scoreCount = 0

            #ゲーム開始する
            start = 1

        if start == 1:

            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_LEFT]:
                bird_x -= 5
            if pressed_keys[K_RIGHT]:
                bird_x += 5
            if pressed_keys[K_UP]:
                bird_y -= 5
            if pressed_keys[K_DOWN]:
                bird_y += 5

            SURFACE.fill((134,158,130))

            #地面の描写
  #          start_pos = (0,screenHeight-25)
   #         end_pos = (screenwidth,screenHeight-25)
    #        pygame.draw.line(SURFACE,(0,255,0),start_pos,end_pos,50)

            #雲の描写
   #         if cloud_x > 0 -cloudwidth:
    #            cloud_x = 0.8
     #       else:
      #          cloud_x = screenwidth
       #     SURFACE.blit(cloud,(cloud_x,0))

            #ビルの描写
   #         building_0.buildingMoves()
    #        SURFACE.blit(building_0.pic,(building_0.builX,building_0.builY))

     #       building_2.buildingMoves()
      #      SURFACE.blit(building_1.pic,(building_2.builX,building_2.builY))

            #カラスの描写
            if crow_y < 0 - crowHeight:
                crow_x = random.randint(0,screenwidth)
                crow_y = screenHeight
                #crowSpeedAdd += 1
            crow_y -= 1 + crowSpeedAdd
            #?
            SURFACE.blit(crow,(crow_x,crow_y))

            #鳥の描写
            if bird_x > screenwidth:
                bird_x = 0 - birdWidth
            if bird_x < 0 - birdWidth :
                bird_x = screenwidth
            if bird_y > screenHeight - birdHeight -25:
                bird_y = screenHeight - birdHeight -25
            if bird_y < 0:
                bird_y = 0



            SURFACE.blit(chicken[chickenimg],(bird_x,bird_y))

            #当たり判定
            if(crow_x < bird_x + birdWidth) and (bird_x < crow_x + crowWidth) and (crow_y < bird_y + birdHeight) and (bird_y < crow_y + crowHeight):
                SURFACE.blit(gameover,gameoverRect)
                score += 1

            scoreboard =  scoreboardFont.render(str(score),True,(0,0,0))
            SURFACE.blit(scoreboard,(0,0))

            pygame.display.update()

        #ゲームオーバー処理
        if start < 400:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        start = 0

if __name__ == '__main__':
    main()
