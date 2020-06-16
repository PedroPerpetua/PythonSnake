import pygame as pg
from os import startfile as open_link
from assets.assets import Assets, Colors
from src.text_button import TextButton
from src.label import Label
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
		self.items["test"] = {}
	def draw(self, window):
		window.blit(Assets.BACKGROUND, (0, 0))
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].draw(window)
		window.blit(Assets.TITLE, (108, 100))
	def update(self, events):
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].update(events)
	@staticmethod
	def screen_loop(window, highscore_handler):
		screen = StartScreen()
		while True:
			events = pg.event.get()
			for event in events:
				if event.type == pg.QUIT:
					return States.EXIT
			if screen.items["button"]["play"].clicked:
				return States.GAME
			if screen.items["button"]["scores"].clicked:
				HighscoresPopup.popup_loop(window, highscore_handler)
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
	def screen_loop(window, highscore_handler):
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
				highscore_handler.add_highscore(SCORE)
				return RetryPopup.popup_loop(window)
			screen.update(events)
			screen.draw(window)
			pg.display.update()

# Menu popus
class CreditsPopup:
	def __init__(self):
		self.items = {}
		self.items["button"] = {}
		self.items["labels"] = {}
		self.items["button"]["github"] = TextButton("Github Repo", 212, 382)
		self.items["button"]["return"] = TextButton("Return", 212, 466)
		self.items["labels"]["label1"] = Label("Made by", 32, 261, 231)
		self.items["labels"]["label2"] = Label("Pedro Perpetua", 32, 172, 268)
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
			if screen.items["button"]["github"].clicked:
				open_link("https://github.com/PedroPerpetua/PythonSnake")
			if screen.items["button"]["return"].clicked:
				return States.RETURN
			screen.draw(window)
			screen.update(events)
			pg.display.update()

class HighscoresPopup:
	def __init__(self, highscore_handler):
		self.items = {}
		self.items["button"] = {}
		self.items["days"] = {}
		self.items["times"] = {}
		self.items["points"] = {}
		scores = highscore_handler.get_top_scores()
		self.items["days"]["1st"] = Label(scores[0]["day"], 24, 210, 205)
		self.items["times"]["1st"] = Label(scores[0]["time"], 24, 210, 237)
		self.items["points"]["1st"] = Label(scores[0]["points"], 38, 426, 214)
		self.items["days"]["2nd"] = Label(scores[1]["day"], 24, 210, 285)
		self.items["times"]["2nd"] = Label(scores[1]["time"], 24, 210, 317)
		self.items["points"]["2nd"] = Label(scores[1]["points"], 38, 426, 294)
		self.items["days"]["3rd"] = Label(scores[2]["day"], 24, 210, 365)
		self.items["times"]["3rd"] = Label(scores[2]["time"], 24, 210, 397)
		self.items["points"]["3rd"] = Label(scores[2]["points"], 38, 426, 374)
		self.items["button"]["return"] = TextButton("Return", 212, 466)
	def draw(self, window):
		window.blit(Assets.SCOREBOARD, (154, 154))
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].draw(window)
	def update(self, events):
		for item_type in self.items:
			for item in self.items[item_type]:
				self.items[item_type][item].update(events)
	@staticmethod
	def popup_loop(window, highscore_handler):
		screen = HighscoresPopup(highscore_handler)
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