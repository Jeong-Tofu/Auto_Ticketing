import pyautogui as pag
import cv2
import pyautogui as pag
import pywinauto
import pygetwindow as gw
import keyboard as kb
import time
import random


check_point_0 = None
check_point_1 = None
check_point_2 = None
check_point_3 = None
check_point_4 = None
clear = 0
num = 0
#-----------전체 티케팅 창 사이즈------------------

scale_start_x = 483
scale_start_y = 323

scale_end_x = 1217
scale_end_y = 902

scale_width = scale_end_x - scale_start_x
scale_height = scale_end_y - scale_start_y

#-----------------------------------------------

#----------좌석 세팅 창 사이즈-------------------- -- 대입


seat_start_x = 479
seat_start_y = 322

seat_end_x = 1206
seat_end_y = 900

seat_width = seat_end_x - seat_start_x
seat_height = seat_end_y - seat_start_y


def Seat_page(Seat_num):    
    point = pag.center(Seat_num)

    #랜덤으로 뽑은 좌석 클릭
    pag.moveTo(point)
    pag.click()

    #좌석 선택완료 클릭 -- 대입
    pag.moveTo(1300, 888)
    pag.click()
    


def check_point(link):
    #grayscale은 빼면 조금 느려질 수 잇음
    #return pag.locateOnScreen(link,grayscale=True, confidence= 0.8,region =(scale_start_x,scale_start_y,scale_width,scale_height))
    return pag.locateOnScreen(link,grayscale=True, confidence= 0.8)
def Seat_search(link):
    #grayscale은 빼면 조금 느려질 수 잇음
    return pag.locateAllOnScreen(link, confidence= 0.80,region =(seat_start_x,seat_start_y,seat_width,seat_height))


while num == 0:
    check_point_3 = Seat_search('Seat_Color.png')
   
    show = list(check_point_3)
    num = len(show)

    if num != 0:
        print(check_point_3)
        print("이미지 있음")
        
        #찾은 좌석을 랜덤으로 고름
        random_seat=random.randint(1,num)
        print(random_seat)
        
        print("{0}개중 {1}".format(num, random_seat))
        #----좌석 선택(클릭)------------------
        #Seat_page(show[random_seat])
        Seat_page(show[random_seat-1])

        #---------이선좌 대응------------


        while True:
            check_point_4 = check_point('already_choiced.png')
            print(check_point_4)

            if check_point_4 == None:
                print("done")
                break
            else:
                #찾은 좌석을 한번 더 랜덤으로 고름
                pag.press('ENTER')
                check_point_4 = None
                random_seat=random.randint(1,num)
                print(random_seat)
                
                Seat_page(show[random_seat-1])
    
        #-----------------------------------
    
        
    else:
        print("좌석 없음!")
        print(num)
        