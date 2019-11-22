import sys
import pygame
import random
from pygame.locals import QUIT , Rect , KEYDOWN , K_LEFT , K_RIGHT , K_UP , K_DOWN , K_RETURN

pygame.init()
pygame.key.set_repeat(5,5)

screenWidth = 1000
screenHeight = 600
SURFACE = pygame.display.set_mode((screenWidth,screenWidth))

pygame.display.set_caption("鳥が動くプロ")

cloud = pygame.image.load("img/cloud.png")
chickin = [pygame.image.load("img/konno.png"),pygame.image.load("img/konno.png"),pygame.image.load("img/konno.png"), pygame.image.load("img/bird_3.png")]
    
building = [pygame.image.load("img/building1.png"),pygame.image.load("img/building2.png"),pygame.image.load("img/building3.png")]

crow = pygame.image.load("img/crow.png")




cloudWidth = 235
cloudHeight = 150
birdWidth = 70
birdHeight = 60
buildingWidth = [95,42,45]
buildingheight = [200,210,84]
crowWidth = 50
crowHeight = 39


scoreboardFont = pygame.font.SysFont("Meiryo",50)

gameoverFont = pygame.font.SysFont("Meiryo",100)
gameover = gameoverFont.render("GAME OVER ￥ Push Enter",True,(255,0,0))
gameoverRect = gameover.get_rect(center = (screenWidth/2,screenHeight/2))

class buildings():

    def __init__(self,num,speed):
        self.number = num
        self.moveSpeed = speed
        self.pic =building[num]
        self.builX = screenWidth - ((num + 1) * 500)
        self.builY = screenHeight - buildingheight[num] -40
    
    def buildingMoves(self):
        self.builX -= self.moveSpeed
        if self.builX <= (0 - buildingWidth[self.number]):
            self.builX = screenWidth

def main():
    start = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN :
                    start = 0
        if start == 0:

            cloud_x = 0

            building_0 = buildings(0,0.5)
            building_1 = buildings(1,0.5)
            building_2 = buildings(2,0.5)

            bird_x = 30
            bird_y = 200
            chickinimg = 0
            chickinimgCount = 0

            crow_x = screenWidth
            crow_y = random.randint(0,screenHeight - 50)
            crowSpeedAdd = 0



            score = 0
            scoreCount = 0

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
            
            SURFACE.fill((40,128,215))

            start_pos = (0,screenHeight - 25)
            end_pos = (screenWidth,screenHeight - 25)
            pygame.draw.line(SURFACE,(0,255,0),start_pos,end_pos,50)

            if cloud_x > 0 - cloudWidth:
                cloud_x -= 0.8
            else:
                cloud_x = screenWidth
            SURFACE.blit(cloud,(cloud_x,0))

            building_0.buildingMoves()
            SURFACE.blit(building_0.pic,(building_0.builX,building_0.builY))
            building_1.buildingMoves()
            SURFACE.blit(building_1.pic,(building_1.builX,building_1.builY))
            building_2.buildingMoves()
            SURFACE.blit(building_2.pic,(building_2.builX,building_2.builY))
            
            if crow_x < 0 - crowWidth:
                crow_x = screenWidth
                crow_y = random.randint(0,screenHeight - 50)
                crowSpeedAdd += 1

            
            crow_x -= 1 + crowSpeedAdd
            SURFACE.blit(crow,(crow_x,crow_y))


            if bird_x > screenWidth:
                bird_x = 0 - birdWidth
            if bird_x < 0 - birdWidth:
                bird_x = screenWidth
            if bird_y > screenHeight - birdHeight - 25:
                bird_y = screenHeight - birdHeight - 25
            if bird_y < 0:
                bird_y = 0
            
            if chickinimgCount == 20:
                chickinimg = (chickinimg + 1) % 4
                chickinimgCount = 0
            else:
                chickinimgCount += 1
            
            SURFACE.blit(chickin[chickinimg],(bird_x,bird_y))

            if (crow_x < bird_x + birdWidth) and (bird_x < crow_x + crowWidth) and (crow_y < bird_y + birdHeight) and (bird_y < crow_y + crowHeight):
                SURFACE.blit(gameover,gameoverRect)
                start = 2

            scoreCount += 1
            if scoreCount == 20:
                score += 1
                scoreCount = 0

            scoreboard = scoreboardFont.render(str(score),True,(0,0,0))
            SURFACE.blit(scoreboard,(0,0))

            pygame.display.update()

        if start == 2:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        start = 0

if __name__ =='__main__':
    main()
