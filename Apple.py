import pygame

from PointClass import POINT


class APPLE(POINT):

    def __init__(self, cell_number, cell_size):
        super().__init__(cell_number, cell_size)
        self.image = pygame.image.load('Graphics/apple.png').convert_alpha()

    def process_points(self, snake):
        snake.add_block()
