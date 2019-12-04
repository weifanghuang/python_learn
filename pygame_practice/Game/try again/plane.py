import pygame


class Airplane():
    def __init__(self, set, screen):
        """ initialize airplane set"""
        self.screen = screen
        self.set = set

        # create airplane and get a rect
        self.image = pygame.image.load('airplane.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # airplane location
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # saved float
        self.center = float(self.rect.centery)

        # moving sign
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.center -= self.set.plane_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.set.plane_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.set.plane_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.set.plane_speed_factor

        self.rect.centery = self.center

    def blitme(self):
        """draw the airplane in correct"""
        self.screen.blit(self.image, self.rect)

    def center_plane(self):
        self.center = self.screen_rect.centery
