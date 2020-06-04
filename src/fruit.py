import src.constants as constants
import random

class Fruit:
    def __init__(self):
        self.position = None
        self.reposition()
    def reposition(self):
        x = random.randint(0, constants.BOARD_SIZE - 1)
        y = random.randint(0, constants.BOARD_SIZE - 1)
        self.position = (x, y)