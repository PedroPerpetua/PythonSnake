import pygame as pg
from assets.assets import import_assets
from src.snake import Snake
from src.screens import GameScreen

WIN_W = 700
WIN_H = 500

def main():
	pg.init()
	window = pg.display.set_mode((WIN_W, WIN_H))
	import_assets()
	GameScreen.screen_loop(window)
	
if __name__ == "__main__":
	main()