# WRITE YOUR SOLUTION HERE:

import pygame

WIDTH, HEIGHT = 640, 480
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
robot = pygame.image.load("robot.png")

robot_height = robot.get_height()
robot_width = robot.get_width()
x1 = WIDTH // 4 * 3  - robot_width // 2
y1 = HEIGHT // 2 - robot_height // 2
x2 = WIDTH // 4  - robot_width // 2
y2 = HEIGHT // 2 - robot_height // 2
move_p1_up = False
move_p1_down = False
move_p1_right = False
move_p1_left = False
move_p2_up = False
move_p2_down = False
move_p2_right = False
move_p2_left = False
speed = 2
max_x = WIDTH - robot_width
max_y = HEIGHT - robot_height

clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				move_p1_left = True
			if event.key == pygame.K_UP:
				move_p1_up = True
			if event.key == pygame.K_RIGHT:
				move_p1_right = True
			if event.key == pygame.K_DOWN:
				move_p1_down = True
			if event.key == pygame.K_a:
				move_p2_left = True
			if event.key == pygame.K_w:
				move_p2_up = True
			if event.key == pygame.K_d:
				move_p2_right = True
			if event.key == pygame.K_s:
				move_p2_down = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				move_p1_left = False
			if event.key == pygame.K_UP:
				move_p1_up = False
			if event.key == pygame.K_RIGHT:
				move_p1_right = False
			if event.key == pygame.K_DOWN:
				move_p1_down = False
			if event.key == pygame.K_a:
				move_p2_left = False
			if event.key == pygame.K_w:
				move_p2_up = False
			if event.key == pygame.K_d:
				move_p2_right = False
			if event.key == pygame.K_s:
				move_p2_down = False

		if event.type == pygame.QUIT:
			exit()

	if move_p1_up and y1 >= speed:
		y1 -= speed
	if move_p1_down and y1 <= max_y:
		y1 += speed
	if move_p1_left and x1 >= speed:
		x1 -= speed
	if move_p1_right and x1 <= max_x:
		x1 += speed
	if move_p2_up and y2 >= speed:
		y2 -= speed
	if move_p2_down and y2 <= max_y:
		y2 += speed
	if move_p2_left and x2 >= speed:
		x2 -= speed
	if move_p2_right and x2 <= max_x:
		x2 += speed

	window.fill((BLACK))
	window.blit(robot, (x1,y1))
	window.blit(robot, (x2,y2))
	pygame.display.flip()

	clock.tick(60)
