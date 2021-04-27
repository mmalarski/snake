import pygame,sys
from pygame.math import Vector2


class SNAKE:
    def __init__(self, cell_number, cell_size):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.speed = 150

        self.head_up = pygame.transform.scale(pygame.image.load('Graphics/head_up.png').convert_alpha().convert_alpha(),
                                              (cell_size, cell_size))
        self.head_down = pygame.transform.scale(pygame.image.load('Graphics/head_down.png').convert_alpha()
                                                .convert_alpha(), (cell_size, cell_size))
        self.head_right = pygame.transform.scale(pygame.image.load('Graphics/head_right.png').convert_alpha()
                                                 .convert_alpha(), (cell_size, cell_size))
        self.head_left = pygame.transform.scale(pygame.image.load('Graphics/head_left.png').convert_alpha()
                                                .convert_alpha(), (cell_size, cell_size))

        self.tail_up = pygame.transform.scale(pygame.image.load('Graphics/tail_up.png').convert_alpha().convert_alpha(), (cell_size, cell_size))
        self.tail_down = pygame.transform.scale(pygame.image.load('Graphics/tail_down.png').convert_alpha()
                                                .convert_alpha(), (cell_size, cell_size))
        self.tail_right = pygame.transform.scale(pygame.image.load('Graphics/tail_right.png').convert_alpha()
                                                 .convert_alpha(), (cell_size, cell_size))
        self.tail_left = pygame.transform.scale(pygame.image.load('Graphics/tail_left.png').convert_alpha()
                                                .convert_alpha(), (cell_size, cell_size))

        self.body_vertical = pygame.transform.scale(pygame.image.load('Graphics/body_vertical.png').convert_alpha()
                                                    .convert_alpha(), (cell_size, cell_size))
        self.body_horizontal = pygame.transform.scale(pygame.image.load('Graphics/body_horizontal.png').convert_alpha()
                                                      .convert_alpha(), (cell_size, cell_size))

        self.body_tr = pygame.transform.scale(pygame.image.load('Graphics/body_tr.png').convert_alpha().convert_alpha(),
                                              (cell_size, cell_size))
        self.body_tl = pygame.transform.scale(pygame.image.load('Graphics/body_tl.png').convert_alpha().convert_alpha(),
                                              (cell_size, cell_size))
        self.body_br = pygame.transform.scale(pygame.image.load('Graphics/body_br.png').convert_alpha().convert_alpha(),
                                              (cell_size, cell_size))
        self.body_bl = pygame.transform.scale(pygame.image.load('Graphics/body_bl.png').convert_alpha().convert_alpha(),
                                              (cell_size, cell_size))

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
        body_copy = self.body[:]
        body_copy.insert(len(body_copy), body_copy[-1] + last_vector)
        self.body = body_copy[:]

    def remove_block(self):
        if len(self.body) < 4:
            pygame.quit()
            sys.exit()
        else:
            self.body = self.body[:-1]
