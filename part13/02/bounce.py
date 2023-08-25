# WRITE YOUR SOLUTION HERE:

import pygame

WIDTH, HEIGHT = 640, 480
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
ball = pygame.image.load("ball.png")

ball_height = ball.get_height()
ball_width = ball.get_width()
max_x = WIDTH - ball_width
max_y = HEIGHT - ball_height
x = 0
y = 0
horizontal_move = 2
vertical_move = 2

clock = pygame.time.Clock()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	window.fill((BLACK))
	window.blit(ball, (x, y))
	pygame.display.flip()

	x += horizontal_move
	y += vertical_move
	if x == 0 or x == max_x:
		horizontal_move *= -1
	if y == 0 or y == max_y:
		vertical_move *= -1

	clock.tick(60)
