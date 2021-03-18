import pygame, sys, Collectable

pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100, 100))
test_surface.fill((50, 60, 70))
x_pos = 850
y_pos = 650
cell_size = 40
cell_number = 100

collectable = Collectable.COLLECTABLE()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    screen.blit(test_surface, (x_pos, y_pos))
    if x_pos != 0:
        x_pos -= 1
    if y_pos != 0:
        y_pos -=1
    pygame.display.update()
    clock.tick(60)
