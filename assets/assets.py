import pygame as pg
import os

class Colors:
	COLORKEY = (255, 0, 255)
	BLACK = (0, 0, 0)

class Assets:
	HEAD = None
	BODY = None
	FRUIT = None
	GOLDEN = None
	BACKGROUND = None
	BOXY_FONT = None
	BUTTON_DEFAULT = None
	BUTTON_HOVERED = None
	POPUP = None
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
	Assets.HEAD = load_image("head")
	Assets.BODY = load_image("body")
	Assets.FRUIT = load_image("fruit")
	Assets.GOLDEN = load_image("golden")
	Assets.BACKGROUND = load_image("background")
	Assets.BOXY_FONT = load_font("boxy_bold")
	Assets.BUTTON_DEFAULT = load_image("button_default")
	Assets.BUTTON_HOVERED = load_image("button_hovered")
	Assets.POPUP = load_image("popup")