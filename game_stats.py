class GameStats():
    """Track stats for Alien Invasions"""

    def __init__(self, ai_settings):
        """Init the stats"""
        # The high score is set to zero only once, never in game
        self.high_score = 0
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Init stats that can change during game play"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

