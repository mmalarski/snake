import pygame
import sys
import Game
from pygame.math import Vector2

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
clock2 = pygame.time.Clock()
test_surface = pygame.Surface((100, 100))
test_surface.fill((50, 60, 70))
x_pos = 850
y_pos = 650

SCREEN_UPDATE = pygame.USEREVENT
game = Game.GAME(cell_number, cell_size, screen, SCREEN_UPDATE)

flag = True

while True:
    if game.snake.speed != 150 and flag:
        clock2.tick()
        flag = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.snake.direction.y != 1:
                    game.snake.set_direction(Vector2(0, -1))
            if event.key == pygame.K_DOWN:
                if game.snake.direction.y != -1:
                    game.snake.set_direction(Vector2(0, 1))
            if event.key == pygame.K_LEFT:
                if game.snake.direction.x != 1:
                    game.snake.set_direction(Vector2(-1, 0))
            if event.key == pygame.K_RIGHT:
                if game.snake.direction.x != -1:
                    game.snake.set_direction(Vector2(1, 0))

    print(clock2.get_time())
    if clock2.get_time() > 5000:
        game.set_time(150)
        flag = True

    screen.fill((175, 215, 70))
    game.draw_elements()
    pygame.display.update()
    clock.tick(60)
