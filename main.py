import pygame
import sys
import Game
from pygame.math import Vector2
import time

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 100))
test_surface.fill((50, 60, 70))
x_pos = 850
y_pos = 650

SCREEN_UPDATE = pygame.USEREVENT
game = Game.GAME(cell_number, cell_size, screen, SCREEN_UPDATE)

flag = True
start = 0
reload = time.time()
while True:
    if game.snake.speed != 150 and flag:
        start = time.time()
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

    if (time.time() - start) > 10 and flag == False:
        game.set_time(150)
        flag = True
        start = 0

    if (time.time() - reload) > 10:
        game.reload_bad_coll()
        reload = time.time()

    screen.fill((175, 215, 70))
    game.draw_elements()
    pygame.display.update()
    clock.tick(60)
