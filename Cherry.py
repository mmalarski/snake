import pygame

from EffectClass import EFFECT


class CHERRY(EFFECT):
    def __init__(self, cell_number, cell_size, game):
        super().__init__(cell_number, cell_size, game)
        self.image = pygame.transform.scale(pygame.image.load('Graphics/cherry.png').convert_alpha(),
                                            (cell_size, cell_size))

    def effect(self, game):
        game.set_time(100)
