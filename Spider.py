import pygame

from EffectClass import EFFECT


class SPIDER(EFFECT):
    def __init__(self, cell_number, cell_size, game):
        super().__init__(cell_number, cell_size, game)
        self.image = pygame.image.load('Graphics/ant.svg').convert_alpha()


    def effect(self, game):
        game.game_over()
