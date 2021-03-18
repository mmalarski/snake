import pygame, random
import main
from pygame.math import Vector2


class COLLECTABLE:
    def __init__(self):
        self.x = random.randint(0, main.cell_number - 1)
        self.y = random.randint(0, main.cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_collectable(self):
        collectable_rect = pygame.Rect(int(self.pos.x * main.cell_size), int(self.pos.y * main.cell_size), main.cell_size,
                                       main.cell_size)
        pygame.draw.rect(main.screen, (126, 166, 114), collectable_rect)

