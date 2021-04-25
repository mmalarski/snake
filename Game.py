import sys
import random

import Ant
import Apple
import Banana
import Cherry
import Moth
import Spider
import Watermelon
import pygame

import Snake

SCREEN_UPDATE = pygame.USEREVENT




class GAME:
    def __init__(self, cell_number, cell_size, screen, evt):
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.screen = screen
        self.game_font = pygame.font.Font(None, 25)
        self.snake = Snake.SNAKE(cell_number, cell_size)
        self.ap = Apple.APPLE(self.cell_number, self.cell_size)
        self.b = Banana.BANANA(cell_number, cell_size)
        self.an = Ant.ANT(self.cell_number, self.cell_size)
        self.w = Watermelon.WATERMELON(cell_number, cell_size, self)
        self.s = Spider.SPIDER(self.cell_number, self.cell_size, self)
        self.m = Moth.MOTH(self.cell_number, self.cell_size, self)
        self.c = Cherry.CHERRY(cell_number, cell_size, self)
        self.collectables = [self.ap, self.b, self.an, self.w, self.s, self.m, self.c]
        self.collectable = random.choice(self.collectables)
        self.set_time(150)

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.collectable.draw_collectable(self.screen)
        self.snake.draw_snake(self.screen)
        self.draw_score()

    def check_collision(self):
        if self.collectable.pos == self.snake.body[0]:
            self.collectable = random.choice(self.collectables)
            self.collectable.randomise()
            self.collectable.do(self.snake)

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = self.game_font.render(score_text, True, (56, 74, 12))
        score_x = int(self.cell_size * self.cell_number - 60)
        score_y = int(self.cell_size * self.cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        self.screen.blit(score_surface, score_rect)

    def set_time(self, speed):
        pygame.time.set_timer(SCREEN_UPDATE, speed)
        self.snake.speed = speed

    def game_over(self):
        pygame.quit()
        sys.exit()