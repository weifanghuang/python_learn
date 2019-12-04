import pygame
import sys
from pygame.sprite import Group
from pygame.sprite import Sprite
from time import sleep
import pygame.font


class Set():
    def __init__(self):
        self.screen_width = 1400
        self.screen_height = 750
        self.bg_color = 143, 188, 143
        self.bottom_limit = 3

        self.speedup_scale = 1.5
        self.initialize_dynamic_set()

    def initialize_dynamic_set(self):
        self.hunter_speed = 5
        self.star_speed = 30
        self.target_speed = 5
        self.target_direction = 1

    def increase_speed(self):
        self.hunter_speed *= self.speedup_scale
        self.star_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale
        self.target_direction *= self.speedup_scale


class Hunter():
    def __init__(self, set, screen):
        self.screen = screen
        self.set = set

        self.image = pygame.image.load('hunter.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

        self.center = float(self.rect.centery)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.center -= self.set.hunter_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.set.hunter_speed

        self.rect.centery = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def hunter_centet(self):
        self.center = self.screen_rect.centery
        self.rect.right = self.screen_rect.right


class Star(Sprite):
    def __init__(self, set, screen, hunter):
        super(Star, self).__init__()
        self.screen = screen

        self.image = pygame.image.load("star.png")
        self.rect = self.image.get_rect()

        self.rect.centery = hunter.rect.centery - 8
        self.rect.left = hunter.rect.left
        self.x = float(self.rect.x)
        self.star_speed_x = set.star_speed

    def update(self):
        self.x -= self.star_speed_x
        self.rect.x = self.x

    def draw_star(self):
        self.screen.blit(self.image, self.rect)


class Target(Sprite):
    def __init__(self, set, screen):
        super(Target, self).__init__()
        self.screen = screen
        self.set = set
        self.image = pygame.image.load('target.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        self.y = float(self.rect.y)

    def update(self):
        self.y += (self.set.target_direction * self.set.target_speed)
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_egde(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top <= screen_rect.top:
            return True
        elif self.rect.bottom >= screen_rect.bottom:
            return True


class GameStats():
    def __init__(self, set):
        self.set = set
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.game_life = self.set.bottom_limit


class Button():
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (70, 130, 180)

        self.text_color = (255, 250, 250)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


def check_events(set, screen, hunter, stars, targets, stats, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(set, screen, hunter, stars, targets, stats, play_button, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, set, screen, hunter, stars)
        elif event.type == pygame.KEYUP:
            check_keyup(event, hunter)


def check_play_button(set, screen, hunter, stars, targets, stats, play_button, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        set.initialize_dynamic_set()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        targets.empty()
        stars.empty()

        create_target(set, screen, targets)
        hunter.hunter_centet()


def check_keydown(event, set, screen, hunter, stars):
    if event.key == pygame.K_UP:
        hunter.moving_up = True
    elif event.key == pygame.K_DOWN:
        hunter.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_star(screen, set, hunter, stars)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_star(screen, set, hunter, stars):
    if len(stars) < 10:
        new_star = Star(set, screen, hunter)
        stars.add(new_star)


def check_keyup(event, hunter):
    if event.key == pygame.K_UP:
        hunter.moving_up = False
    elif event.key == pygame.K_DOWN:
        hunter.moving_down = False


def create_target(set, screen, targets):
    targets_num = 1
    for target_num in range(targets_num):
        target = Target(set, screen)
        target.x = 0
        target.rect.x = target.x
        targets.add(target)


def check_targets_edges(targets):
    for target in targets:
        if target.check_egde():
            target.set.target_direction *= -1


def update_stars(set, screen, stars, stats, targets, hunter):
    stars.update()
    check_collisions(set, screen, stars, stats, targets, hunter)
    for star in stars.copy():
        if star.rect.right < 0:
            stars.remove(star)


def check_collisions(set, screen, stars, stats, targets, hunter):
    for star in stars:
        collisions = pygame.sprite.groupcollide(stars, targets, True, True)
        if collisions:
            stars.empty()
            set.increase_speed()
            create_target(set, screen, targets)
        elif star.rect.x < 0:
            game_over(set, screen, stats, hunter, targets, stars)


def game_over(set, screen, stats, hunter, targets, stars):
    if stats.game_life > 0:
        stats.game_life -= 1

        targets.empty()
        stars.empty()

        create_target(set, screen, targets)
        hunter.hunter_centet()

        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_targets(targets):
    check_targets_edges(targets)
    targets.update()


def update_screen(set, screen, hunter, targets, stars, stats, play_button):
    screen.fill(set.bg_color)
    for star in stars.sprites():
        star.draw_star()
    hunter.blitme()
    targets.draw(screen)
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def shooting_game():
    pygame.init()
    set = Set()
    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    pygame.display.set_caption("Shooting_game")

    hunter = Hunter(set, screen)
    stars = Group()
    targets = Group()
    create_target(set, screen, targets)
    stats = GameStats(set)
    play_button = Button(screen, "PLAY")

    while True:
        check_events(set, screen, hunter, stars, targets, stats, play_button)
        if stats.game_active:
            hunter.update()
            update_stars(set, screen, stars, stats, targets, hunter)
            update_targets(targets)
        update_screen(set, screen, hunter, targets, stars, stats, play_button)


shooting_game()
