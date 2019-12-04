import sys
import pygame
from fire import Bullet
from spider import Spider
from random import randint
from time import sleep


def check_events(set, screen, plane, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_event_down(event, set, screen, plane, bullets)
        elif event.type == pygame.KEYUP:
            check_event_up(event, plane)


def check_event_down(event, set, screen, plane, bullets):
    if event.key == pygame.K_UP:
        plane.moving_up = True
    elif event.key == pygame.K_DOWN:
        plane.moving_down = True
    elif event.key == pygame.K_RIGHT:
        plane.moving_right = True
    elif event.key == pygame.K_LEFT:
        plane.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(set, screen, plane, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(set, screen, plane, bullets):
    if len(bullets) < set.bullets_allowed:
        new_bullet = Bullet(set, screen, plane)
        bullets.add(new_bullet)


def check_event_up(event, plane):
    if event.key == pygame.K_UP:
        plane.moving_up = False
    elif event.key == pygame.K_DOWN:
        plane.moving_down = False
    elif event.key == pygame.K_RIGHT:
        plane.moving_right = False
    elif event.key == pygame.K_LEFT:
        plane.moving_left = False


def get_number_y(set, spider_height):
    able_space_y = set.screen_height - spider_height
    num_spider_y = int(able_space_y / spider_height)
    return num_spider_y


def create_spiders(set, screen, plane, spiders):
    spider = Spider(set, screen)
    num_spider_y = get_number_y(set, spider.rect.height)
    num_lines = get_number_lines(set, plane.rect.width, spider.rect.width)

    for num_line in range(num_lines):
        for num_spider in range(num_spider_y):
            create_spider(set, screen, spiders, num_spider, num_line)


def create_spider(set, screen, spiders, num_spider, num_line):
    spider = Spider(set, screen)
    spider_height = spider.rect.height
    spider.y = randint(-10, 10) + 2 * spider_height * num_spider
    spider.rect.y = spider.y
    spider.rect.x = 25 * spider.rect.width + randint(-10, 10) * spider.rect.width * num_line

    spiders.add(spider)


def get_number_lines(set, plane_width, spider_width):
    able_space_x = (set.screen_width - (3*spider_width) - plane_width)
    num_lines = int(able_space_x/(2 * spider_width))
    return num_lines


def update_bullets(set, screen, plane, spiders, bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.right >= set.screen_width:
            bullets.remove(bullet)

    check_bullets_spiders_collision(set, screen, plane, spiders, bullets)


def check_bullets_spiders_collision(set, screen, plane, spiders, bullets):
    collisions = pygame.sprite.groupcollide(bullets, spiders, True, True)
    if len(spiders) == 0:
        bullets.empty()
        create_spiders(set, screen, plane, spiders)


def update_screen(set, screen, plane, spiders, bullets):
    screen.fill(set.background_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    plane.blitme()
    spiders.draw(screen)
    pygame.display.flip()


def update_spider(set, sta, screen, plane, spiders, bullets):
    spiders.update()
    spider_len_check(set, screen, plane, spiders)
    if pygame.sprite.spritecollideany(plane, spiders):
        plane_hit(set, sta, screen, plane, spiders, bullets)


def plane_hit(set, sta, screen, plane, spiders, bullets):
    if sta.plane_left > 0:
        sta.plane_left -= 1
        spiders.empty()
        bullets.empty()
        create_spiders(set, screen, plane, spiders)
        plane.center_plane()

        sleep(1)
        print(sta.plane_left)
    else:
        sta.game_active = False


def spider_len_check(set, screen, plane, spiders):
    for spider in spiders.copy():
        if spider.rect.right <= 0:
            spiders.remove(spider)
            if len(spiders) == 0:
                create_spiders(set, screen, plane, spiders)
