import sys
import pygame
from rain import Car


def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def create_cars(ai_set, screen, cars):
    car = Car(ai_set, screen)
    car_width = car.rect.width
    car_height = car.rect.height
    available_spare_x = ai_set.screen_width - 2 * car_width
    number_car_x = int(available_spare_x / (2 * car_width))
    available_spare_y = ai_set.screen_height - car_height
    number_car_y = int(available_spare_y / (2 * car_height))

    for car_number in range(number_car_x):
        for number_car in range(number_car_y):
            car = Car(ai_set, screen)
            car.x = car_width + 2 * car_width * car_number
            car.rect.x = car.x
            car.rect.y = car_height + 2 * car_height * number_car
            cars.add(car)


# def change_direction(ai_set, screen, cars):


def update_cars(ai_set, screen, cars):
    cars.update()
    for car in cars.copy():
        if car.rect.top >= ai_set.screen_height:
            cars.remove(car)

    if car.rect.top >= ai_set.screen_height:
        create_cars(ai_set, screen, cars)


def update_screen(ai_set, screen, cars):
    screen.fill(ai_set.bg_color)
    cars.draw(screen)
    pygame.display.flip()
