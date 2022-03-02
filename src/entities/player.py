from src.entities import Entity

class Player(Entity):

    def __init__(self):
        super().__init__("player", 4, 4)
        self.health = 100
        self.mana = 100
