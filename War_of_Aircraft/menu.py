import pygame
from button import Button

class StartGame(Button):

    def __init__(self, game_settings, screen, msg = 'Start Game', level = 1):
        super().__init__(game_settings, screen, msg, level)
        #确定按钮这个矩形的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = (self.game_settings.screen_height - self.height * 4) / 2 + self.height * level


class LoadGame(Button):

    def __init__(self, game_settings, screen, msg = 'Load Game', level = 2):
        super().__init__(game_settings, screen, msg, level)
        #确定按钮这个矩形的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = (self.game_settings.screen_height - self.height * 4) / 2 + self.height * level

class Options(Button):

    def __init__(self, game_settings, screen, msg = 'Options', level = 3):
        super().__init__(game_settings, screen, msg, level)
        #确定按钮这个矩形的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = (self.game_settings.screen_height - self.height * 4) / 2 + self.height * level

class Quit(Button):

    def __init__(self, game_settings, screen, msg = 'Quit', level = 4):
        super().__init__(game_settings, screen, msg, level)
        #确定按钮这个矩形的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = (self.game_settings.screen_height - self.height * 4) / 2 + self.height * level