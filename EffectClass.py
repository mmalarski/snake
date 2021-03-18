import Collectable


class EFFECT(Collectable):
    def __init__(self, cell_number, cell_size):
        super().__init__(self, cell_number, cell_size)

    def effect(self):
        print()

    def do(self, snake):
        self.effect()