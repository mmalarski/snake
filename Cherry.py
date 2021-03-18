from EffectClass import EFFECT


class CHERRY(EFFECT):

    def __init__(self, cell_number, cell_size):
        super().__init__(cell_number, cell_size)

    def effect(self):
        print()
