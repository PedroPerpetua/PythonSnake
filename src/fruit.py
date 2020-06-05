import src.constants as constants
import random
class Fruit:
    def __init__(self):
        self.position = None
        self.reposition()
        self.golden = False
    def reposition(self):
        x = random.randint(0, constants.BOARD_SIZE - 1)
        y = random.randint(0, constants.BOARD_SIZE - 1)
        self.position = (x, y)
        # 10% chance of golden fruit
        self.golden = (random.randint(1, 10) == 10)