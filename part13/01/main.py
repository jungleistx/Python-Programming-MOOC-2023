
# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

robot_width = robot.get_width()
robot_height = robot.get_height()
left_top = (0, 0)
right_top = (width - robot_width, 0)
left_bottom = (0, height - robot_height)
right_bottom = (width - robot_width, height - robot_height)

window.fill((0, 0, 0))
window.blit(robot, left_top)
window.blit(robot, right_top)
window.blit(robot, right_bottom)
window.blit(robot, left_bottom)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
