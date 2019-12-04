import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class that manges bullets fired by ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet at the location of the ship"""
        super(Bullet, self).__init__()
        self.screen = screen
        """Create a bullet rect At(0,0),setting correct location"""
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """moving bullet to the screen top"""
        # Update the minimum value indicating the position of the bullet
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet in the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
