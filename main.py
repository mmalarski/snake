import pygame
import sys
import Game
from pygame.math import Vector2

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100, 100))
test_surface.fill((50, 60, 70))
x_pos = 850
y_pos = 650


game = Game.GAME(cell_number, cell_size, screen)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.snake.set_direction(Vector2(0, -1))
            if event.key == pygame.K_DOWN:
                game.snake.set_direction(Vector2(0, 1))
            if event.key == pygame.K_LEFT:
                game.snake.set_direction(Vector2(-1, 0))
            if event.key == pygame.K_RIGHT:
                game.snake.set_direction(Vector2(1, 0))

    screen.fill((175, 215, 70))
    game.draw_elements()
    pygame.display.update()
    clock.tick(60)
