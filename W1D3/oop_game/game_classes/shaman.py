from game_classes.human import Human

class Shaman(Human):
    def __init__(self,name):
        super().__init__()
        self.mana = 10
        self.totem = "a cool magic thing"
        self.name = name

    def use_totem(self):
        print(f"The Shaman looks at their {self.totem} and it fills them with magical knowledge (Mana +1)")
        self.mana += 1

    def heal(self):
        super().heal()
        print(f"The healing cost you one point of armor")
        self.armor -= 1

    

