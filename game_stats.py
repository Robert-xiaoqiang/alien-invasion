class GameStats():
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset()
		self.high_score = 0
	def reset(self):
		self.ships_left = self.ai_settings.ship_limits
		self.active = False
		self.score = 0
		self.level = 1