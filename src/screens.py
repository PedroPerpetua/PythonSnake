import pygame as pg
from src.game import Game

class StartScreen:
	def __init__(self):
		self.items = {}
	def draw(self, window):
		for item_type in self.items:
			for item in self.items[item_type]:
				item.draw(window)
	def update(self, window):
		for item_type in self.items:
			for item in self.items[item_type]:
				item.update(window)
	@staticmethod
	def screen_loop(window):
		screen = StartScreen()
		while True:
			events = pg.event.get()
			for event in events:
				if event.type == pg.QUIT:
					pass
			screen.draw(window)
			screen.update(window)
			pg.display.update()

class CreditsScreen:
	def __init__(self):
		self.items = {}
	def draw(self, window):
		for item_type in self.items:
			for item in self.items[item_type]:
				item.draw(window)
	def update(self, window):
		for item_type in self.items:
			for item in self.items[item_type]:
				item.update(window)
	@staticmethod
	def screen_loop(window):
		screen = CreditsScreen()
		while True:
			events = pg.event.get()
			for event in events:
				if event.type == pg.QUIT:
					pass
			screen.draw(window)
			screen.update(window)
			pg.display.update()

class HighscoreScreen:
	def __init__(self):
		self.items = {}
	def draw(self, window):
		for item_type in self.items:
			for item in self.items[item_type]:
				item.draw(window)
	def update(self, window):
		for item_type in self.items:
			for item in self.items[item_type]:
				item.update(window)
	@staticmethod
	def screen_loop(window):
		screen = HighscoreScreen()
		while True:
			events = pg.event.get()
			for event in events:
				if event.type == pg.QUIT:
					pass
			screen.draw(window)
			screen.update(window)
			pg.display.update()

class GameScreen:
	def __init__(self):
		self.game = Game(0, 0)
	def draw(self, window):
		window.fill((255, 255, 255))
		self.game.draw(window)
	def update(self, events):
		self.game.update(events)
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
