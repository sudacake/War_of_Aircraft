import pygame

class Player():

    def __init__(self, screen, game_settings):
        """初始化玩家并设置其初始位置"""
        self.screen = screen
        #获取游戏设置
        self.game_settings = game_settings

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #储存小数
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

    def update(self):
        """更新player位置"""
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.player_speed_right
        if self.moving_left == True and self.rect.left > self.screen_rect.left:
            self.center -= self.game_settings.player_speed_left
        if self.moving_up == True and self.rect.top > self.screen_rect.top:
            self.bottom -= self.game_settings.player_speed_up
        if self.moving_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.game_settings.player_speed_down

        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blit_player(self):
        """在指定位置绘制player"""
        self.screen.blit(self.image, self.rect)
