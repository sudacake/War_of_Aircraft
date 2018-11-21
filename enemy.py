import pygame
from pygame.sprite import Sprite
import random

class Enemy(Sprite):

    def __init__(self, screen, game_settings):
        super().__init__()
        #获取基本参数
        self.screen =screen
        self.game_settings = game_settings

        #获取敌机图像及其外接矩阵
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #初始化敌机位置
        self.rect.left = random.randint(0,self.game_settings.screen_width - self.rect.width)
        self.rect.top = self.screen_rect.top

        self.y = float(self.rect.y)

    def blit_enemy(self):

        #绘制enemy
        self.screen.blit(self.image, self.rect)

    def update(self):

        self.y += self.game_settings.enemy_speed
        self.rect.y = self.y