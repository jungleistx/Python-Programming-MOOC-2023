# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

robot_width = robot.get_width()
robot_height = robot.get_height()
start_x = robot_width
start_y = robot_height

window.fill((0, 0, 0))
for i in range(10):
	x = start_x + (width / 80) * i
	for j in range(10):
		window.blit(robot, (x, start_y))
		x += (robot_width * 0.8)
	start_y += (robot_height / 5)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
