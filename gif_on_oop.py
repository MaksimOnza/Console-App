import os, platform, time, re

if(platform.system() == 'Windows'):
    import colorama
    colorama.init()


ENTER = ''
LEVEL = 'l'
ESCAPE = 'e'
SETTINGS = 's'
COLOR = 'c'


class MainClass:
    def __init__(self):
        start = ControlClass()
        print('MainClass')
    
class ControlClass:
    firstStart = False
    start_game = False
    setting_screen_loop = False
    level_screen_loop = False
    color_screen_loop = False
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

    def screen_image_ascii(self):
        showScreen = ShowClass()
        showScreen.image_ascii()
        input()

    def show_level_screen(self):
        showScreen = ShowClass()
        showScreen.show_level_screen()

    def show_color_screen(self):
        showScreen = ShowClass()
        showScreen.show_color_screen()

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

    def control_color(self, entrance):
        temp = re.match(r'\d', entrance)
        if entrance == temp.group(0):
            ColorClass.select_color(self, entrance)
        elif entrance =='e':
            self.level_game = 0
            self.color_screen_loop = False
        else:
            self.level_game = 0

    def control_setting(self, entrance):
        if entrance == LEVEL:
            self.level_screen()
        if entrance == COLOR:
            self.color_screen()
        elif entrance == ESCAPE:
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

    def color_screen(self):
        self.color_screen_loop = True
        while self.color_screen_loop:
            self.show_color_screen()
            entrance = input()
            self.control_color(entrance)

    def first_choice(self, entrance):
        if entrance == ENTER:
            print('Enter')
            self.screen_image_ascii()
            #Enter_condition(entrance)
        elif entrance == LEVEL:
            self.setting_screen()
        elif entrance == ESCAPE:
            print('Escape')
            self.start_game = False
        elif entrance == SETTINGS:
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

    def show_color_screen(self):
        self.clear_screen()
        print()
        print('Choice a color\n')
        print('Red ->       press   1')
        print('Green ->     press   2')
        print('Yellow ->    press   3')
        print('Blue ->      press   4')
        print('Magenta ->   press   5')
        print('Cyan  ->     press   6')
        print('White  ->    press   7')
        print('Grey  ->     press   8')
        print('BOLD  ->     press   9')
        print('UP ->        press   E')


    def image_ascii(self):
        
        print('.............................................')
        print('.............................................')
        print('......................*......................')
        print('.............+........#......................')
        print('..............#................=.............')
        print('.............................................')
        print('.......@#............@##@....................')
        print('.................#::::::::::#.......#+.......')
        print('...............#:::::::=#:::::=..............')
        print('..............:::::::*===::::::..............')
        print('....:+#.......#:::::::#@:%#=:::#.......-.....')
        print('..............#::::#%#:%#==::::=.............')
        print('...............#:::#==#:*:::::#..............')
        print('................#::::::::::::%...............')
        print('......*:.........#:::+###:::#........##......')
        print('..................#########+.................')
        print('..................##########.................')
        print('...................#%%%%%%#..................')
        print('...................#%%%%%%#..................')
        print('...................#@@@@@@#..................')
        print('....................#@%%@#...................')
        print('.....................####....................')
        print('.............................................')

class ColorClass:

    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Magenta = '\033[95m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Grey = '\033[90m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    #def __init__():
    dict_color = {
                1:'\033[91m',
                2:'\033[92m',
                3:'\033[93m',
                4:'\033[94m',
                5:'\033[95m',
                6:'\033[96m',
                7:'\033[97m',
                8:'\033[90m',
                9:'\033[1m'
                }

    def select_color(self, color):
        print(ColorClass.dict_color[int(color)])
        print('select_color')


m = MainClass()