#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from blocks import Platform, BlockDie, BlockTeleport, Princess
from pygame import *
from helperspygame import RendererPygame



from loadlevels import LoadLevel
from monsters import Monster
from player import Player
from utils import camera_configure
from camera import Camera
from constants import DISPLAY, WIN_WIDTH, WIN_HEIGHT, BACKGROUND_COLOR, LIMIT_FPS, PLATFORM_WIDTH, \
    PLATFORM_HEIGHT, PLATFORM_COLOR, CENTER_OF_SCREEN


def main():
    loadlevel = LoadLevel()
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Super Mario Boy")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон

    renderer = RendererPygame()  # визуализатор
    for lvl in range(1, 4):
        loadlevel.loadlevel("levels/map_%s" % lvl, platforms, entities, animatedEntities, monsters)
        bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом

        left = right = False  # по умолчанию - стоим
        up = False
        running = False
        try:
            hero = Player(loadlevel.playerX, loadlevel.playerY)  # создаем героя по (x,y) координатам
            entities.add(hero)
        except:
            print (u"Не удалось на карте найти героя, взяты координаты по-умолчанию")
            hero = Player(65, 65)
        entities.add(hero)

        timer = pygame.time.Clock()

        camera = Camera(camera_configure, loadlevel.total_level_width, loadlevel.total_level_height)

        while not hero.winner:  # Основной цикл программы
            timer.tick(60)
            for e in pygame.event.get():  # Обрабатываем события
                if e.type == QUIT:
                    raise SystemExit, "QUIT"
                if e.type == KEYDOWN and e.key == K_UP:
                    up = True
                if e.type == KEYDOWN and e.key == K_LEFT:
                    left = True
                if e.type == KEYDOWN and e.key == K_RIGHT:
                    right = True
                if e.type == KEYDOWN and e.key == K_LSHIFT:
                    running = True

                if e.type == KEYUP and e.key == K_UP:
                    up = False
                if e.type == KEYUP and e.key == K_RIGHT:
                    right = False
                if e.type == KEYUP and e.key == K_LEFT:
                    left = False
                if e.type == KEYUP and e.key == K_LSHIFT:
                    running = False
            for sprite_layer in loadlevel.sprite_layers:  # перебираем все слои
                if not sprite_layer.is_object_group:  # и если это не слой объектов
                    renderer.render_layer(screen, sprite_layer)  # отображаем его

            for e in entities:
                screen.blit(e.image, camera.apply(e))
            animatedEntities.update()  # показываеaм анимацию
            monsters.update(platforms)  # передвигаем всех монстров
            camera.update(hero)  # центризируем камеру относительно персонаж
            center_offset = camera.reverse(CENTER_OF_SCREEN)  # получаем координаты внутри длинного уровня
            renderer.set_camera_position_and_size(center_offset[0], center_offset[1], \
                                                  WIN_WIDTH, WIN_HEIGHT, "center")
            hero.update(left, right, up, running, platforms)  # передвижение
            pygame.display.update()  # обновление и вывод всех изменений на экран
            screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        for sprite_layer in loadlevel.sprite_layers:
            if not sprite_layer.is_object_group:
                renderer.render_layer(screen, sprite_layer)
        # когда заканчиваем уровень
        for e in entities:
            screen.blit(e.image, camera.apply(e))  # еще раз все перерисовываем
        font = pygame.font.Font(None, 38)
        text = font.render(("Thank you MarioBoy! but our princess is in another level!"), 1,
                           (255, 255, 255))  # выводим надпись
        screen.blit(text, (10, 100))
        pygame.display.update()
        time.wait(10000)  # ждем 10 секунд и после - переходим на следующий уровень


level = []
entities = pygame.sprite.Group()  # Все объекты
animatedEntities = pygame.sprite.Group()  # все анимированные объекты, за исключением героя
monsters = pygame.sprite.Group()  # Все передвигающиеся объекты
platforms = []  # то, во что мы будем врезаться или опираться
if __name__ == "__main__":
    main()