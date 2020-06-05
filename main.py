import pygame as pg
from assets.assets import import_assets
from src.screens import StartScreen

WIN_W = 704
WIN_H = 704

def main():
	pg.init()
	window = pg.display.set_mode((WIN_W, WIN_H))
	import_assets()
	StartScreen.screen_loop(window)

if __name__ == "__main__":
	main()