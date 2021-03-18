import Collectable


class EFFECT(Collectable):
    def __init__(self, cell_number, cell_size):
        super().__init__(self, cell_number, cell_size)
        self.effect = effect

    def effect(self):
        print()