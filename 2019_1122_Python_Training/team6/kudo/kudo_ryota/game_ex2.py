import sys
import pygame
import random 
from pygame.locals import QUIT,Rect,MOUSEBUTTONDOWN,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN
from time import sleep

pygame.init()
SURFACE = pygame.display.set_mode((800,800))
pygame.display.set_caption("ブラックジャック")
FPSCLOCK = pygame.time.Clock()

card1 = pygame.image.load("trump2/torannpu-illust_s1.png")
card2 = pygame.image.load("trump2/torannpu-illust_s2.png")
card3 = pygame.image.load("trump2/torannpu-illust_s3.png")
card4 = pygame.image.load("trump2/torannpu-illust_s4.png")
card5 = pygame.image.load("trump2/torannpu-illust_s5.png")
card6 = pygame.image.load("trump2/torannpu-illust_s6.png")
card7 = pygame.image.load("trump2/torannpu-illust_s7.png")
card8 = pygame.image.load("trump2/torannpu-illust_s8.png")
card9 = pygame.image.load("trump2/torannpu-illust_s9.png")
card10 = pygame.image.load("trump2/torannpu-illust_s10.png")
card11 = pygame.image.load("trump2/torannpu-illust_s11.png")
card12 = pygame.image.load("trump2/torannpu-illust_s12.png")
card13 = pygame.image.load("trump2/torannpu-illust_s13.png")
card14 = pygame.image.load("trump2/torannpu-illust_k1.png")
card15 = pygame.image.load("trump2/torannpu-illust_k2.png")
card16 = pygame.image.load("trump2/torannpu-illust_k3.png")
card17 = pygame.image.load("trump2/torannpu-illust_k4.png")
card18 = pygame.image.load("trump2/torannpu-illust_k5.png")
card19 = pygame.image.load("trump2/torannpu-illust_k6.png")
card20 = pygame.image.load("trump2/torannpu-illust_k7.png")
card21 = pygame.image.load("trump2/torannpu-illust_k8.png")
card22 = pygame.image.load("trump2/torannpu-illust_k9.png")
card23 = pygame.image.load("trump2/torannpu-illust_k10.png")
card24 = pygame.image.load("trump2/torannpu-illust_k11.png")
card25 = pygame.image.load("trump2/torannpu-illust_k12.png")
card26 = pygame.image.load("trump2/torannpu-illust_k13.png")
card27 = pygame.image.load("trump2/torannpu-illust_d1.png")
card28 = pygame.image.load("trump2/torannpu-illust_d2.png")
card29 = pygame.image.load("trump2/torannpu-illust_d3.png")
card30 = pygame.image.load("trump2/torannpu-illust_d4.png")
card31 = pygame.image.load("trump2/torannpu-illust_d5.png")
card32 = pygame.image.load("trump2/torannpu-illust_d6.png")
card33 = pygame.image.load("trump2/torannpu-illust_d7.png")
card34 = pygame.image.load("trump2/torannpu-illust_d8.png")
card35 = pygame.image.load("trump2/torannpu-illust_d9.png")
card36 = pygame.image.load("trump2/torannpu-illust_d10.png")
card37 = pygame.image.load("trump2/torannpu-illust_d11.png")
card38 = pygame.image.load("trump2/torannpu-illust_d12.png")
card39 = pygame.image.load("trump2/torannpu-illust_d13.png")
card40 = pygame.image.load("trump2/torannpu-illust_h1.png")
card41 = pygame.image.load("trump2/torannpu-illust_h2.png")
card42 = pygame.image.load("trump2/torannpu-illust_h3.png")
card43 = pygame.image.load("trump2/torannpu-illust_h4.png")
card44 = pygame.image.load("trump2/torannpu-illust_h5.png")
card45 = pygame.image.load("trump2/torannpu-illust_h6.png")
card46 = pygame.image.load("trump2/torannpu-illust_h7.png")
card47 = pygame.image.load("trump2/torannpu-illust_h8.png")
card48 = pygame.image.load("trump2/torannpu-illust_h9.png")
card49 = pygame.image.load("trump2/torannpu-illust_h10.png")
card50 = pygame.image.load("trump2/torannpu-illust_h11.png")
card51 = pygame.image.load("trump2/torannpu-illust_h12.png")
card52 = pygame.image.load("trump2/torannpu-illust_h13.png")
cardall = [
    card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15,card16,card17,card18,card19,card20,card21,card22,card23,card24,card25,card26,card27,card28,card29,card30,card31,card32,card33,card34,card35,card36,card37,card38,card39,card40,card41,card42,card43,card44,card45,card46,card47,card48,card49,card50,card51,card52

]

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

            S = [1,2,3,4,5,6,7,8,9,10,11,12,13]
            K = [1,2,3,4,5,6,7,8,9,10,11,12,13]
            D = [1,2,3,4,5,6,7,8,9,10,11,12,13]
            H = [1,2,3,4,5,6,7,8,9,10,11,12,13]

            #中の数字14～26がKのA~13と考える 27~39がD 40~52がH
            card = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
            #print(card)

            #確かめ用
            '''
            print(card[14])
            card2 = card[14] % 13
            print(card2)
            '''
            #カードをシャッフル
            random.shuffle(card)
            print(card)
            
            #変数宣言
            tefuda_sum = 0
            d_next = 1


            #手札
            tefuda = []
            dtefuda = []
            
            print("自分が２枚、ディーラーが１枚ヒットします。")
            start = 1

        if start == 1:
            #手札を引く　最初に２枚引く
            for i in range(0,2):
                tefuda.append(card[0])
                del card[0]
                #print(card)
                #13%13が0になってしまうため、13を残す処理
                for i in range (0,len(tefuda)):
                    if tefuda[i] == 13 or tefuda[i] == 26 or tefuda[i] == 13 or tefuda[i] == 39 or tefuda[i] == 52:
                        tefuda[i] = 13
                    else:
                        tefuda[i] = tefuda[i]%13
                print("自分の今持っているカード",tefuda)
                #J Q K の時は値は合計の時10にする
                tefuda2 = tefuda.copy()
                for i in range(0,len(tefuda2)):
                    if tefuda2[i] == 11 or tefuda2[i] == 12 or tefuda2[i] == 13:
                        tefuda2[i] = 10
                tefuda_sum = sum(tefuda2)
                print("自分の現在の数値の合計",tefuda_sum)
            #for i in range (0,len(tefuda)):
            #    tefuda_sum = tefuda_sum + tefuda[i]
            #print(tefuda_sum)
            for i in range(0,len(tefuda2)):
                SURFACE.blit(cardall[tefuda[i]-1],(150*i,450))
            START = 2
            pygame.display.update()

        if START == 2:
            #ディーラーが1枚引く
            for i in range(0,1):
                dtefuda.append(card[0])
                del card[0]
                #print(card)
                #13%13が0になってしまうため、13を残す処理
                for i in range (0,len(dtefuda)):
                    if dtefuda[i] == 13 or dtefuda[i] == 26 or dtefuda[i] == 13 or dtefuda[i] == 39 or dtefuda[i] == 52:
                        dtefuda[i] = 13
                    else:
                        dtefuda[i] = dtefuda[i]%13
                print("ディーラーが今持っているカード",dtefuda)
                #J Q K の時は値は合計の時10にする
                dtefuda2 = dtefuda.copy()
                for i in range(0,len(dtefuda2)):
                    if dtefuda2[i] == 11 or dtefuda2[i] == 12 or dtefuda2[i] == 13:
                        dtefuda2[i] = 10
                dtefuda_sum = sum(dtefuda2)
                print("ディーラーの現在の数値の合計",dtefuda_sum)
            for i in range(0,len(dtefuda2)):
                SURFACE.blit(cardall[dtefuda[i]-1],(150*i,150))
            START = 3
            pygame.display.update()

        if START == 3:
            START == 4
            #手札を引く Enterを押したら　１枚引くようにしたいが 現状１を押して引く
            while True:
                num1 = int(input("さらにカードを引く場合は1,引かない場合は2を入力してください"))    
                if num1 == 1:
                    print("さらにカードを引きます")
                    tefuda.append(card[0])
                    del card[0]
                else:
                    print("これ以上引きません")
                    START = 4
                    break  
                #手札を13で%してカードの強さに戻す
                for i in range (0,len(tefuda)):
                    if tefuda[i] == 13 or tefuda[i] == 26 or tefuda[i] == 13 or tefuda[i] == 39 or tefuda[i] == 52:
                        tefuda[i] = 13
                    else:
                        tefuda[i] = tefuda[i]%13
                print("自分の今持っているカード",tefuda)
                #J Q K の時は値は合計の時10にする
                tefuda2 = tefuda.copy()
                for i in range(0,len(tefuda2)):
                    if tefuda2[i] == 11 or tefuda2[i] == 12 or tefuda2[i] == 13:
                        tefuda2[i] = 10
                tefuda_sum = sum(tefuda2)
                print("自分の現在の数値",tefuda_sum)
                
                for i in range(0,len(tefuda2)):
                    SURFACE.blit(cardall[tefuda[i]-1],(150*i,450))
                pygame.display.update()

                if tefuda_sum >= 22:
                    print("自分の手札が21を超えたため負けです")
                    d_next = 0
                    START = 12
                    break
            if tefuda_sum >= 22:
                d_next = 0
                START = 12
                sleep(1)
                break




            
        if START == 4:
            #自分が21以下の時のみディーラーがヒットする
            if d_next == 0:
                print("ディーラー勝利のためこれ以上ヒットしません")  
            else: 
                #ディラーが１６以上になるまで引く
                if dtefuda_sum >= 16:
                    print("ディーラーが16以上のためこれ以上引きません")
                    if dtefuda_sum > tefuda_sum:
                        print("あなたの負けです。")
                    elif tefuda_sum > dtefuda_sum:
                        print("あなたの勝ちです。")
                    else:
                        print("引き分けです。")
                else:
                    while dtefuda_sum <= 15:
                        print("ディーラーが１５以下のため、さらにカードを引きます")
                        dtefuda.append(card[0])
                        del card[0]
                        #print(card)
                        #13%13が0になってしまうため、13を残す処理
                        for i in range (0,len(dtefuda)):
                            if dtefuda[i] == 13 or dtefuda[i] == 26 or dtefuda[i] == 13 or dtefuda[i] == 39 or dtefuda[i] == 52:
                                dtefuda[i] = 13
                            else:
                                dtefuda[i] = dtefuda[i]%13
                        print("ディーラーが今持っているカード",dtefuda)
                        #J Q K の時は値は合計の時10にする
                        dtefuda2 = dtefuda.copy()
                        for i in range(0,len(dtefuda2)):
                            if dtefuda2[i] == 11 or dtefuda2[i] == 12 or dtefuda2[i] == 13:
                                dtefuda2[i] = 10
                        dtefuda_sum = sum(dtefuda2)
                        print("ディーラーの現在の数値の合計",dtefuda_sum)
                    if dtefuda_sum >= 22:
                        print("ディーラーが21を超えたためあなたの勝利です")
                    if tefuda_sum < dtefuda_sum:
                        print("ディーラーの勝ちです。")
                    elif tefuda_sum > dtefuda_sum:
                        print("あなたの勝ちです")
                    else:
                        print("引き分けです")
            sleep(1)
            break            
            if START == 12:
                print("あなたの負けです")
                break
            


        #pygame.display.update()
        #FPSCLOCK.tick(3)
        if start == 11:
            start = 0
        #    pygame.display.update()
        #    FPSCLOCK.tick(3)
        sleep(3)
if __name__ == '__main__':
    main()