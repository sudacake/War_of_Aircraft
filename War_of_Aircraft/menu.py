import pygame
from button import Button

class StartGame():

    def __init__(self, game_settings, screen, msg = 'Start Game'):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings

        #设置按钮的尺寸和其他属性
        self.width, self.height = 230 ,75
        self.button_cololr = (255, 0, 0)
        self.text_color = (255, 255, 255)
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 48)

        #创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = (self.game_settings.screen_height - self.height * 4) / 2 + self.height * 1

        #按钮的标签只需创建一次
        #self.prep_msg(msg)
        self.msg = msg

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_cololr)

        self.msg_imag_rect = self.msg_image.get_rect()
        self.msg_imag_rect.center = self.rect.center

    def update(self):
        if self.game_settings.botton_select == 1:
            self.font = pygame.font.SysFont(None, 60)
            self.text_color = (0, 0, 0)
        else:
            self.font = pygame.font.SysFont(None, 48)
            self.text_color = (255, 255, 255)
        self.prep_msg(self.msg)

    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_cololr, self.rect)
        self.screen.blit(self.msg_image, self.msg_imag_rect)

class LoadGame():

    def __init__(self, game_settings, screen, msg = 'Load Game'):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings

        #设置按钮的尺寸和其他属性
        self.width, self.height = 230 ,75
        self.button_cololr = (255, 0, 0)
        self.text_color = (255, 255, 255)
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 48)

        #创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = (self.game_settings.screen_height - self.height * 4) / 2 + self.height * 2

        #按钮的标签只需创建一次
        #self.prep_msg(msg)
        self.msg = msg

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_cololr)

        self.msg_imag_rect = self.msg_image.get_rect()
        self.msg_imag_rect.center = self.rect.center

    def update(self):
        if self.game_settings.botton_select == 2:
            self.font = pygame.font.SysFont(None, 60)
            self.text_color = (0, 0, 0)
        else:
            self.font = pygame.font.SysFont(None, 48)
            self.text_color = (255, 255, 255)
        self.prep_msg(self.msg)

    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_cololr, self.rect)
        self.screen.blit(self.msg_image, self.msg_imag_rect)

class Options():

    def __init__(self, game_settings, screen, msg = 'Options'):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings

        #设置按钮的尺寸和其他属性
        self.width, self.height = 230 ,75
        self.button_cololr = (255, 0, 0)
        self.text_color = (255, 255, 255)
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 48)

        #创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = (self.game_settings.screen_height - self.height * 4) / 2 + self.height * 3

        #按钮的标签只需创建一次
        #self.prep_msg(msg)
        self.msg = msg

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_cololr)

        self.msg_imag_rect = self.msg_image.get_rect()
        self.msg_imag_rect.center = self.rect.center

    def update(self):
        if self.game_settings.botton_select == 3:
            self.font = pygame.font.SysFont(None, 60)
            self.text_color = (0, 0, 0)
        else:
            self.font = pygame.font.SysFont(None, 48)
            self.text_color = (255, 255, 255)
        self.prep_msg(self.msg)

    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_cololr, self.rect)
        self.screen.blit(self.msg_image, self.msg_imag_rect)

class Quit():

    def __init__(self, game_settings, screen, msg = 'Quit'):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings

        #设置按钮的尺寸和其他属性
        self.width, self.height = 230 ,75
        self.button_cololr = (255, 0, 0)
        self.text_color = (255, 255, 255)
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 48)

        #创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = (self.game_settings.screen_height - self.height * 4) / 2 + self.height * 4

        #按钮的标签只需创建一次
        #self.prep_msg(msg)
        self.msg = msg

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_cololr)

        self.msg_imag_rect = self.msg_image.get_rect()
        self.msg_imag_rect.center = self.rect.center

    def update(self):
        if self.game_settings.botton_select == 4:
            self.font = pygame.font.SysFont(None, 60)
            self.text_color = (0, 0, 0)
        else:
            self.font = pygame.font.SysFont(None, 48)
            self.text_color = (255, 255, 255)
        self.prep_msg(self.msg)

    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_cololr, self.rect)
        self.screen.blit(self.msg_image, self.msg_imag_rect)