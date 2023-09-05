# WRITE YOUR SOLUTION HERE:

import pygame

WIDTH, HEIGHT = 640, 480
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
robot = pygame.image.load("robot.png")

robot_height = robot.get_height()
robot_width = robot.get_width()
x = WIDTH // 2  - robot_width // 2	# start in the middle
y = HEIGHT // 2 - robot_height // 2
move_up = False
move_down = False
move_right = False
move_left = False
speed = 2
max_x = WIDTH - robot_width
max_y = HEIGHT - robot_height

clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				move_left = True
			if event.key == pygame.K_UP:
				move_up = True
			if event.key == pygame.K_RIGHT:
				move_right = True
			if event.key == pygame.K_DOWN:
				move_down = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				move_left = False
			if event.key == pygame.K_UP:
				move_up = False
			if event.key == pygame.K_RIGHT:
				move_right = False
			if event.key == pygame.K_DOWN:
				move_down = False

		if event.type == pygame.QUIT:
			exit()

	if move_up and y >= speed:
		y -= speed
	if move_down and y <= max_y:
		y += speed
	if move_left and x >= speed:
		x -= speed
	if move_right and x <= max_x:
		x += speed

	window.fill((BLACK))
	window.blit(robot, (x,y))
	pygame.display.flip()

	clock.tick(60)
