import pyautogui as pag
import cv2
import pyautogui as pag
import pywinauto
import pygetwindow as gw
import keyboard as kb

test_pos = pag.position()

temp_pos_x1=0 
temp_pos_y1=0
temp_pos_x2=0
temp_pos_y2=0
temp_pos_x3=0
temp_pos_y3=0
temp_pos_x4=0
temp_pos_y4=0
temp_pos_x5=0
temp_pos_y5=0


print("Start!")


while True:
    if kb.read_key() == 'a':
        print("pressed!")
        temp_pos_x1,temp_pos_y1 = pag.position()
        print("postion -- x1 : {0} | y1 : {1} ".format(temp_pos_x1,temp_pos_y1))
        
    elif kb.read_key() == 's':
        print("pressed!")
        temp_pos_x2,temp_pos_y2 = pag.position()
        print("postion -- x2 : {0} | y2 : {1} ".format(temp_pos_x2,temp_pos_y2))

    elif kb.read_key() == 'd':
        print("pressed!")
        temp_pos_x3,temp_pos_y3 = pag.position()
        print("postion -- x3 : {0} | y3 : {1} ".format(temp_pos_x3,temp_pos_y3))

    elif kb.read_key() == 'f':
        print("pressed!")
        temp_pos_x4,temp_pos_y4 = pag.position()
        print("postion -- x4 : {0} | y4 : {1} ".format(temp_pos_x4,temp_pos_y4))

    elif kb.read_key() == 'g':
        print("pressed!")
        temp_pos_x5,temp_pos_y5 = pag.position()
        print("postion -- x5 : {0} | y5 : {1} ".format(temp_pos_x5,temp_pos_y5))

    if kb.read_key() == "p":
        print('done')
        print("1_pos ( {0}, {1} )\n".format(temp_pos_x1,temp_pos_y1))
        print("2_pos ( {0}, {1} )\n".format(temp_pos_x2,temp_pos_y2))
        print("3_pos ( {0}, {1} )\n".format(temp_pos_x3,temp_pos_y3))
        print("4_pos ( {0}, {1} )\n".format(temp_pos_x4,temp_pos_y4))
        print("5_pos ( {0}, {1} )\n".format(temp_pos_x5,temp_pos_y5))
        break

