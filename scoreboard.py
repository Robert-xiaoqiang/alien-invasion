import pygame.font
from pygame.sprite import Group
from ship          import Ship

class Scoreboard():
	def __init__(self, ai_settings, screen, stats):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 30)

	def prep_score(self):# 200 * 50 ???
		self.image = self.font.render('Your Score: '+"{:,}".format(int(round(self.stats.score, -1))), True, 
			                          self.text_color, self.ai_settings.bg_color)

		self.rect = self.image.get_rect()
		self.rect.right = self.screen_rect.right - 100
		self.rect.top = self.screen_rect.top

	def prep_high_score(self):
		self.high_image = self.font.render('Highest Score: '+"{:,}".format(int(round(self.stats.high_score, -1))), True,
										   self.text_color, self.ai_settings.bg_color)
		self.high_rect = self.high_image.get_rect()
		self.high_rect.left = self.screen_rect.left + 30
		self.high_rect.top = self.screen_rect.top

	def prep_level(self):
		self.level_image = self.font.render('Level: ' + str(self.stats.level), True,
											self.text_color, self.ai_settings.bg_color)
		self.level_rect = self.level_image.get_rect()
		self.level_rect.centerx = self.screen_rect.centerx
		self.level_rect.top = self.screen_rect.top
	def prep_left_ships(self):
		self.ships = Group()
		for ship_index in range(0, self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen, 'ship_mini.jpg')
			ship.rect.x = self.screen_rect.centerx - ship.rect.width + 2 * ship_index * ship.rect.width
			ship.rect.y = self.level_rect.bottom + 10
			self.ships.add(ship)

	def show_score(self):
		self.screen.blit(self.image, self.rect)
		self.screen.blit(self.high_image, self.high_rect)
		self.screen.blit(self.level_image, self.level_rect)
		# self.ships.draw(self.screen)
		for ship in self.ships.sprites():
			ship.blitme() 