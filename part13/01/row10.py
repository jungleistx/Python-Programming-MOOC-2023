# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

robot_width = robot.get_width()
robot_height = robot.get_height()
start_x = (width - (10 * robot_width)) / 2
start_y = (height - robot_height) / 2

window.fill((0, 0, 0))
for i in range(10):
	window.blit(robot, (start_x, start_y))
	start_x += robot_width
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
