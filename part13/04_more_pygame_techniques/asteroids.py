# WRITE YOUR SOLUTION HERE:

import pygame, time
from random import randint

WIDTH, HEIGHT = 400, 480
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f'Asteroids')

robot = pygame.image.load('robot.png')
rock = pygame.image.load('rock.png')
robot_height = robot.get_height()
robot_width = robot.get_width()
rock_height = rock.get_height()
rock_width = rock.get_width()

def create_rock(amount:int, r_width, r_height, WIDTH) -> list:
	rocks = []
	for i in range(amount):
		rock = {}
		rock_x = randint(0, WIDTH - r_width)
		rock_y = -randint(r_height * 2, r_height * 8)
		if amount > 1 and i > 0:
			rock_y += rocks[i - 1]['y']
		rock['x'] = rock_x
		rock['y'] = rock_y
		rocks.append(rock)
	return rocks

rock_amount = 3
rocks = create_rock(rock_amount, rock_width, rock_height, WIDTH)
points = 0
robot_speed = 5
x_robot = WIDTH // 2 - robot_width // 2
y_robot = HEIGHT - robot_height
max_x = WIDTH - robot_width
robot_move_left = False
robot_move_right = False

clock = pygame.time.Clock()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

		# check if keys pressed
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				robot_move_left = True
			if event.key == pygame.K_RIGHT:
				robot_move_right = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				robot_move_left = False
			if event.key == pygame.K_RIGHT:
				robot_move_right = False

	window.fill(BLACK)

	# move robot
	if robot_move_left:
		x_robot -= robot_speed
	if robot_move_right:
		x_robot += robot_speed

	# portal robot from sides
	if x_robot > WIDTH:
		x_robot -= WIDTH + robot_width
	elif x_robot < 0 - robot_width:
		x_robot += WIDTH + robot_width

	# set rock_speed relative to points, robot_speed relative to rock
	rock_speed = points // 2 + 1
	robot_speed = int(rock_speed * 1.5)
	if robot_speed < 5:
		robot_speed = 5

	# move rocks
	for i in range(rock_amount):
		rocks[i]['y'] += rock_speed
		window.blit(rock, (rocks[i]['x'], rocks[i]['y']))

	# draw scoreboard
	score_font = pygame.font.SysFont(None, 24)
	score_text = score_font.render(f"Points: {points:3}", True, RED)
	score_text_rect = score_text.get_rect(topright=(WIDTH - 20, 10))
	window.blit(score_text, score_text_rect)

	# rocks hit robot
	robot_rect = robot.get_rect()
	robot_rect.topleft = (x_robot, y_robot)
	rock_rect = rock.get_rect()
	for i in range(rock_amount):
		rock_rect.topleft = (rocks[i]['x'], rocks[i]['y'])
		# check for collision
		if robot_rect.colliderect(rock_rect):
			# create and join new rock to the list
			del rocks[i]
			new_rock = create_rock(1, rock_width, rock_height, WIDTH)
			rocks.extend(new_rock)
			points += 1

	# rocks hit floor == game over
	for i in range(len(rocks)):
		if rocks[i]['y'] >= HEIGHT - rock_height:
			mid_x = WIDTH // 2
			mid_y = HEIGHT // 2
			game_font = pygame.font.SysFont(None, 24)
			text = game_font.render("GAME OVER!", True, RED)
			text_rect = text.get_rect(center=(mid_x, mid_y))
			window.blit(text, text_rect)
			pygame.display.flip()
			running = False

	window.blit(robot, (x_robot, y_robot))
	pygame.display.flip()
	clock.tick(60)

# endgame loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
