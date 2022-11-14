#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from blocks import Platform
from pygame import *

from constants import DISPLAY, WIN_WIDTH, WIN_HEIGHT, BACKGROUND_COLOR, LIMIT_FPS, level, PLATFORM_WIDTH, \
    PLATFORM_HEIGHT, PLATFORM_COLOR
from player import Player


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Knight of the moon")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом

    hero = Player(55, 55)  # создаем героя по (x,y) координатам
    left = right = False  # по умолчанию — стоим
    up = False

    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться

    entities.add(hero)

    timer = pygame.time.Clock()

    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    while 1:  # Основной цикл программы
        timer.tick(LIMIT_FPS) #ограничение кол кадров
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == KEYDOWN and e.key == K_UP:
                up = True

            if e.type == KEYUP and e.key == K_UP:
                up = False

            if e.type == QUIT:
                raise SystemExit, "QUIT"
        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        hero.update(left, right, up)  # передвижение
        entities.draw(screen)  # отображение всего


        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()
