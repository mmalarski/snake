import pygame
from pygame.math import Vector2


class SNAKE:
    def __init__(self, cell_number, cell_size):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)

    def set_direction(self, value):
        self.direction = value

    def draw_snake(self, screen):
        i = 0
        for block in self.body:
            snake_rect = pygame.Rect(int(block.x * self.cell_size), int(block.y * self.cell_size),
                                     self.cell_size, self.cell_size)
            if i % 2 == 0:
                pygame.draw.rect(screen, (183, 111, 122), snake_rect)
            else:
                pygame.draw.rect(screen, (150, 110, 120), snake_rect)
            i += 1

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        last_vector = Vector2(self.body[-1].x - self.body[-2].x, self.body[-1].y - self.body[-2].y)
        print(last_vector)
        body_copy = self.body[:]
        body_copy.insert(len(body_copy), body_copy[-1] + last_vector)
        self.body = body_copy[:]
