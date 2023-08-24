# WRITE YOUR SOLUTION HERE:

import pygame, random

WIDTH, HEIGHT = 640, 480
BLACK = (0, 0, 0)
ROBOT_AMOUNT = 1000

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
robot = pygame.image.load("robot.png")

robot_width = robot.get_width()
robot_height = robot.get_height()
max_x = WIDTH - robot_width
max_y = HEIGHT - robot_height

window.fill((BLACK))
for i in range(ROBOT_AMOUNT):
	x = random.randint(0, max_x)
	y = random.randint(0, max_y)
	window.blit(robot, (x, y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
