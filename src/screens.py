import pygame as pg
import sys
from assets.assets import Assets, Colors
from src.text_button import TextButton
from src.game import Game

class StartScreen:
	def __init__(self):
		self.items = {}
		self.items["button"] = {}
		self.items["button"]["play"] = TextButton("Play!", 212, 216)
		self.items["button"]["scores"] = TextButton("Highscores", 212, 330)
		self.items["button"]["credits"] = TextButton("Credits", 212, 444)
		self.items["button"]["exit"] = TextButton("Exit", 212, 558)
	def draw(self, window):
		window.blit(Assets.BACKGROUND, (0, 0))
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].draw(window)
	def update(self, events):
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].update(events)
	@staticmethod
	def screen_loop(window):
		screen = StartScreen()
		while True:
			events = pg.event.get()
			for event in events:
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit(0)
			if screen.items["button"]["play"].clicked:
				GameScreen.screen_loop(window)
			if screen.items["button"]["scores"].clicked:
				pass
			if screen.items["button"]["credits"].clicked:
				pass
			if screen.items["button"]["exit"].clicked:
				pg.quit()
				sys.exit(0)
			screen.draw(window)
			screen.update(events)
			pg.display.update()

class CreditsScreen:
	def __init__(self):
		self.items = {}
	def draw(self, window):
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].draw(window)
	def update(self, events):
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].update(events)
	@staticmethod
	def screen_loop(window):
		screen = CreditsScreen()
		while True:
			events = pg.event.get()
			for event in events:
				if event.type == pg.QUIT:
					pass
			screen.draw(window)
			screen.update(events)
			pg.display.update()

class HighscoreScreen:
	def __init__(self):
		self.items = {}
	def draw(self, window):
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].draw(window)
	def update(self, events):
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].update(events)
	@staticmethod
	def screen_loop(window):
		screen = HighscoreScreen()
		while True:
			events = pg.event.get()
			for event in events:
				if event.type == pg.QUIT:
					pass
			screen.draw(window)
			screen.update(events)
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
			screen.update(events)
			screen.draw(window)
			pg.display.update()

			if screen.game.lost():
				screen.game.snake.move()
				info = {"retry": True, "score": screen.game.score}
				RetryPopup.screen_loop(window, info)
				if not info["retry"]:
					break
				screen.game = Game(0, 0)

class RetryPopup:
	def __init__(self, score):
		self.items = {}
		self.items["button"] = {}
		self.items["button"]["menu"] = TextButton("Main Menu", 212, 298)
		self.items["button"]["retry"] = TextButton("Retry", 212, 382)
		self.items["button"]["exit"] = TextButton("Exit", 212, 466)
		self.text = pg.font.Font(Assets.BOXY_FONT, 48).render("Score: " + str(score), True, Colors.BLACK)

	def draw(self, window):
		window.blit(Assets.POPUP, (154, 154))
		window.blit(self.text, (352 - self.text.get_rect().centerx, 170))
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].draw(window)
	def update(self, events):
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].update(events)
	@staticmethod
	def screen_loop(window, information):
		screen = RetryPopup(information["score"])
		while True:
			events = pg.event.get()
			for event in events:
				if event.type == pg.QUIT:
					pg.quit()
					exit(0)
			if screen.items["button"]["exit"].clicked:
				pg.quit()
				exit(0)
			if screen.items["button"]["retry"].clicked:
				break
			if screen.items["button"]["menu"].clicked:
				information["retry"] = False
				break
			screen.draw(window)
			screen.update(events)
			pg.display.update()