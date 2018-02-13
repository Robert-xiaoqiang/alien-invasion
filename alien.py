import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self, ai_settings, screen):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load('bee.jpg')
		self.rect  = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.x = float(self.rect.x)
	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		return self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left

	def update(self):
		self.x += self.ai_settings.alien_speed * self.ai_settings.alien_direction
		self.rect.x = self.x