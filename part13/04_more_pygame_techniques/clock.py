# WRITE YOUR SOLUTION HERE:

import pygame, math
from datetime import datetime


def calculate_angles(t: datetime) -> tuple:
	# 360 degrees / [60s / 60m / 12h] * timeunit - offset
	second_angle = math.radians(6 * t.second - 90)
	minute_angle = math.radians(6 * t.minute - 90)
	# every minute adds 0.5 degree to the hour
	hour_angle = math.radians(30 * t.hour + t.minute / 2 - 90)
	return (second_angle, minute_angle, hour_angle)


WIDTH, HEIGHT = 640, 480
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

t = datetime.now()
pygame.display.set_caption(f'{t.hour:02}:{t.minute:02}:{t.second:02}')

outer_circle_radius = int(min(WIDTH, HEIGHT) * 0.42)	# relative to screensize
inner_circle_radius = int(outer_circle_radius * 0.98)
center_radius = int(outer_circle_radius * 0.05)
centroid = (WIDTH // 2, HEIGHT // 2)		# middle point

# draw outer 'border' and clock center
window.fill(BLACK)
pygame.draw.circle(window, WHITE, centroid, outer_circle_radius)
pygame.draw.circle(window, BLACK, centroid, inner_circle_radius)
pygame.draw.circle(window, WHITE, centroid, center_radius)
pygame.display.flip()

second_width = 1
minute_width = 2
hour_width = 5
second_length = int(outer_circle_radius * 0.90)
minute_length = second_length
hour_length = int(outer_circle_radius * 0.65)
lengths = [second_length, minute_length, hour_length]
widths = [second_width, minute_width, hour_width]

clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	# reset center circles
	pygame.draw.circle(window, BLACK, centroid, inner_circle_radius)
	pygame.draw.circle(window, WHITE, centroid, center_radius)

	# update title to current time
	t = datetime.now()
	pygame.display.set_caption(f'{t.hour:02}:{t.minute:02}:{t.second:02}')

	angles = calculate_angles(t)

	# draw clockhands
	for i in range(3):
		x = centroid[0] + lengths[i] * math.cos(angles[i])
		y = centroid[1] + lengths[i] * math.sin(angles[i])
		pygame.draw.line(window, WHITE, centroid, (x, y), widths[i])

	pygame.display.flip()

	clock.tick(30)	# with fps 1 might be 1second offset-issue
