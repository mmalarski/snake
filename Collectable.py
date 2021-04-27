import pygame
import random
from pygame.math import Vector2


class COLLECTABLE:
    def __init__(self, cell_number, cell_size):
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.randomise()

    def draw_collectable(self, screen, image):
        collectable_rect = pygame.Rect(int(self.pos.x * self.cell_size), int(self.pos.y * self.cell_size),
                                       self.cell_size, self.cell_size)
        screen.blit(image, collectable_rect)

    def randomise(self):
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def do(self, snake=None):
        pass
