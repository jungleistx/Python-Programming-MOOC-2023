# WRITE YOUR SOLUTION HERE:

import pygame

WIDTH, HEIGHT = 640, 480
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
robot_a = pygame.image.load("robot.png")
robot_b = pygame.image.load("robot.png")

robot_height = robot_a.get_height()
robot_width = robot_a.get_width()
max_y = HEIGHT - robot_height
max_x = WIDTH - robot_width
a_y = HEIGHT / 10
a_x = 0
b_y = a_y + (robot_height * 1.2)
b_x = 0
a_speed = 1
b_speed = 2

clock = pygame.time.Clock()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	window.fill((BLACK))
	window.blit(robot_a, (a_x, a_y))
	window.blit(robot_b, (b_x, b_y))
	pygame.display.flip()

	a_x += a_speed
	b_x += b_speed

	if a_x == 0 or a_x == max_x:
		a_speed *= -1
	if b_x == 0 or b_x == max_x:
		b_speed *= -1

	clock.tick(60)
