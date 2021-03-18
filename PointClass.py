from Collectable import COLLECTABLE


class POINT(COLLECTABLE):
    def __init__(self, cell_number, cell_size):
        super().__init__(cell_number, cell_size)

    def process_points(self, snake):
        pass

    def do(self, snake):
        self.process_points(snake)
