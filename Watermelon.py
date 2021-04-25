from PointClass import POINT
from EffectClass import EFFECT


class WATERMELON(EFFECT, POINT):

    def __init__(self, cell_number, cell_size, game):
        super().__init__(cell_number, cell_size, game)
        super(EFFECT, self).__init__(cell_number, cell_size)

    def process_points(self, snake):
        snake.add_block()
        snake.add_block()

    def effect(self, game):
        game.set_time(100)

    def do(self, snake=None):
        self.process_points(snake)
        self.effect(self.game)
