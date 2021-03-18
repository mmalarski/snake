from PointClass import POINT
from EffectClass import EFFECT


class WATERMELON(POINT, EFFECT):

    def __init__(self, cell_number, cell_size):
        super().__init__(cell_number, cell_size)

    def process_points(self, snake):
        snake.add_block()
        snake.add_block()
