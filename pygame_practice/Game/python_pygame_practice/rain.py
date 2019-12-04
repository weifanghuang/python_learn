import pygame
from pygame.sprite import Sprite


class Car(Sprite):

    def __init__(self, ai_set, screen):
        super(Car, self). __init__()
        self.screen = screen
        self.ai_set = ai_set
        self.image = pygame.image.load('raindrop.png')
        self.rect = self.image.get_rect()
        self.drop_speed = 5

    def blitme(self):
        """Draw a ship at designated location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.drop_speed

    def check_edges(self):
        screen_rect = screen.get_rect()
        if self.rect.y >= screen_rect.bottom + self.rect.width:
            return True

