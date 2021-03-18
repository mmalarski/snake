import pygame
import sys
import Collectable

pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100, 100))
test_surface.fill((50, 60, 70))
x_pos = 850
y_pos = 650
cell_size = 40
cell_number = 100

collectable = Collectable.COLLECTABLE(cell_number, cell_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175, 215, 70))
    pygame.display.update()
    clock.tick(60)
