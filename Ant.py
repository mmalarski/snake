from PointClass import POINT


class ANT(POINT):

    def __init__(self, cell_number, cell_size):
        super().__init__(cell_number, cell_size)

    def process_points(self, snake):
        snake.remove_block()
