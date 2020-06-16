import pygame as pg
from assets.assets import Assets, Colors

class Label:
    def __init__(self, text, size, x, y):
        self.text = pg.font.Font(Assets.BOXY_FONT, size).render(text, True, Colors.BLACK)
        self.pos = (x, y)
    def draw(self, window):
        window.blit(self.text, self.pos)
    def update(self, _):
        pass
