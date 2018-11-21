import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, game_settings, screen, player):
        super().__init__()
        #获取屏幕
        self.screen = screen

        #在（0，0）处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top

        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.speed = game_settings.bullet_speed

    def update(self):

        #更新表示子弹位置的小数值
        self.y -= self.speed

        self.rect.y = self.y

    def draw_bullet(self):

        #绘制子弹 矩形rect
        pygame.draw.rect(self.screen, self.color, self.rect)