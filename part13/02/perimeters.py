# # WRITE YOUR SOLUTION HERE:

import pygame

WIDTH, HEIGHT = 640, 480
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
robot = pygame.image.load("robot.png")

robot_height = robot.get_height()
robot_width = robot.get_width()
max_y = HEIGHT - robot_height
max_x = WIDTH - robot_width
x = 0
y = 0
vertical_speed = 1
horizontal_speed = 1
horizontal_move = True
vertical_move = False

clock = pygame.time.Clock()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	window.fill((BLACK))
	window.blit(robot, (x, y))
	pygame.display.flip()

	if vertical_move:
		y += vertical_speed
	if horizontal_move:
		x += horizontal_speed

	# top right / bottom left
	if horizontal_move and (x >= max_x or x <= 0):
		horizontal_move = False
		horizontal_speed *= -1
		vertical_move = True

	# top left / bottom right
	elif vertical_move and (y >= max_y or y <= 0):
		vertical_move = False
		vertical_speed *= -1
		horizontal_move = True

	clock.tick(60)
