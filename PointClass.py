from Collectable import COLLECTABLE


class POINT(COLLECTABLE):
    def __init__(self, cell_number, cell_size, image):
        super().__init__(cell_number, cell_size, image)
        self.image = image

    def process_points(self, snake):
        pass

    def do(self, snake=None):
        self.process_points(snake)
