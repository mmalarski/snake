import sys
import pygame
import Snake, Collectable


class GAME:
    def __init__(self, cell_number, cell_size, screen):
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.screen = screen
        self.snake = Snake.SNAKE(cell_number, cell_size)
        self.collectable = Collectable.COLLECTABLE(cell_number, cell_size)

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.collectable.draw_collectable(self.screen)
        self.snake.draw_snake(self.screen)

    def check_collision(self):
        if self.collectable.pos == self.snake.body[0]:
            self.collectable.randomise()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x <= self.cell_number:
            self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()
