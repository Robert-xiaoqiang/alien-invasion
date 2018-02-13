import sys
import pygame
from bullet import Bullet
from alien  import Alien
from time import sleep

def check_events(ai_settings, stats, screen, ship, bullets, aliens, play_button):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, stats, screen, ship, bullets, aliens,
				              play_button, mouse_x, mouse_y)
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.move_right = True
			elif event.key == pygame.K_LEFT:
				ship.move_left  = True
			elif event.key == pygame.K_SPACE:
				bullets.add(Bullet(ai_settings, screen, ship))
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.move_right = False
			elif event.key == pygame.K_LEFT:
				ship.move_left = False

def check_play_button(ai_settings, stats, screen, ship, bullets, aliens,
	                  play_button, mouse_x, mouse_y):
	if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.active:
		ai_settings.initilize_dynamic_settings()
		stats.reset()	
		stats.active = True
		pygame.mouse.set_visible(False)
		aliens.empty()
		bullets.empty()
		create_aliens(ai_settings, screen, ship, aliens)
		ship.center_ship()

def update_screen(ai_settings, stats, screen, ship, bullets, aliens, play_button, sb):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	sb.prep_score() # generate a new score pic(for restart bug)
	sb.prep_high_score()
	sb.prep_level()
	sb.prep_left_ships()
	sb.show_score()
	# bullets.draw_bullet()
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	for alien in aliens.sprites():
		alien.blitme()
	if not stats.active:
		play_button.draw_button()
	pygame.display.flip()

def check_ship_alien_collision(ai_settings, stats, screen, ship, bullets, aliens):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():
			stats.score += len(aliens) * ai_settings.alien_points
		    #sb.prep_score()
		if stats.score > stats.high_score:
			stats.high_score = stats.score
		# print('high_score' + str(stats.high_score))
	if len(aliens) == 0:
		bullets.empty()
		create_aliens(ai_settings, screen, ship, aliens)
		ai_settings.increase_speed()
		stats.level += 1

def update_bullets(ai_settings, stats, screen, ship, bullets, aliens):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_ship_alien_collision(ai_settings, stats, screen, ship, bullets, aliens)

def get_aliens_sum(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	return int(available_space_x / (2 * alien_width))

def get_aliens_row(ai_settings, ship_height, alien_height):
	available = ai_settings.screen_height - 3 * alien_height -  2 * ship_height - 50
	return int(available / (2 * alien_height))

def create_alien(ai_settings, screen, aliens, alien_index, row_index): # create only one
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_index
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_index
	aliens.add(alien)

def create_aliens(ai_settings, screen, ship, aliens): # create lines
	sum_of_aliens = get_aliens_sum(ai_settings, Alien(ai_settings, screen).rect.width)
	row_of_aliens = get_aliens_row(ai_settings, ship.rect.height, Alien(ai_settings, screen).rect.height)
	for row_index in range(1, row_of_aliens):
		for alien_index in range(0, sum_of_aliens):
			create_alien(ai_settings, screen, aliens, alien_index, row_index)

def update_aliens(ai_settings, stats, screen, ship, bullets, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			for alien_ in aliens.sprites():
				alien_.rect.y += ai_settings.alien_drop_speed
			ai_settings.alien_direction *= -1
			break
	aliens.update() # polymorphism && list operation
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, bullets, aliens)
	check_aliens_bottom(ai_settings, stats, screen, ship, bullets, aliens)

def ship_hit(ai_settings, stats, screen, ship, bullets, aliens):
	if stats.ships_left > 0:
		stats.ships_left -= 1
		aliens.empty()
		bullets.empty()

		create_aliens(ai_settings, screen, ship, aliens)
		ship.center_ship()

		sleep(1.5)
	else:
		stats.active = False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, bullets, aliens):
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen.get_rect().bottom:
			ship_hit(ai_settings, stats, screen, ship, bullets, aliens)
			break