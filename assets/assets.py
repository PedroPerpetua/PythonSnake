import pygame as pg
import os

class Colors:
	COLORKEY = (255, 0, 255)
	BLACK = (0, 0, 0)

class Assets:
	TITLE = None
	SNAKE_HEAD = None
	SNAKE_BODY = None
	FRUIT_NORMAL = None
	FRUIT_GOLDEN = None
	BACKGROUND = None
	BOXY_FONT = None
	BUTTON_DEFAULT = None
	BUTTON_HOVERED = None
	POPUP = None
	SCOREBOARD = None
def import_assets():
	def load_image(image_name, convert=True):
		if convert:
			image = pg.image.load("assets/" + image_name + ".png").convert()
		else:
			image = pg.image.load("assets/" + image_name + ".png")
		image.set_colorkey(Colors.COLORKEY)
		return image
	def load_font(font_name):
		if not os.path.isfile("assets/" + font_name + ".ttf"):
			font = pg.font.match_font(font_name)
		else:
			font = "assets/" + font_name + ".ttf"
		return font
	Assets.TITLE = load_image("title")
	Assets.SNAKE_HEAD = load_image("snake_head")
	Assets.SNAKE_BODY = load_image("snake_body")
	Assets.FRUIT_NORMAL = load_image("fruit_normal")
	Assets.FRUIT_GOLDEN = load_image("fruit_golden")
	Assets.BACKGROUND = load_image("background")
	Assets.BOXY_FONT = load_font("boxy_bold")
	Assets.BUTTON_DEFAULT = load_image("button_default")
	Assets.BUTTON_HOVERED = load_image("button_hovered")
	Assets.POPUP = load_image("popup")
	Assets.SCOREBOARD = load_image("scoreboard")