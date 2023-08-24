# WRITE YOUR SOLUTION HERE:

import pygame, random

WIDTH, HEIGHT = 640, 480
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
robot = pygame.image.load("robot.png")

robot_height = robot.get_height()
max_y = HEIGHT - robot_height
x = 0
y = 0
velocity = 1

clock = pygame.time.Clock()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	window.fill((BLACK))
	window.blit(robot, (x, y))
	pygame.display.flip()

	y += velocity
	if velocity > 0 and y >= max_y:
		velocity *= -1
	if velocity < 0 and y <= 0:
		velocity *= -1

	clock.tick(60)
