import pygame

from EffectClass import EFFECT


class SPIDER(EFFECT):
    def __init__(self, cell_number, cell_size, image, game):
        super().__init__(cell_number, cell_size, game)
        self.image = pygame.image.load('Graphics/ant.svg').convert_alpha()
        self.image = image

    def effect(self, game):
        game.game_over()
