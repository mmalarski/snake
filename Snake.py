import pygame
from pygame.math import Vector2


class SNAKE:
    def __init__(self, cell_number, cell_size):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self, screen):
        for block in self.body:
            snake_rect = pygame.Rect(int(block.x * self.cell_size), int(block.y * self.cell_size),
                                     self.cell_size, self.cell_size)
            pygame.draw.rect(screen, (183, 111, 122), snake_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
