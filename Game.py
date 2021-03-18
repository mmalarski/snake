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

    def draw_elements(self):
        self.collectable.draw_collectable(self.screen)
        self.snake.draw_snake(self.screen)