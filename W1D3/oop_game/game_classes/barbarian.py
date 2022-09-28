from game_classes.human import Human

class Barbarian(Human):
    def __init__(self, name) -> None:
        super().__init__()
        self.mana = 1
        self.name = name
        self.strength = 10

    