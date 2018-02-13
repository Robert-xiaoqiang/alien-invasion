class Settings():
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color      = (230, 230, 230)
		
		self.ship_limits   = 3

		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)

		self.alien_drop_speed = 8
		self.alien_direction = 1 # 1 right; -1 left

		self.speedup = 1.1

	def initilize_dynamic_settings(self):
		self.ship_speed    = 1.5
		self.bullet_speed = 1.2
		self.alien_speed = 1.1
		self.alien_points = 50

	def increase_speed(self):
		self.ship_speed *= self.speedup
		self.bullet_speed *= self.speedup
		self.alien_speed *= self.speedup
		self.alien_points *= self.speedup