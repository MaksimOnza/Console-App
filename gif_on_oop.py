import os, platform

class Constants:
    ENTER = ''
    LEVEL = 'l'
    ESCAPE = 'e'
    SETTINGS = 's'

class MainClass:
    def __init__(self):
        start = ControlClass()
        print('MainClass')
    

class ControlClass:
    firstStart = False
    start_game = False
    setting_screen_loop = False
    level_screen_loop = False
    level_screen = False
    level_game = 0
    
    def __init__(self):
        self.start_game = True
        self.start_function()

    def start_function(self):
        while self.start_game:
            if self.firstStart==False:
                self.hello()
                self.firstStart = True
            self.show_start_screen()
            entrance = input()
            self.start_game = self.first_choice(entrance)

    def show_start_screen(self):
        self.showScreen = ShowClass()
        self.showScreen.show_start_screen()

    def show_level_screen(self):
        showScreen = ShowClass()
        showScreen.show_level_screen()

    def show_setting_screen(self):
        showScreen = ShowClass()
        showScreen.show_setting_screen()

    def control_level(self, entrance):
        if entrance == '1':
            self.level_game = 1
        elif entrance == '2':
            self.level_game = 2
        elif entrance == '3':
            self.level_game = 3
        elif entrance =='e':
            self.level_game = 0
            self.level_screen_loop = False
        else:
            self.level_game = 0

    def control_setting(self, entrance):
        if entrance == Constants.LEVEL:
            self.level_screen()
        elif entrance == Constants.ESCAPE:
            self.setting_screen_loop = False

    def setting_screen(self):
        self.setting_screen_loop = True
        while self.setting_screen_loop:
            self.show_setting_screen()
            entrance = input()
            self.control_setting(entrance)

    def level_screen(self):
        self.level_screen_loop = True
        while self.level_screen_loop:
            self.show_level_screen()
            entrance = input()
            self.control_level(entrance)

    def first_choice(self, entrance):
        if entrance == Constants.ENTER:
            print('Enter')
            #Enter_condition(entrance)
        elif entrance == Constants.LEVEL:
            print('Level')
            self.setting_screen()
            #Level_condition(entrance)
        elif entrance == Constants.ESCAPE:
            print('Escape')
            self.start_game = False
            #Escape_condition()
        elif entrance == Constants.SETTINGS:
            print('Setting')
            self.setting_screen()
            #Settings_condition()
        else:
            print('else - main_condition')
        return self.start_game

    def hello(self):
        d = ShowClass()
        print(d.hello())
        del d


class ShowClass:

    def clear_screen(self):
        if(platform.system() == 'Linux'):
            os.system('clear')
        if(platform.system() == 'Windows'):
            os.system('cls')

    def show_start_screen(self):
        self.clear_screen()
        print()
        print('Start ->     press   ENTER')
        print('Settings ->  press   S')
        print('Exit ->      press   E')

    def hello(self):
       print('HELLo!')

    def show_setting_screen(self):
        self.clear_screen()
        print()
        print('Level ->     press   L')
        print('Speed ->     press   S')
        print('Color ->     press   C')
        print('UP ->        press   E')

    def show_level_screen(self):
        self.clear_screen()
        print()
        print('Choice a level\n')
        print('Level I ->   press   1')
        print('Level II ->  press   2')
        print('Level III -> press   3')
        print('UP ->        press   E')


m = MainClass()