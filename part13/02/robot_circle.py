# WRITE YOUR SOLUTION HERE:

import pygame, math

WIDTH, HEIGHT = 640, 480
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
robot = pygame.image.load("robot.png")

robot_height = robot.get_height()
robot_width = robot.get_width()
angle = 0
robots = 10

clock = pygame.time.Clock()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	window.fill((BLACK))
	for i in range(robots):
		x = WIDTH/2 + math.cos(angle + 2 * math.pi * i / robots) * 135 - robot_width / 2
		y = HEIGHT/2 + math.sin(angle + 2 * math.pi * i / robots) * 135 - robot_height / 2
		window.blit(robot, (x, y))

	pygame.display.flip()
	angle += 0.01
	clock.tick(60)
