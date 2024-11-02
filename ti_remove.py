import pyautogui as pag
import cv2
import pyautogui as pag
import pywinauto
import pygetwindow as gw
import keyboard as kb
import time
import random


check_point_1 = None
check_point_2 = None
check_point_3 = None

#-----------전체 티케팅 창 사이즈------------------

scale_start_x = 479
scale_start_y = 291

scale_end_x = 1436
scale_end_y = 908

scale_width = scale_end_x - scale_start_x
scale_height = scale_end_y - scale_start_y

#-----------------------------------------------

#----------좌석 서팅 창 사이즈--------------------
num = 0

seat_start_x = 531
seat_start_y = 389

seat_end_x = 1127
seat_end_y = 646

seat_width = seat_end_x - seat_start_x
seat_height = seat_end_y - seat_start_y
#------------------------------------------------


def first_page():

    #관람일 선택
    pag.moveTo(716, 522)
    pag.click()

    #회차가 2개 이상이면 추가적인 클릭필요a
    # pag.moveTo(x,y)
    # pag.click()

    #다음단계 or 좌석 선택
    pag.moveTo(1088, 653)
    pag.click()


def second_page():

    #오른쪽 S석 클릭
    pag.moveTo(1291, 460)
    pag.click()

    #S석 아래 리스트 클릭 - 이건 숫자 인식으로 가장 많은 자리 고르는거 고민
    pag.moveTo(1285, 485)
    pag.click()

def check_point(link):
    #grayscale은 빼면 조금 느려질 수 잇음
    return pag.locateOnScreen(link,grayscale=True, confidence= 0.8,region =(scale_start_x,scale_start_y,scale_width,scale_height))
 
def Seat_search(link):
    #grayscale은 빼면 조금 느려질 수 잇음
    return pag.locateAllOnScreen(link, confidence= 0.99,region =(seat_start_x,seat_start_y,seat_width,seat_height))

#------------시작-------------------------
print("test Ticketing start")


while True:
    if kb.read_key() == 'a':

        while num == 0:
            check_point_3 = Seat_search('Mac_changer/Seat_Color.png')
            show = list(check_point_3)
            num = len(show)

            if num != 0:
                print(check_point_3)
                print("이미지 있음")
                
                #찾은 좌석을 랜덤으로 고름
                random_seat=random.randint(1,num)
                print(random_seat)
                
                print("{0}개중 {1}".format(num, show[random_seat]))
                #----좌석 선택(클릭)------------------
                
                #-----------------------------------
                break
                
            else:
                print("좌석 없음!")
                print(num)