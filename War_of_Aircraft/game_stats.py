
class GameStats():
    """跟踪游戏运行时的数据信息"""

    def __init__(self, game_settings):
        """初始化统计信息"""
        self.settings = game_settings
        self.reset_starts()

    def reset_starts(self):
        """初始化在游戏运行期间可能发生的统计信息"""
        self.player_hp = self.settings.player_hp