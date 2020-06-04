import pygame as pg

class Colors:
	COLORKEY = (255, 0, 255)

class Assets:
	HEAD = None
	BODY = None
	FRUIT = None

def import_assets():
	def load_image(image_name, convert=True):
		if convert:
			image = pg.image.load("assets/" + image_name + ".png").convert()
		else:
			image = pg.image.load("assets/" + image_name + ".png")
		image.set_colorkey(Colors.COLORKEY)
		return image
	Assets.HEAD = load_image("head")
	Assets.BODY = load_image("body")
	Assets.FRUIT = load_image("fruit")