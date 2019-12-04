import pygame
import sys
from random import randint
from pygame.sprite import Sprite
from pygame.sprite import Group
from time import sleep


class Set():
    def __init__(self):
        self.screen_width = 1400
        self.screen_height = 750
        self.bg_color = 255, 240, 245


class Santa():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('santa_claus.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.santa_speed = 15

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.santa_speed
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.santa_speed

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def santa_centet(self):
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


class Present(Sprite):
    def __init__(self, screen, set):
        super(Present, self).__init__()
        self.screen = screen
        self.set = set
        self.image = pygame.image.load('christmas_box.png')
        self.rect = self.image.get_rect()
        self.random_number = randint(0, set.screen_width)
        self.drop_speed = 5

        self.rect.centerx = self.random_number
        self.rect.top = 0
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.drop_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Star(Sprite):
    def __init__(self, screen, set):
        super(Star, self).__init__()
        self.screen = screen
        self.random_number = randint(0, set.screen_width)
        self.drop_speed = 10

        self.image = pygame.image.load("star.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.random_number
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.drop_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class GameStats():
    def __init__(self, set):
        self.set = set
        self.bottom_limit = 3
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.game_life = self.bottom_limit


def check_events(santa):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, santa)
        elif event.type == pygame.KEYUP:
            check_keyup(event, santa)


def check_keydown(event, santa):
    if event.key == pygame.K_RIGHT:
        santa.moving_right = True
    elif event.key == pygame.K_LEFT:
        santa.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup(event, santa):
    if event.key == pygame.K_RIGHT:
        santa.moving_right = False
    elif event.key == pygame.K_LEFT:
        santa.moving_left = False


def create_present(screen, set, presents):
    random_num = randint(0, 3)
    for present_num in range(random_num):
        present = Present(screen, set)
        presents.add(present)


def create_stars(screen, set, stars):
    random_num = randint(0, 6)
    for stars_num in range(random_num):
        star = Star(screen, set)
        stars.add(star)


def update_present_star(screen, stats, santa, presents, stars, set):
    presents.update()
    stars.update()
    for present in presents.copy():
        if present.rect.bottom >= set.screen_height:
            game_over(screen, set, stats, santa, presents, stars)
    for star in stars.copy():
        if star.rect.bottom >= set.screen_height:
            game_over(screen, set, stats, santa, presents, stars)


def game_over(screen, set, stats, santa, presents, stars):
    if stats.bottom_limit > 0:
        stats.bottom_limit -= 1

        presents.empty()
        stars.empty()
        create_present(screen, set, presents)
        create_stars(screen, set, stars)
        santa.santa_centet()

        sleep(0.5)

    else:
        stats.game_active = False


def check_present(screen, presents, santa, set):
    for present in presents.copy():
        if present.rect.top >= set.screen_height or \
                pygame.sprite.spritecollide(santa, presents, True, collided=None):
            presents.remove(present)
            if len(presents) == 0:
                create_present(screen, set, presents)


def check_star(screen, stars, santa, set):
    for star in stars.copy():
        if star.rect.top >= set.screen_height or \
                pygame.sprite.spritecollide(santa, stars, True, collided=None):
            stars.remove(star)
            if len(stars) == 0:
                create_stars(screen, set, stars)


def update_screen(set, screen, santa, presents, stars):
    screen.fill(set.bg_color)
    santa.blitme()
    presents.draw(screen)
    stars.draw(screen)
    pygame.display.flip()


def ball_come():
    pygame.init()
    set = Set()
    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    pygame.display.set_caption("Merry Christmas")
    santa = Santa(screen)
    presents = Group()
    stars = Group()

    stats = GameStats(set)

    create_present(screen, set, presents)
    create_stars(screen, set, stars)

    while True:
        check_events(santa)
        if stats.game_active:
            santa.update()
            update_present_star(screen, stats, santa, presents, stars, set)
            check_present(screen, presents, santa, set)
            check_star(screen, stars, santa, set)

        update_screen(set, screen, santa, presents, stars)


ball_come()
