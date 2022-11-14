#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyganim as pyganim
from pygame import *

from constants import ANIMATION_RIGHT, ANIMATION_LEFT, ANIMATION_STAY, ANIMATION_JUMP_RIGHT, ANIMATION_JUMP, \
    ANIMATION_JUMP_LEFT

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"

JUMP_POWER = 10
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.x_speed = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.y_speed = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?

        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        #        Анимация движения вправо
        self.boltAnimRight = pyganim.PygAnimation(ANIMATION_RIGHT)
        self.boltAnimRight.play()
        #        Анимация движения влево
        self.boltAnimLeft = pyganim.PygAnimation(ANIMATION_LEFT)
        self.boltAnimLeft.play()

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()

    def update(self, left, right, up, platforms):
        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.y_speed = -JUMP_POWER

        if left:
            self.x_speed = -MOVE_SPEED  # Лево = x- n

        if right:
            self.x_speed = MOVE_SPEED  # Право = x + n

        if not (left or right):  # стоим, когда нет указаний идти
            self.x_speed = 0
        if not self.onGround:
            self.y_speed += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.y_speed
        self.collide(0, self.y_speed, platforms)

        self.rect.x += self.x_speed  # переносим свои положение на x_speed
        self.collide(self.x_speed, 0, platforms)




    def collide(self, x_speed, y_speed, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if x_speed > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if x_speed < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if y_speed > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.y_speed = 0  # и энергия падения пропадает

                if y_speed < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.y_speed = 0  # и энергия прыжка пропадает