from Collectable import COLLECTABLE


class EFFECT(COLLECTABLE):
    def __init__(self, cell_number, cell_size, image, game):
        super().__init__(cell_number, cell_size, image)
        self.game = game
        self.image = image

    def effect(self, game):
        pass

    def do(self, snake=None):
        self.effect(self.game)
