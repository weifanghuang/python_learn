import sys
import pygame
from rain import Car
from set import Set
import rainfunction as cf
from pygame.sprite import Group
from pygame.sprite import Sprite


def my_game():
    pygame.init()
    ai_set = Set()
    screen = pygame.display.set_mode((ai_set.screen_width, ai_set.screen_height))
    pygame.display.set_caption("kim_first_game")

    cars = Group()
    cf.create_cars(ai_set, screen, cars)

    while True:
        cf.check_event()
        cf.update_cars(ai_set, screen, cars)
        cf.update_screen(ai_set, screen, cars)


my_game()
