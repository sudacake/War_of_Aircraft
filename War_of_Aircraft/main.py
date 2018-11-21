import pygame
#import sys

from settings  import Settings
from pygame.time import Clock
from player import Player
import game_functions as gf
from pygame.sprite import Group

def main():
    #初始化屏幕
    pygame.display.init()
    #创建Settings实例——game_settings
    game_settings = Settings()
    #初始化 display Surface 参数有游戏屏幕的宽与高，数据存储在Settings类中
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    #设置窗口标题
    pygame.display.set_caption('飞机大战')
    #创建Player实例——player 参数有screnn、game_settings， screen用于确定player的位置
    player = Player(screen, game_settings)
    #创建两个Group类实例——enemys以及bullets（敌机与子弹）
    enemys = Group()
    bullets = Group()

    #创建时间跟踪
    clock = Clock()
    time = 0.0

    while True:
        #按键判断
        gf.check_events(game_settings, screen, player, bullets)
        #更新player位置参数
        player.update()
        #更新子弹与敌机的位置参数，以及存活状态
        gf.update_bullets(bullets, enemys)
        gf.update_enemys(screen, game_settings, enemys)
        #绘制屏幕
        gf.update_screen(game_settings, screen, player, bullets, enemys)

        #循环间隔
        pygame.time.delay(10)

        #游戏时间统计
        time += clock.tick() / 1000

main()