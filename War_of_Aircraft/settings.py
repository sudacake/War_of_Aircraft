import pygame

class Settings():

    def __init__(self):

        #屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #玩家设置
        self.player_speed_right = 4
        self.player_speed_left = 4
        self.player_speed_up = 4
        self.player_speed_down = 4

        self.player_hp = 10
        self.player_invincible = False

        #子弹设置
        self.bullet_speed = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60

        #敌机设置
        self.enemy_num = 3
        self.enemy_speed = 1.5

        #菜单中的按钮设置
        self.botton_width = 200
        self.botton_height = 75
        self.botton_color = (255, 0, 0)
        self.botton_text_color = (255, 255, 255)
        pygame.font.init()
        self.botton_font = pygame.font.SysFont(None, 48)

        self.botton_select = 1