import pygame as pg
import src.constants as constants
from assets.assets import Assets
from src.snake import Snake
from src.fruit import Fruit 

class Game:
    def __init__(self, x, y):
        size = constants.BOARD_SIZE * constants.PIXEL_SIZE
        border_size = constants.BORDER_SIZE * 2 + size
        self.border_box = pg.rect.Rect((x, y), (border_size, border_size))
        self.box = pg.rect.Rect((x + constants.BORDER_SIZE, y + constants.BORDER_SIZE), (size, size))
        self.score = 0
        self.snake = Snake(int(constants.BOARD_SIZE / 2), constants.BOARD_SIZE / 2)
        self.fruit = Fruit()
        self.clock = pg.time.Clock()
        self.count = 0
    def draw(self, window):
        pg.draw.rect(window, (0, 0, 0), self.box)
        # Draw the snake
        head = self.snake.body[0]
        head_x, head_y = self.box.left + constants.PIXEL_SIZE * head[0], self.box.top + constants.PIXEL_SIZE * head[1]
        rotated_head = pg.transform.rotate(Assets.HEAD, self.snake.direction)
        window.blit(rotated_head, (head_x, head_y))
        for part in self.snake.body[1:]:
            x, y = self.box.left + constants.PIXEL_SIZE * part[0], self.box.top + constants.PIXEL_SIZE * part[1]
            window.blit(Assets.BODY, (x, y))
        # Draw the fruit
        x, y = self.box.left + constants.PIXEL_SIZE * self.fruit.position[0], self.box.top + constants.PIXEL_SIZE * self.fruit.position[1]
        window.blit(Assets.FRUIT, (x, y))
    def update(self, events):
        self.clock.tick()
        self.count += self.clock.get_time()
        if self.count > constants.TICK:
            self.count %= constants.TICK
            self.snake.move()
            if self.snake.body[0] == self.fruit.position:
                while self.fruit.position in self.snake.body:
                    self.fruit.reposition()
                self.snake.grow()
                self.score += 1

        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key in (pg.K_UP, pg.K_w):
                    self.snake.change_direction(constants.NORTH)
                elif event.key in (pg.K_RIGHT, pg.K_d):
                    self.snake.change_direction(constants.EAST)
                elif event.key in (pg.K_DOWN, pg.K_s):
                    self.snake.change_direction(constants.SOUTH)
                elif event.key in (pg.K_LEFT, pg.K_a):
                    self.snake.change_direction(constants.WEST)