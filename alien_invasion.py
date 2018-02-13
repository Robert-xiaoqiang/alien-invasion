import sys
import pygame
from settings import Settings
from ship     import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button     import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
	ai_settings = Settings()
	ai_settings.initilize_dynamic_settings()

	pygame.init()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	
	ship = Ship(ai_settings, screen, 'ship.jpg')
	bullets = Group()
	aliens  = Group()
	stats = GameStats(ai_settings)
	play_button = Button(ai_settings, screen, 'Play')
	sb = Scoreboard(ai_settings, screen, stats)
	gf.create_aliens(ai_settings, screen, ship, aliens)

	while True:
		if stats.active:
			ship.update()

			#bullets.update() #polymorphism && list operation!
			gf.update_bullets(ai_settings, stats, screen, ship, bullets, aliens)

			gf.update_aliens(ai_settings, stats, screen, ship, bullets, aliens)
		gf.update_screen(ai_settings, stats, screen, ship, bullets, aliens, play_button, sb)		
		gf.check_events(ai_settings, stats, screen, ship, bullets, aliens, play_button)
		
run_game()