import sys
import pygame
import Snake, Collectable, Banana


class GAME:
    def __init__(self, cell_number, cell_size, screen):
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.screen = screen
        self.game_font = pygame.font.Font(None, 25)
        self.snake = Snake.SNAKE(cell_number, cell_size)
        self.collectable = Banana.BANANA(cell_number, cell_size)

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
            self.collectable.randomise()
            self.collectable.do(self.snake)

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = self.game_font.render(score_text, True, (56, 74, 12))
        score_x = int(self.cell_size * self.cell_number - 60)
        score_y = int(self.cell_size * self.cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        self.screen.blit(score_surface, score_rect)
