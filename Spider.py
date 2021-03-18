import sys

import pygame

from EffectClass import EFFECT


class SPIDER(EFFECT):

    def __init__(self, cell_number, cell_size, game):
        super().__init__(cell_number, cell_size, game)

    def effect(self, game):
        game.game_over()
