import pyautogui as pag
import cv2
import pyautogui as pag
import pywinauto
import pygetwindow as gw
import keyboard as kb
import time
import random


#...............셀레니움..................................


from selenium import webdriver
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import time
import re
driver = webdriver.Chrome(r"C:\Users\jeong\OneDrive - 명지대학교\mech\코딩공부\python_workspace\selenium\chromedriver.exe")
#driver2 = webdriver.Chrome(r"C:\Users\jeong\Dropbox\mech\코딩공부\python_workspace\selenium\chromedriver.exe")

driver.get("https://time.navyism.com/?host=http%3A%2F%2Ftkfile.yes24.com%2Fimages%2Fpopup%2FInfo%2FNotice_info.html%3FipsFilterNumber%3DC008/")
#driver2.get("http://ticket.yes24.com/Perf/40733")

#<div id="time_area">2021년 11월 15일 11시 24분 34초</div>
#......................................................<a class="ui-state-default ui-state-active eveon" href="#">11</a>

check_point_0 = None
check_point_1 = None
check_point_2 = None
check_point_3 = None
check_point_4 = None
num = 0
#-----------전체 티케팅 창 사이즈------------------

scale_start_x = 479
scale_start_y = 291

scale_end_x = 1436
scale_end_y = 908

scale_width = scale_end_x - scale_start_x
scale_height = scale_end_y - scale_start_y

#-----------------------------------------------

#----------좌석 세팅 창 사이즈--------------------


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

def Seat_page(Seat_num):    
    point = pag.center(Seat_num)

    #랜덤으로 뽑은 좌석 클릭
    pag.moveTo(point)
    pag.click()

    #좌석 선택완료 클릭
    pag.moveTo(1314, 887)
    pag.click()
    


def check_point(link):
    #grayscale은 빼면 조금 느려질 수 잇음
    #return pag.locateOnScreen(link,grayscale=True, confidence= 0.8,region =(scale_start_x,scale_start_y,scale_width,scale_height))
    return pag.locateOnScreen(link,grayscale=True, confidence= 0.8)
def Seat_search(link):
    #grayscale은 빼면 조금 느려질 수 잇음
    return pag.locateAllOnScreen(link, confidence= 0.95,region =(seat_start_x,seat_start_y,seat_width,seat_height))


#------------시작-------------------------
print("test Ticketing start")


while True:
    
    a = driver.find_element_by_id('time_area').text
    
    time_arr = a.split()
    
    #print(time_arr[4],type(time_arr[4]))
    if time_arr[4] == "04분":
    
        #print(a)
        time_arr = a.split()
        
        pag.press('F5')
        pag.sleep(2)
        pag.scroll(-1000)
        #예매하기 버튼

       
        while check_point_0 == None:
            print("Cant Find!_0")
            check_point_0 = check_point('Mac_changer\web_page.PNG')

        pag.moveTo(639, 542)
        pag.click()
        pag.moveTo(950, 763)
        pag.click()

        

        print("티케팅 시작")
        break
    else:
        print("티켓팅 시간이 아닙니다.")
        print(time_arr[4])
    
    


while True:
    #if kb.read_key() == 'a':

    print("tracking...")
    
    #첫번째 페이지 왼쪽 "일(red)"인식하기  

    while check_point_1 == None:
        print("Cant Find!_1")
        check_point_1 = check_point('Mac_changer/1st_page.png')
        
    #---------------인식후 동작------------------------

    print("Successfully Find!")
    first_page()

    #---------------다음 페이지 로딩 기다림-------------a


    #두번째 페이지 오른족 하단"좌석 선택완료" 인식하기
    

    while check_point_2 == None:
        print("Cant Find!")
        check_point_2 = check_point('Mac_changer/2nd_page.png')

    #---------------인식후 동작------------------------

    print("Successfully Find!")
    second_page()

    #---------------좌석 서칭--------------------------

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
            
            print("{0}개중 {1}".format(num, random_seat))
            #----좌석 선택(클릭)------------------
            #Seat_page(show[random_seat])
            Seat_page(show[random_seat])

            #---------이선좌 대응------------
            check_point_4 = Seat_search('Mac_changer/already_choiced.png')

            if check_point_4 == None:
                print("done")
            else:
                #찾은 좌석을 한번 더 랜덤으로 고름
                pag.press('ENTER')

                random_seat=random.randint(1,num)
                print(random_seat)
                
                Seat_page(show[random_seat])
        
            #-----------------------------------
        
            
        else:
            print("좌석 없음!")
            print(num)
        
    break   
   
        #----------------이선좌 대응할지 말지 판단-----------------------
        #다음 단계가 뜨느냐 or 이선좌가 뜨느냐 
        #다음 단계가 뜨면 그냥 진행하면 되고 
        #이선좌가 뜨면 
        #--------------------------------------------------------------
        #+ 좌석이 있긴한데 이게 오른쪽 옆에 열려있는건 남은 좌석만 나오나봄
        # 이건 컴퓨터 여러대 켜서 해결 할 수 있을거 같음

        #---------------이선좌가 해결된 이후 다음 단계 누르기------------
