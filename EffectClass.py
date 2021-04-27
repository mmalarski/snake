from Collectable import COLLECTABLE


class EFFECT(COLLECTABLE):
    def __init__(self, cell_number, cell_size, game):
        super().__init__(cell_number, cell_size)
        self.game = game

    def effect(self, game):
        pass

    def do(self, snake=None):
        self.effect(self.game)
