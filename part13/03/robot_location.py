# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

WIDTH, HEIGHT = 640, 480
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
robot = pygame.image.load("robot.png")

robot_height = robot.get_height()
robot_width = robot.get_width()
x = WIDTH // 2  - robot_width // 2	# start in the middle
y = HEIGHT // 2 - robot_height // 2
max_x = WIDTH - robot_width
max_y = HEIGHT - robot_height

window.fill(BLACK)
window.blit(robot, (x,y))
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.pos[0] >= x and event.pos[0] <= x + robot_width:	# inside x
				if event.pos[1] >= y and event.pos[1] <= y + robot_height: # inside y
					# generate new pos
					while event.pos[0] >= x and event.pos[0] <= x + robot_width:
						x = randint(0, max_x)
					while event.pos[1] >= y and event.pos[1] <= y + robot_height:
						y = randint(0, max_y)

			window.fill(BLACK)
			window.blit(robot, (x,y))
			pygame.display.flip()

		if event.type == pygame.QUIT:
			exit()
