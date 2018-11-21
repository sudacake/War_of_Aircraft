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