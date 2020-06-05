import pygame as pg
from assets.assets import Assets, Colors

class TextButton:
    def __init__(self, text, x, y):
        self.clicked = False
        self.hovered = False
        self.text = pg.font.Font(Assets.BOXY_FONT, 32).render(text, True, Colors.BLACK)
        self.box = pg.rect.Rect((x, y), (280, 64))
        self.position = (self.box.centerx - self.text.get_rect().centerx, self.box.centery - self.text.get_rect().centery + 3)
    def draw(self, window):
        if not self.hovered:
            window.blit(Assets.BUTTON_DEFAULT, self.box)
        else:
            window.blit(Assets.BUTTON_HOVERED, self.box)
        window.blit(self.text, self.position)
    def update(self, events):
        self.hovered = False
        if self.box.collidepoint(pg.mouse.get_pos()):
            self.hovered = True
        self.clicked = False
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN and self.hovered:
                self.clicked = True