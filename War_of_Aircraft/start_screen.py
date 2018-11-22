import pygame

class StartScreen():

    def __init__(self, game_settings, screen):
        self.game_settings = game_settings
        self.screen = screen

        #获取开始界面图像及其外接矩阵
        self.image = pygame.image.load('images/start_screen.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #界面位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)



