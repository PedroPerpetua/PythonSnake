import pygame as pg
import sys
from assets.assets import import_assets
from src.screens import StartScreen, GameScreen, States

WIN_W = 704
WIN_H = 704

def main():
	pg.init()
	window = pg.display.set_mode((WIN_W, WIN_H))
	import_assets()
	state = StartScreen.screen_loop(window)
	while state != States.EXIT:
		if state == States.MENU:
			state = StartScreen.screen_loop(window)
		if state == States.GAME:
			state = GameScreen.screen_loop(window)
	pg.quit()
	sys.exit(0)

if __name__ == "__main__":
	main()