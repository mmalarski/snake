import pygame

from PointClass import POINT


class BANANA(POINT):

    def __init__(self, cell_number, cell_size, image):
        super().__init__(cell_number, cell_size)
        self.image = pygame.image.load('Graphics/ant.svg').convert_alpha()
        self.image = image

    def process_points(self, snake):
        snake.add_block()
        snake.add_block()
