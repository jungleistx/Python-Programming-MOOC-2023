# Complete your game here

import pygame
from random import randint

class Graveyard():
	WIDTH = 480
	HEIGHT = 480
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	GRAY = (75, 75, 75)

	def __init__(self):
		pygame.init()
		pygame.display.set_caption(f'Graveyard')
		self.game_font = pygame.font.SysFont(None, 24)
		self.hiscore = 0
		self.x_mid = Graveyard.WIDTH // 2
		self.y_mid = Graveyard.HEIGHT // 2
		self.load_images()
		self.init_jump()
		self.start_game()

	def starting_guide(self):
		start_text1 = self.game_font.render('Welcome!', True, Graveyard.RED)
		start_text2 = self.game_font.render('Collect coins, avoid ghosts.', True, Graveyard.RED)
		start_text3 = self.game_font.render('Move with <- and ->, jump with SPACE', True, Graveyard.RED)
		start_text4 = self.game_font.render('Press SPACE to start!', True, Graveyard.RED)
		rect1 = start_text1.get_rect(center=(self.x_mid, self.y_mid - 30))
		rect2 = start_text2.get_rect(center=(self.x_mid, self.y_mid - 10))
		rect3 = start_text3.get_rect(center=(self.x_mid, self.y_mid + 10))
		rect4 = start_text4.get_rect(center=(self.x_mid, self.y_mid + 30))
		self.window.fill(Graveyard.GRAY)
		self.show_points()
		self.window.blit(start_text1, rect1)
		self.window.blit(start_text2, rect2)
		self.window.blit(start_text3, rect3)
		self.window.blit(start_text4, rect4)
		pygame.display.flip()
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.new_game()

	def create_monster(self, amount:int):
		monsters = []
		for i in range(amount):
			monster = {}
			monster_x = randint(0, Graveyard.WIDTH - self.monster_width)
			monster_y = -randint(self.monster_height * 2, self.monster_height * 10)
			monster['x'] = monster_x
			monster['y'] = monster_y
			monster['speed'] = randint(1, self.robot_speed)
			monsters.append(monster)
		return monsters

	def create_coin(self, amount:int):
		coins = []
		for i in range(amount):
			coin = {}
			coin_x = randint(0, Graveyard.WIDTH - self.coin_width)
			coin_y = -randint(self.coin_height * 2, self.coin_height * 10)
			coin['x'] = coin_x
			coin['y'] = coin_y
			coins.append(coin)
		return coins

	def game_over(self):
		self.show_points()
		game_over_text1 = self.game_font.render("GAME OVER!", True, Graveyard.RED)
		game_over_text2 = self.game_font.render("ESC to quit", True, Graveyard.RED)
		game_over_text3 = self.game_font.render("SPACE to play again", True, Graveyard.RED)
		game_over_rect1 = game_over_text1.get_rect(center=(self.x_mid, self.y_mid - 20))
		game_over_rect2 = game_over_text2.get_rect(center=(self.x_mid, self.y_mid))
		game_over_rect3 = game_over_text3.get_rect(center=(self.x_mid, self.y_mid + 20))

		self.window.blit(game_over_text1, game_over_rect1)
		self.window.blit(game_over_text2, game_over_rect2)
		self.window.blit(game_over_text3, game_over_rect3)
		pygame.display.flip()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.new_game()
					if event.key == pygame.K_ESCAPE:
						exit()

	def load_images(self):
		self.robot = pygame.image.load('robot.png')
		self.robot_height = self.robot.get_height()
		self.robot_width = self.robot.get_width()
		self.monster = pygame.image.load('monster.png')
		self.monster_height = self.monster.get_height()
		self.monster_width = self.monster.get_width()
		self.coin = pygame.image.load('coin.png')
		self.coin_height = self.coin.get_height()
		self.coin_width = self.coin.get_width()

	def init_jump(self):
		self.jump_distance = int(self.robot_height * 0.7)
		self.robot_floor = Graveyard.HEIGHT - self.robot_height
		self.jump_height_max = self.robot_floor - self.jump_distance
		self.hover_amount = 3
		self.jump_speed = 3
		self.hover_state = False
		self.jump_down_state = False
		self.jump_up = False

	def main_loop(self):
		clock = pygame.time.Clock()
		while True:
			self.event_handler()
			self.draw_window()
			self.draw_arrows()
			self.move_coins()
			self.move_monsters()
			self.show_points()
			if self.robot_jump:
				self.jump_handler()
			pygame.display.flip()
			clock.tick(60)

	def add_monster(self):
		new_monster = self.create_monster(1)
		self.monsters.extend(new_monster)
		self.monster_amount += 1
		if self.monster_amount % 3 == 0:
			self.add_coin()

	def add_coin(self):
		new_coins = self.create_coin(2)
		self.coins.extend(new_coins)
		self.coin_amount += 2

	def move_monsters(self):
		for i in range(self.monster_amount):
			self.monsters[i]['y'] += self.monsters[i]['speed']
			self.monster_hit()
			if self.monsters[i]['y'] >= Graveyard.HEIGHT:
				del self.monsters[i]
				new_monster = self.create_monster(1)
				self.monsters.extend(new_monster)
			self.window.blit(self.monster, (self.monsters[i]['x'], self.monsters[i]['y']))

	def monster_hit(self):
		robot_rect = self.robot.get_rect()
		robot_rect.topleft = (self.robot_x, self.robot_y)
		monster_rect = self.monster.get_rect()
		for i in range(self.monster_amount):
			monster_rect.topleft = (self.monsters[i]['x'], self.monsters[i]['y'])
			if robot_rect.colliderect(monster_rect):
				self.game_over()

	def move_coins(self):
		for i in range(self.coin_amount):
			self.coins[i]['y'] += self.coin_speed
			self.check_coin_hit()
			self.check_coin_floor()
			self.window.blit(self.coin, (self.coins[i]['x'], self.coins[i]['y']))

	def check_coin_floor(self):
		for i in range(self.coin_amount):
			if self.coins[i]['y'] >= Graveyard.HEIGHT:
				del self.coins[i]
				new_coin = self.create_coin(1)
				self.coins.extend(new_coin)

	def check_coin_hit(self):
		robot_rect = self.robot.get_rect()
		robot_rect.topleft = (self.robot_x, self.robot_y)
		coin_rect = self.coin.get_rect()

		for i in range(self.coin_amount):
			coin_rect.topleft = (self.coins[i]['x'], self.coins[i]['y'])
			if robot_rect.colliderect(coin_rect):
				del self.coins[i]
				new_coin = self.create_coin(1)
				self.coins.extend(new_coin)
				self.points += 1

				# add monster every 3 point
				if self.points % 3 == 0:
					self.add_monster()

	def show_points(self):
		if self.hiscore < self.points:
			self.hiscore = self.points
		hiscore_text = self.game_font.render(f"HISCORE {self.hiscore:2}", True, Graveyard.RED)
		points_text = self.game_font.render(f"POINTS {self.points:3}", True, Graveyard.RED)
		hiscore_rect = hiscore_text.get_rect(topleft=(10, 10))
		points_rect = hiscore_text.get_rect(topright=(Graveyard.WIDTH - 10, 10))
		self.window.blit(hiscore_text, hiscore_rect)
		self.window.blit(points_text, points_rect)

	def draw_arrows(self):
		arrow_left = self.game_font.render('<-', True, Graveyard.RED)
		arrow_right = self.game_font.render('->', True, Graveyard.RED)
		left_rect = arrow_left.get_rect(topleft=(10, Graveyard.HEIGHT - self.robot_height - 20))
		right_rect = arrow_right.get_rect(topright=(Graveyard.WIDTH - 10, Graveyard.HEIGHT - self.robot_height - 20))
		self.window.blit(arrow_left, left_rect)
		self.window.blit(arrow_right, right_rect)

	def new_game(self):
		self.robot_x = self.x_mid - self.robot_width // 2
		self.robot_y = Graveyard.HEIGHT - self.robot_height
		self.robot_move_left = False
		self.robot_move_right = False
		self.robot_jump = False
		self.robot_speed = 5
		self.coin_amount = 5
		self.points = 0
		self.monster_amount = 0
		self.coins = self.create_coin(self.coin_amount)
		self.coin_speed = 2
		self.monsters = []
		self.draw_arrows()
		self.main_loop()

	def start_game(self):
		self.window = pygame.display.set_mode((Graveyard.WIDTH, Graveyard.HEIGHT))
		self.points = 0
		self.starting_guide()

	def draw_window(self):
		self.window.fill(Graveyard.GRAY)
		self.window.blit(self.robot, (self.robot_x, self.robot_y))

	def event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.robot_move_left = True
				if event.key == pygame.K_RIGHT:
					self.robot_move_right = True
				if event.key == pygame.K_SPACE and not self.robot_jump:
					self.robot_jump = True
					self.jump_up = True
					self.jump_handler()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					self.robot_move_left = False
				if event.key == pygame.K_RIGHT:
					self.robot_move_right = False

		if self.robot_move_left or self.robot_move_right:
			self.move_robot()

	def hover(self):
		if self.hover_amount >= 0:
			self.hover_amount -= 1
		else:
			self.hover_amount = 3
			self.hover_state = False
			self.jump_down_state = True

	def jump_down(self):
		if self.robot_y < self.robot_floor:
			self.robot_y += self.jump_speed
		else:
			self.jump_down_state = False
			self.robot_jump = False

	def jump_handler(self):
		if self.jump_up:
			self.jump()
		elif self.hover_state:
			self.hover()
		elif self.jump_down_state:
			self.jump_down()

	def jump(self):
		if self.robot_y > self.jump_height_max:
			self.robot_y -= self.jump_speed
		else:
			self.jump_up = False
			self.hover_state = True

	def move_robot(self):
		if self.robot_move_right:
			self.robot_x += self.robot_speed
		if self.robot_move_left:
			self.robot_x -= self.robot_speed
		self.portal()

	def portal(self):
		if self.robot_x > Graveyard.WIDTH:
			self.robot_x -= Graveyard.WIDTH + self.robot_width
		elif self.robot_x < 0 - self.robot_width:
			self.robot_x += Graveyard.WIDTH + self.robot_width


if __name__ == "__main__":
	Graveyard()
