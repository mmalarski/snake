import pygame

from PointClass import POINT


class APPLE(POINT):

    def __init__(self, cell_number, cell_size, image):
        super().__init__(cell_number, cell_size)
        self.image = pygame.image.load('Graphics/apple.png').convert_alpha()
        self.image = image

    def process_points(self, snake):
        snake.add_block()
