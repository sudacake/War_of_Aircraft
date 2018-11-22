import pygame
import sys

from settings  import Settings
from game_stats import GameStats
from pygame.time import Clock
from player import Player
import game_functions as gf
from pygame.sprite import Group
from button import Button
import menu
from start_screen import StartScreen

def main():
    #初始化屏幕
    pygame.display.init()
    #创建Settings实例——game_settings
    game_settings = Settings()
    #初始化 display Surface 参数有游戏屏幕的宽与高，数据存储在Settings类中
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    #设置窗口标题
    pygame.display.set_caption('飞机大战')
    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(game_settings)
    #创建Player实例——player 参数有screnn、game_settings， screen用于确定player的位置
    player = Player(screen, game_settings)
    #创建两个Group类实例——enemys以及bullets（敌机与子弹）
    enemys = Group()
    bullets = Group()
    #创建Play按钮
    #button = Button(game_settings, screen, "Play")
    #创建菜单
    menu_startgame = menu.StartGame(game_settings, screen)
    menu_loadgame = menu.LoadGame(game_settings, screen)
    menu_options = menu.Options(game_settings, screen)
    menu_quit = menu.Quit(game_settings, screen)
    menu_list = [menu_startgame, menu_loadgame, menu_options, menu_quit]
    #创建开始界面
    startscreen = StartScreen(game_settings, screen)


    #创建时间跟踪
    clock = Clock()
    time = 0.0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_RETURN and game_settings.botton_select == 1:
                    while True:
                        # 按键判断
                        gf.check_events(game_settings, screen, player, bullets)
                        # 更新player位置参数
                        player.update()
                        # 更新子弹与敌机的位置参数，以及存活状态
                        gf.update_bullets(bullets, enemys)
                        gf.update_enemys(screen, game_settings, enemys, player)
                        # 绘制屏幕
                        gf.update_screen(game_settings, screen, player, bullets, enemys)

                        pygame.time.delay(10)
               elif event.key == pygame.K_RETURN and game_settings.botton_select == 4:
                   sys.exit()

               elif ( event.key == pygame.K_TAB or event.key == pygame.K_DOWN ) and game_settings.botton_select < 4:
                    game_settings.botton_select += 1
               elif event.key == pygame.K_UP and game_settings.botton_select > 1:
                    game_settings.botton_select -= 1


        screen.fill((game_settings.bg_color))
        #开始界面
        startscreen.blitme()
        for i in range(4):
            menu_list[i].update()
        for i in range(4):
            menu_list[i].draw_button()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

"""
        #按键判断
        gf.check_events(game_settings, screen, player, bullets)
        #更新player位置参数
        player.update()
        #更新子弹与敌机的位置参数，以及存活状态
        gf.update_bullets(bullets, enemys)
        gf.update_enemys(screen, game_settings, enemys, player)
        #绘制屏幕
        gf.update_screen(game_settings, screen, player, bullets, enemys, menu_list)"""

        #循环间隔
        #pygame.time.delay(10)

        #游戏时间统计
        #time += clock.tick() / 1000

main()