import pygame
import sys
from star import Star
from pygame.sprite import Group
from random import randint


def game_star():
    pygame.init()
    screen = pygame.display.set_mode((1400, 750))
    pygame.display.set_caption("Star Range")

    bg_color = (0, 0, 51)

    stars = Group()
    draw_stars(stars, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        stars.draw(screen)
        pygame.display.flip()


def draw_stars(stars, screen):
    star = Star(screen)
    star_width = star.rect.width
    star_height = star.rect.height
    available_x = 1400 - (2 * star_width)
    x_star_num = int(available_x / (2 * star_width))
    available_y = 750 - (2 * star_height) + randint(-10, 10)
    y_star_num = int(available_y / star_height)
    for star_num in range(x_star_num):
        for num_star in range(y_star_num):
            star = Star(screen)
            star.rect.x = star.rect.x + 2 * star.rect.x * star_num
            star.rect.y = star.rect.y + 2 * star.rect.y * num_star
            stars.add(star)


game_star()

# import pygame
# import sys
# from pygame.sprite import Group
# from pygame.sprite import Sprite
# from random import randint
#
#
# class Settings():
#     def __init__(self):
#         self.screen_width = 1000
#         self.screen_height = 600
#         self.bg_color = (0, 0, 51)

# def get_number_star_x(settings, star_width):
#     available_space_x = settings.screen_width - 2 * star_width
#     number_stars_x = int(available_space_x / (star_width * 2))
#     return number_stars_x
#
#
# def get_number_rows(settings, star_height):
#     """计算屏幕可容纳多少行外星人"""
#     available_space_y = (settings.screen_height - 2 * star_height)
#     number_rows = int(available_space_y / (star_height * 2))
#     return number_rows
#
#
# def create_star(settings, screen, stars, star_number, row_number):
#     star = Star(settings, screen)
#     star.rect.x = star.rect.x + 2 * star.rect.x * star_number
#     star.rect.y = star.rect.y + 2 * star.rect.y * row_number
#     stars.add(star)
#
#
# def create_star_group(settgings, screen, stars):
#     star = Star(settgings, screen)
#     number_stars_x = get_number_star_x(settgings, star.rect.width)
#     number_rows = get_number_rows(settgings, star.rect.height)
#
#     for row_number in range(number_rows):
#         for star_number in range(number_stars_x):
#             create_star(settgings, screen, stars, star_number, row_number)
#
#
# def run_star():
#     pygame.init()
#     settings = Settings()
#     screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
#     pygame.display.set_caption('Stars')
#     stars = Group()
#     create_star_group(settings, screen, stars)
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         screen.fill(settings.bg_color)
#         stars.draw(screen)
#         pygame.display.flip()
#
#
# run_star()