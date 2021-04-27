import pygame,sys
from pygame.math import Vector2
import RetryPopUp


class SNAKE:
    def __init__(self, cell_number, cell_size):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.speed = 150
        self.head = None
        self.tail = None

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
        # i = 0
        # for block in self.body:
        #     snake_rect = pygame.Rect(int(block.x * self.cell_size), int(block.y * self.cell_size),
        #                              self.cell_size, self.cell_size)
        #     if i % 2 == 0:
        #         pygame.draw.rect(screen, (183, 111, 122), snake_rect)
        #     else:
        #         pygame.draw.rect(screen, (150, 110, 120), snake_rect)
        #     i += 1
        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):
            snake_rect = pygame.Rect(int(block.x * self.cell_size), int(block.y * self.cell_size),
                                         self.cell_size, self.cell_size)
            if index == 0:
                screen.blit(self.head, snake_rect)
            elif index == len(self.body) -1:
                screen.blit(self.tail, snake_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, snake_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, snake_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, snake_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, snake_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, snake_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, snake_rect)


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
            RetryPopUp.retry()
        else:
            self.body = self.body[:-1]

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down