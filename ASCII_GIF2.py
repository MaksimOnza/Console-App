import threading
import platform
import os
import time

ENTER = ''
LEVEL = 'l'
ESCAPE = 'e'
SETTINGS = 's'

start_game = True
nonstop_show_gif = False
hello_message = True
level_game = 1
test = True

list_keys = {
        's': "settings", 
        '': "enter", 
        'l': "level",
        'e': "escape"
        }


def show_hello_message():
    print()
    print('Hey!\nWelcom to a little game!')

def show_start_screen():
    print()
    print('Start ->     press   ENTER')
    print('Level ->     press   L')
    print('Settings ->  press   S')
    print('Exit ->      press   E')

def show_level_screen():
    clear_screen()
    print()
    print('Choice a level\n')
    print('Level I ->   press   1')
    print('Level II ->  press   2')
    print('Level III -> press   3')
    print('UP ->        press   E')

def show_settings_screen():
    print()
    print('Settings message')

def show_error_message():
    print('Press other key')

def show_stopgame_message():
    print('Game stopped')

def show_ASCII_image1():
    print(' ()_()\n (O.o)\n (")(")')
def show_ASCII_image2():
    print(' ()_()\n (O.O)\n (")(")')
def show_ASCII_image3():
    print(' ()_()\n (o.O)\n (")(")')


def clear_screen():
    if(platform.system() == 'Linux'):
        os.system('clear')
    if(platform.system() == 'Windows'):
        os.system('cls')

def draw_gif():
    global level_game
    global nonstop_show_gif
    while nonstop_show_gif:
        clear_screen()
        show_ASCII_image1()
        time.sleep(.3*level_game)
        clear_screen()
        show_ASCII_image2()
        time.sleep(.3*level_game)
        clear_screen()
        show_ASCII_image3()
        time.sleep(.3*level_game)
        time.sleep(1)
        
def show_gif():
    backgrounThread = threading.Thread(target = draw_gif)
    backgrounThread.start()

def control_level(entrance):
    global level_game
    if entrance == '1':
        level_game = 1
    elif entrance == '2':
        level_game = 2
    elif entrance == '3':
        level_game = 3
    elif entrance =='e':
        level_game = 0
        clear_screen()
    else:
        level_game = 0
        clear_screen()


def main_condition(entrance):
    if entrance == ENTER:
        Enter_condition(entrance)
    elif entrance == ESCAPE:
        Escape_condition()
    elif entrance == LEVEL:
        Level_condition(entrance)
    elif entrance == SETTINGS:
        Settings_condition()
    else:
        print('else - main_condition') 

def Enter_condition(entrance):
    clear_screen()
    global nonstop_show_gif
    nonstop_show_gif = True
    show_gif()
    entrance = input()
    if entrance == ESCAPE:
        nonstop_show_gif = False
        print('stop_show_gif')
#доработать Escape_condition
def Escape_condition():
    start_game = False
    print()
    show_stopgame_message()

def Level_condition(entrance):
    show_level_screen()
    entrance = input()
    control_level(entrance)

def Settings_condition():
    clear_screen()
    show_settings_screen()
    entrance = input()


clear_screen()
while start_game:
    clear_screen()
    if hello_message == True:
        show_hello_message()
    show_start_screen()
    entrance = input()
    if entrance == ESCAPE:
        Escape_condition()
        break
    if entrance in list_keys:
        main_condition(entrance)
        hello_message = False
    else:
        show_error_message()
        start_game = False
    hello_message = False
