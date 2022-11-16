#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from blocks import Platform, BlockDie, BlockTeleport, Princess
from pygame import *

from monsters import Monster
from player import Player
from utils import camera_configure
from camera import Camera
from constants import DISPLAY, WIN_WIDTH, WIN_HEIGHT, BACKGROUND_COLOR, LIMIT_FPS, level, PLATFORM_WIDTH, \
    PLATFORM_HEIGHT, PLATFORM_COLOR


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Knight of the moon")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом

    hero = Player(100, 700)  # создаем героя по (x,y) координатам
    left = right = False  # по умолчанию — стоим
    up = False
    running = False

    entities = pygame.sprite.Group()  # Все объекты
    animatedEntities = pygame.sprite.Group()  # все анимированные объекты, за исключением героя
    monsters = pygame.sprite.Group()  # Все передвигающиеся объекты
    platforms = []  # то, во что мы будем врезаться или опираться

    mn = Monster(190, 200, 2, 3, 150, 15)
    entities.add(mn)
    platforms.append(mn)
    monsters.add(mn)
    monsters.update(platforms)  # передвигаем всех монстров

    tp = BlockTeleport(128, 512, 800, 64)
    entities.add(tp)
    platforms.append(tp)
    animatedEntities.add(tp)

    entities.add(hero)

    animatedEntities.update()

    timer = pygame.time.Clock()

    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)

            if col == "*":
                bd = BlockDie(x, y)
                entities.add(bd)
                platforms.append(bd)

            if col == "P":
                pr = Princess(x, y)
                entities.add(pr)
                platforms.append(pr)
                animatedEntities.add(pr)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)

    while 1:  # Основной цикл программы
        timer.tick(LIMIT_FPS)  # ограничение кол кадров
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_LSHIFT:
                running = True

            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == KEYDOWN and e.key == K_UP:
                up = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_LSHIFT:
                running = False

            if e.type == QUIT:
                raise SystemExit, "QUIT"

        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        camera.update(hero)  # центризируем камеру относительно персонажа
        hero.update(left, right, up, running, platforms)  # передвижение
        for e in entities:
            screen.blit(e.image, camera.apply(e))  # отображение всего

        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()
