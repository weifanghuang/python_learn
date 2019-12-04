import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class that represents a single alien"""
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the image of the alien and get its circumscribed rectangle.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Place each alien in the top of the left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save the alien correct location
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at designated location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """ If the aliens is at the edge of the screen will return True  """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move the alien to screen right"""
        self.x += (self.ai_settings.alien_speed_factor
                   * self.ai_settings.fleet_direction)
        self.rect.x = self.x



