import pygame

from EffectClass import EFFECT


class MOTH(EFFECT):

    def __init__(self, cell_number, cell_size, game):
        super().__init__(cell_number, cell_size, game)
        self.image = pygame.transform.scale(pygame.image.load('Graphics/moth.png').convert_alpha(),
                                            (cell_size, cell_size))

    def effect(self):
        self.game.set_time(500)
