import pygame as pg
from assets.assets import Assets, Colors
from src.text_button import TextButton
from src.game import Game

SCORE = -1
class States:
	EXIT = -1
	RETURN = 0
	MENU = 1
	GAME = 2

# Main screens
class StartScreen:
	def __init__(self):
		self.items = {}
		self.items["button"] = {}
		self.items["button"]["play"] = TextButton("Play!", 212, 306)
		self.items["button"]["scores"] = TextButton("Highscores", 212, 390)
		self.items["button"]["credits"] = TextButton("Credits", 212, 474)
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
					return States.EXIT
			if screen.items["button"]["play"].clicked:
				return States.GAME
			if screen.items["button"]["scores"].clicked:
				HighscoresPopup.popup_loop(window)
			if screen.items["button"]["credits"].clicked:
				CreditsPopup.popup_loop(window)
			if screen.items["button"]["exit"].clicked:
				return States.EXIT
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
		global SCORE
		screen = GameScreen()
		while True:
			events = pg.event.get()
			for event in events:
				if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
					option = PausePopup.popup_loop(window)
					if option != States.RETURN:
						return option
			if screen.game.lost():
				screen.game.snake.move()
				SCORE = screen.game.score
				return RetryPopup.popup_loop(window)
			screen.update(events)
			screen.draw(window)
			pg.display.update()

# Menu popus
class CreditsPopup:
	def __init__(self):
		self.items = {}
		self.items["button"] = {}
		self.items["button"]["return"] = TextButton("Return", 212, 466)
	def draw(self, window):
		window.blit(Assets.POPUP, (154, 154))
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].draw(window)
	def update(self, events):
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].update(events)
	@staticmethod
	def popup_loop(window):
		screen = CreditsPopup()
		while True:
			events = pg.event.get()
			for event in events:
				if event.type == pg.QUIT:
					return States.EXIT
				if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
					return States.RETURN
			if screen.items["button"]["return"].clicked:
				return States.RETURN
			screen.draw(window)
			screen.update(events)
			pg.display.update()

class HighscoresPopup:
	def __init__(self):
		self.items = {}
		self.items["button"] = {}
		self.items["button"]["return"] = TextButton("Return", 212, 466)
	def draw(self, window):
		window.blit(Assets.POPUP, (154, 154))
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].draw(window)
	def update(self, events):
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].update(events)
	@staticmethod
	def popup_loop(window):
		screen = HighscoresPopup()
		while True:
			events = pg.event.get()
			for event in events:
				if event.type == pg.QUIT:
					return States.EXIT
				if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
					return States.RETURN
			if screen.items["button"]["return"].clicked:
				return States.RETURN
			screen.draw(window)
			screen.update(events)
			pg.display.update()

# In game popups
class PausePopup:
	def __init__(self):
		self.items = {}
		self.items["button"] = {}
		self.items["button"]["resume"] = TextButton("Resume", 212, 214)
		self.items["button"]["menu"] = TextButton("Main Menu", 212, 298)
		self.items["button"]["restart"] = TextButton("Restart", 212, 382)
		self.items["button"]["exit"] = TextButton("Exit", 212, 466)
	def draw(self, window):
		window.blit(Assets.POPUP, (154, 154))
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].draw(window)
	def update(self, events):
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].update(events)
	@staticmethod
	def popup_loop(window):
		screen = PausePopup()
		while True:
			events = pg.event.get()
			for event in events:
				if event.type == pg.QUIT:
					return States.EXIT
				if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
					return States.RETURN
			if screen.items["button"]["exit"].clicked:
				return States.EXIT
			if screen.items["button"]["resume"].clicked:
				return States.RETURN
			if screen.items["button"]["restart"].clicked:
				return States.GAME
			if screen.items["button"]["menu"].clicked:
				return States.MENU
			screen.draw(window)
			screen.update(events)
			pg.display.update()

class RetryPopup:
	def __init__(self):
		global SCORE
		self.items = {}
		self.items["button"] = {}
		self.items["button"]["menu"] = TextButton("Main Menu", 212, 298)
		self.items["button"]["retry"] = TextButton("Retry", 212, 382)
		self.items["button"]["exit"] = TextButton("Exit", 212, 466)
		self.text = pg.font.Font(Assets.BOXY_FONT, 48).render("Score: " + str(SCORE), True, Colors.BLACK)
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
	def popup_loop(window):
		screen = RetryPopup()
		while True:
			events = pg.event.get()
			for event in events:
				if event.type == pg.QUIT:
					return States.EXIT
			if screen.items["button"]["exit"].clicked:
				return States.EXIT
			if screen.items["button"]["retry"].clicked:
				return States.GAME
			if screen.items["button"]["menu"].clicked:
				return States.MENU
			screen.draw(window)
			screen.update(events)
			pg.display.update()