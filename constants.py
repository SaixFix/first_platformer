#! /usr/bin/env python
# -*- coding: utf-8 -*-

PATCH_BLOCKS = "blocks/platform.png"


# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"

LIMIT_FPS = 60

#константы уровня
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

level = [
       "----------------------------------",
       "-                                -",
       "-                       --       -",
       "-                                -",
       "-            --                  -",
       "-                                -",
       "--                               -",
       "-                                -",
       "-                   ----     --- -",
       "-                                -",
       "--                               -",
       "-                                -",
       "-                            --- -",
       "-                                -",
       "-                                -",
       "-      ---                       -",
       "-                                -",
       "-   -------         ----         -",
       "-                                -",
       "-                         -      -",
       "-                            --  -",
       "-                                -",
       "-                                -",
       "----------------------------------"]

#Константы блоков

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

#Константы анимации героя
ANIMATION_DELAY = 50 # скорость смены кадров
ANIMATION_RIGHT = [('knight/r1.png'),
            ('knight/r2.png'),
            ('knight/r3.png'),
            ('knight/r4.png'),
            ('knight/r5.png'),
            ('knight/r6.png'),
            ('knight/r7.png'),
            ('knight/r8.png'),
            ('knight/r9.png'),
            ('knight/r10.png')]

ANIMATION_LEFT = [('knight/l1.png'),
            ('knight/l2.png'),
            ('knight/l3.png'),
            ('knight/l4.png'),
            ('knight/l5.png'),
            ('knight/l6.png'),
            ('knight/l7.png'),
            ('knight/l8.png'),
            ('knight/l9.png'),
            ('knight/l10.png')]
ANIMATION_JUMP_LEFT = [('knight/jump_l.png', 1)]
ANIMATION_JUMP_RIGHT = [('knight/jump_r.png', 1)]
ANIMATION_JUMP = [('knight/jump_r.png', 1)]
ANIMATION_STAY = [('knight/0.png', 1)]


