class GameSta():
    def __init__(self, set):
        self.set = set
        self.reset_sta()
        self.game_active = True

    def reset_sta(self):
        self.plane_left = self.set.plane_limit
