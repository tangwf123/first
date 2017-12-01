# Author：TangWeiFeng
import sys
import pygame
from settings import Settings
from ship import Ship
import ganme_functions

def run_game():
    #初始化游戏，并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Aline invasion')

    ship = Ship(ai_settings,screen)
    #设置背景颜色
    #bg_color = (230,230,230)

    #主循环
    while True:
        #监听键盘鼠标事件
        ganme_functions.check_events(ship,screen)

        ganme_functions.update_screen(ai_settings,screen,ship)

        ship.updata()



run_game()