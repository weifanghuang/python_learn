class Settings():

    """Store all setting classes"""
    def __init__(self):
        """Initialize the game setting"""
        # screen setting
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # ship speed setting
        self.ship_speed_factor = 10
        self.ship_limit = 3
        # bullet setting
        self.bullet_speed_factor = 10
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 10
        # aliens setting
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 5
        self.speedup_scale = 1.5
        self.score_scale = 1.5

        self.initalize_dynamic_setting()
        # fleet_direction of 1 means moving to the screen right;
        self.fleet_direction = 1

    def initalize_dynamic_setting(self):
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 5

        # fleet_direction of 1 means moving to the screen right;
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
