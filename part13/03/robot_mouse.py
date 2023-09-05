# WRITE YOUR SOLUTION HERE:


import pygame

WIDTH, HEIGHT = 640, 480
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
robot = pygame.image.load("robot.png")

half_robot_height = robot.get_height() // 2
half_robot_width = robot.get_width() // 2

while True:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEMOTION:
			x = event.pos[0] - half_robot_width
			y = event.pos[1] - half_robot_height

			window.fill(BLACK)
			window.blit(robot, (x,y))
			pygame.display.flip()

		if event.type == pygame.QUIT:
			exit()
