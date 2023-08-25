# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

def create_robot(max_x, robot_width, robot_height):
	starting_x = randint(0, max_x)
	# random height from the top
	starting_y = -randint(robot_height, robot_height * 5)

	# right from middle point
	if starting_x >= max_x / 2 - robot_width / 2:
		floor_direction = 1
	# to the left
	else:
		floor_direction = -1

	return {
		'x': starting_x,
		'y': starting_y,
		'fall': True,
		'direction': floor_direction
	}


WIDTH, HEIGHT = 640, 480
BLACK = (0, 0, 0)
ROBOTS = 10

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
robot = pygame.image.load("robot.png")

robot_height = robot.get_height()
robot_width = robot.get_width()
max_x = WIDTH - robot_width
max_y = HEIGHT - robot_height
edge_left = 0 - robot_width
edge_right = WIDTH + robot_width

robot_list = []
while len(robot_list) < ROBOTS:
	robot_list.append(create_robot(max_x, robot_width, robot_height))

clock = pygame.time.Clock()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	window.fill((BLACK))
	for i in range(ROBOTS):
		window.blit(robot, (robot_list[i]['x'], robot_list[i]['y']))

		# move robots
		if robot_list[i]['fall']:
			robot_list[i]['y'] += 1
		else:
			robot_list[i]['x'] += robot_list[i]['direction']

	pygame.display.flip()

	for i in range(ROBOTS):
		# check if touches bottom
		if robot_list[i]['fall']:
			if robot_list[i]['y'] == max_y:
				robot_list[i]['fall'] = False
		# check if beyond edge
		elif robot_list[i]['x'] <= edge_left or robot_list[i]['x'] >= edge_right:
			robot_list[i] = create_robot(max_x, robot_width, robot_height)

	clock.tick(60)
