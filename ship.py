import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self, ai_settings, screen, jpg):
		super().__init__()
		self.screen = screen
		self.image  = pygame.image.load(jpg)
		self.rect   = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.move_right = False
		self.move_left  = False
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom  = self.screen_rect.bottom
		
		self.centerx = float(self.rect.centerx)  #self.centerx(float), self.rect.cebterx(int)

	def center_ship(self):
		self.centerx = float(self.screen_rect.centerx)

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.move_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.ship_speed
		if self.move_left and self.rect.left > self.screen_rect.left:
			self.centerx -= self.ai_settings.ship_speed
		self.rect.centerx = self.centerx