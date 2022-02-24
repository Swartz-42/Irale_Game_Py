from src.entities import Entity

class Player(Entity):

    def __init__(self):
        super().__init__("player", 0, 0)