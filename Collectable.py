import pygame
import main
from pygame.math import Vector2

class COLLECTABTE:
    def __init__(self):
        self.x = 5
        self.y = 4
        self.pos = Vector2(self.x, self.y)

    def draw_collectable(self):
        collectable_rect = pygame.Rect(self.pos.x * main.cell_size, self.pos.y * main.cell_size, main.cell_size,
                                       main.cell_size)
        pygame.draw.rect(main.screen, (126, 166, 114), collectable_rect)

