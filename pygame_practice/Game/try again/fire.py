import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, set, screen, plane):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, set.bullet_width, set.bullet_height)
        self.rect.centery = plane.rect.centery
        self.rect.right = plane.rect.right

        self.x = float(self.rect.x)

        self.color = set.bullet_color
        self.speed_factor = set.bullet_speed_factor

    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)