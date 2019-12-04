import sys
import pygame
from preferences import Preferences
from plane import Airplane
from spider import Spider
import game_functionx as gf
from pygame.sprite import Group
from game_sta import GameSta


def kim_game():
    pygame.init()
    set = Preferences()
    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    pygame.display.set_caption("kim_Game")

    plane = Airplane(set, screen)

    bullets = Group()

    spiders = Group()

    gf.create_spiders(set, screen, plane, spiders)

    sta = GameSta(set)

    while True:

        gf.check_events(set, screen, plane, bullets)
        if sta.game_active:
            plane.update()
            gf.update_bullets(set, screen, plane, spiders, bullets)
            gf.update_spider(set, sta, screen, plane, spiders, bullets)
        gf.update_screen(set,  screen, plane, spiders, bullets)


kim_game()