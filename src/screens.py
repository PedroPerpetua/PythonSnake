import pygame as pg
from src.game import Game

class GameScreen:
	def __init__(self):
		self.items = {}
		self.items["game"] = {}
		self.items["game"]["game"] = Game(10, 10)
		self.game = None
	def draw(self, window):
		window.fill((255, 255, 255))
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].draw(window)
	def update(self, events):
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].update(events)

	@staticmethod
	def screen_loop(window):
		screen = GameScreen()
		while True:
			events = pg.event.get()
			for event in events:
				if event.type == pg.QUIT:
					#EXIT PROMPT
					pass
			
			screen.draw(window)
			screen.update(events)
			pg.display.update()
