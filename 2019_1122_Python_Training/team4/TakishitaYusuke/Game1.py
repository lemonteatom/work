import sys
import pygame
import random
from pygame.locals import QUIT, Rect, KEYDOWN, K_w, K_a, K_s, K_d, K_SPACE, K_RETURN, K_LSHIFT, K_1, K_2, K_3

pygame.init()
pygame.key.set_repeat(5,5)

screen_width = 1280     #画面サイズ横の変数
screen_height = 720     #画面サイズ縦の変数
SURFACE = pygame.display.set_mode((screen_width,screen_height))     #画面サイズ


pygame.display.set_caption("鳥が動くプログラム")        #ウィンドウに表示される名前


cloud = pygame.image.load("cloud.png")
bird = [pygame.image.load("bird_0.png"),pygame.image.load("bird_1.png"),pygame.image.load("bird_2.png"),pygame.image.load("bird_3.png")]
building = [pygame.image.load("building1.png"),pygame.image.load("building2.png"),pygame.image.load("building3.png")]
crow = pygame.image.load("crow.png")

cloud_width = 235
cloud_height = 150
bird_width = 70
bird_height = 60
crow_width = 50
crow_height = 40
building_width = [95,42,45]
building_height = [200,210,84]

scoreboard_font = pygame.font.SysFont("meiryo",50)

gameover_font = pygame.font.SysFont("meiryo",100)
gameover = gameover_font.render("GAME OVER:PUSH ENTER",True,(255,0,0))
gameover_rect = gameover.get_rect(center = (screen_width/2, screen_height/2))
first_font = pygame.font.SysFont("meiryo",100)
first = first_font.render("plz select bird coloer\n 1:blue\n 2:red",True,(255,0,0))
first_rect = first.get_rect(center = (screen_width/2, screen_height/2))


class Buildings():

    def __init__(self,num,speed):
        self.number = num
        self.moving_speed = speed
        self.picture = building[num]
        self.building_x = screen_width - ((num + 1) * 500)
        self.building_y = screen_height - building_height[num] - 40

    def move_building(self):
        self.building_x -= self.moving_speed
        if self.building_x <= (0 - building_width[self.number]):
            self.building_x = screen_width



def main():
    start = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif  event.type == KEYDOWN:
                if event.key == K_RETURN:
                    start = 0


        #if start == -1:
            #SURFACE.blit(first,first_rect)
            #if pressed_keys[K_2]:
                #bird = [pygame.image.load("C:/Users/user/Desktop/Python/Picture/bird_0_r.png"),pygame.image.load("C:/Users/user/Desktop/Python/Picture/bird_1_r.png"),pygame.image.load("C:/Users/user/Desktop/Python/Picture/bird_2_r.png"),pygame.image.load("C:/Users/user/Desktop/Python/Picture/bird_3_r.png")]


        if start == 0:
            bird_speed = 5
            cloud_x = 0
            building_0 = Buildings(0,0.5)
            building_1 = Buildings(1,0.5)
            building_2 = Buildings(2,0.5)
            bird_x = 30
            bird_y = 200
            bird_image = 0
            bird_image_count = 0
            crow_x = screen_width
            crow_y = random.randint(0,screen_height - 50)
            accelerate_crow = 0
            score = 0
            score_count = 0
            space_flag = False
            space_count = 0

            start = 1



        if start == 1:

            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[K_a]:           #移動はwasd
                bird_x -= bird_speed
            if pressed_keys[K_d]:
                bird_x += bird_speed
            if pressed_keys[K_w]:
                bird_y -= bird_speed
            if pressed_keys[K_s]:
                bird_y += bird_speed

            if pressed_keys[K_SPACE]:       #スペースを押してる間は無敵
                space_flag = True
                space_count += 1
            else:
                space_flag = False
                if space_count > 0:
                    space_count -= 1
            if space_count > 1000:          #無敵を使いすぎると死ぬ
                SURFACE.blit(gameover,gameover_rect)
                start = 2
                
            if pressed_keys[K_LSHIFT]:      #左シフトを押してる間は鳥の移動速度が早くなる
                bird_speed = 10
            else:
                bird_speed = 5

            SURFACE.fill((40,128,215))



            start_pos = (0,screen_height - 25)
            end_pos = (screen_width,screen_height - 25)
            pygame.draw.line(SURFACE,(0,255,0),start_pos,end_pos,50)

            if cloud_x > 0 - cloud_width:
                cloud_x -= 0.8
            else:
                cloud_x = screen_width
        
            SURFACE.blit(cloud,(cloud_x,0))



            building_0.move_building()
            #SURFACE.blit(building_0.picture, building_0.building_x, building_0.building_y)

            building_1.move_building()
            #SURFACE.blit(building_1.picture, building_1.building_x, building_1.building_y)



            if crow_x < 0 -crow_width:
                crow_x = screen_width
                crow_y = random.randint(0,screen_height - 50)
                accelerate_crow += 0.5

            crow_x -= 1 + accelerate_crow
            SURFACE.blit(crow,(crow_x,crow_y))



            #if bird_x > screen_width:                      #画面の左右の端に行ったら逆サイドから出てくる
                #bird_x = 0 - bird_width
            if bird_x > screen_width - bird_width:          #画面の左右の端に行ったらそれ以上進まない
                    bird_x = screen_width - bird_width
            #if bird_x < 0 - bird_width:
                #bird_x = screen_width
            if bird_x < 0:
                bird_x = 0
            if bird_y > screen_height - bird_height - 25:
                bird_y = screen_height - bird_height - 25
            if bird_y < 0:
                bird_y = 0

            SURFACE.blit(bird[bird_image],(bird_x,bird_y))


            if bird_image_count == 20:
                bird_image = (bird_image + 1) % 4
                bird_image_count = 0
            else:
                bird_image_count += 1

            SURFACE.blit(bird[bird_image],(bird_x,bird_y))


            if (crow_x < bird_x + bird_width) and (bird_x < crow_x + crow_width) and (crow_y < bird_y + bird_height) and (bird_y < crow_y + crow_height) and space_flag == False:
                
                start = 2


            score_count += 1
            if score_count == 20:
                score += 1
                score_count = 0

            scoreboard = scoreboard_font.render(str(score),True,(0,0,0))
            SURFACE.blit(scoreboard,(0,0))



            pygame.display.update()

        
        if start == 2:
            SURFACE.blit(gameover,gameover_rect)
            # イベント処理
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN :
                        start = 0
            pygame.display.update()

if __name__ == '__main__':
    main()