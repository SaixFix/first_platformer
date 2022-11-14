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
    "-------------------------",
    "-                       -",
    "-                       -",
    "-                       -",
    "-            --         -",
    "-                       -",
    "--                      -",
    "-                       -",
    "-                   --- -",
    "-                       -",
    "-                       -",
    "-      ---              -",
    "-                       -",
    "-   -----------        -",
    "-                       -",
    "-                -      -",
    "-                   --  -",
    "-                       -",
    "-                       -",
    "-------------------------"]

#Константы блоков

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

#Константы анимации героя
ANIMATION_DELAY = 0.1 # скорость смены кадров
ANIMATION_RIGHT = 'knight/Run.gif'

ANIMATION_LEFT = 'knight/__Run_Left.gif'

ANIMATION_JUMP_LEFT = [('knight/__Jump_left.gif', 0.1)]
ANIMATION_JUMP_RIGHT = [('knight/__Jump.gif', 0.1)]
ANIMATION_JUMP = [('knight/__Jump.gif', 0.1)]
ANIMATION_STAY = [('knight/__Idle.gif', 0.1)]


