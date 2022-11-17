#! /usr/bin/env python
# -*- coding: utf-8 -*-
from blocks import BlockTeleport

class LoadLevel:
    playerX = 0
    playerY = 0

    def loadLevel(self, level, entities, platforms, animatedEntities, monsters, Monster):
        playerX = 0
        playerY = 0  # объявляем глобальные переменные, это координаты героя

        levelFile = open('./levels/1.txt')
        line = " "
        commands = []
        while line[0] != "/":  # пока не нашли символ завершения файла
            line = levelFile.readline()  # считываем построчно
            if line[0] == "[":  # если нашли символ начала уровня
                while line[0] != "]":  # то, пока не нашли символ конца уровня
                    line = levelFile.readline()  # считываем построчно уровень
                    if line[0] != "]":  # и если нет символа конца уровня
                        endLine = line.find("|")  # то ищем символ конца строки
                        level.append(line[0: endLine])  # и добавляем в уровень строку от начала до символа "|"

            if line[0] != "":  # если строка не пустая
                commands = line.split()  # разбиваем ее на отдельные команды
                if len(commands) > 1:  # если количество команд > 1, то ищем эти команды
                    if commands[0] == "player":  # если первая команда - player
                        self.playerX = int(commands[1])  # то записываем координаты героя
                        self.playerY = int(commands[2])
                    if commands[0] == "portal":  # если первая команда portal, то создаем портал
                        tp = BlockTeleport(int(commands[1]), int(commands[2]), int(commands[3]), int(commands[4]))
                        entities.add(tp)
                        platforms.append(tp)
                        animatedEntities.add(tp)
                    if commands[0] == "monster":  # если первая команда monster, то создаем монстра
                        mn = Monster(int(commands[1]), int(commands[2]), int(commands[3]), int(commands[4]),
                                              int(commands[5]), int(commands[6]))
                        entities.add(mn)
                        platforms.append(mn)
                        monsters.add(mn)