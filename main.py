import pygame
import sys
import Collectable, Snake

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100, 100))
test_surface.fill((50, 60, 70))
x_pos = 850
y_pos = 650


collectable = Collectable.COLLECTABLE(cell_number, cell_size)
snake = Snake.SNAKE(cell_number, cell_size)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175, 215, 70))
    collectable.draw_collectable(screen)
    snake.draw_snake(screen)
    pygame.display.update()
    clock.tick(60)
