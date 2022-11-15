#! /usr/bin/env python
# -*- coding: utf-8 -*-
from pygame import Rect


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        """все объекты рисуются в меньшем прямоугольнике"""
        return target.rect.move(self.state.topleft)

    def update(self, target):
        """Меньший прямоугольник центрируется относительно главного персонажа"""
        self.state = self.camera_func(self.state, target.rect)


