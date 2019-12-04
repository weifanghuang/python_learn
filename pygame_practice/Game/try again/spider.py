import pygame
from pygame.sprite import Sprite
from random import randint


class Spider(Sprite):
    def __init__(self, set, screen):
        super(Spider, self).__init__()
        self.screen = screen
        self.set = set
        self.random_number = randint(-10, 10)

        self.image = pygame.image.load("spider.jpg")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width + self.random_number
        self.rect.y = self.rect.height + self.random_number

        self.y = float(self.rect.y)

    def update(self):
        self.rect.x -= self.set.spider_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)


