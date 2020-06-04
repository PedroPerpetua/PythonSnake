import pygame as pg
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Snake:
    def __init__(self, x, y):
        self.body = [(x, y), (x - 1, y), (x - 2, y)]
        self.direction = WEST
        self.timer = pg.time.Clock()
    
    def update(self, events):
        self.timer.tick()
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key in [pg.K_UP, pg.K_w]:
                    self.direction = NORTH
                elif event.key in [pg.K_RIGHT, pg.K_d]:
                    self.direction = EAST
                elif event.key in [pg.K_DOWN, pg.K_s]:
                    self.direction = SOUTH
                elif event.key in [pg.K_LEFT, pg.K_a]:
                    self.direction = WEST
        
    def draw(self, window):
        pass