import pygame
from pygame.sprite import Sprite
from random import randint


class Star(Sprite):
    def __init__(self, screen):
        super(Star, self).__init__()
        self.screen = screen
        self.random_number = randint(-10, 10)

        self.image = pygame.image.load("star.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width + self.random_number
        self.rect.y = self.rect.height + self.random_number

    def blitme(self):
        self.screen.blit(self.image, self.rect)# import pygame

