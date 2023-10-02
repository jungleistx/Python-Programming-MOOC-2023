# WRITE YOUR SOLUTION HERE:

import pygame

WIDTH, HEIGHT = 640, 480
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
robot = pygame.image.load("robot.png")

x = WIDTH // 2  - robot.get_width() // 2	# start in the middle
y = HEIGHT // 2 - robot.get_height() // 2
move_up = False
move_down = False
move_right = False
move_left = False
speed = 2

clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				move_left = True
			if event.key == pygame.K_UP:
				move_up = True
			if event.key == pygame.K_RIGHT:
				move_right = True
			if event.key == pygame.K_DOWN:
				move_down = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				move_left = False
			if event.key == pygame.K_UP:
				move_up = False
			if event.key == pygame.K_RIGHT:
				move_right = False
			if event.key == pygame.K_DOWN:
				move_down = False

		if event.type == pygame.QUIT:
			exit()

	if move_up:
		y -= speed
	if move_down:
		y += speed
	if move_left:
		x -= speed
	if move_right:
		x += speed

	window.fill((BLACK))
	window.blit(robot, (x,y))
	pygame.display.flip()

	clock.tick(60)
