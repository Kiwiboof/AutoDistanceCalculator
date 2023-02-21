import sys
import pygame
from constants import *

clock = pygame.time.Clock()

pygame.display.set_caption('Auto Calculator')

screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y), 0, 32)

field = pygame.image.load('field.png')
field = pygame.transform.scale(field, (field.get_width() * MULTIPLIER, field.get_height() * MULTIPLIER))


counter = 0
position1 = 0
position2 = 0
distance = 0
product = 0

robot_pos = (0, 0)

while True:

    robot = pygame.Rect(robot_pos[0] - (WIDTH / 2), robot_pos[1] - (HEIGHT / 2), WIDTH, HEIGHT)
    screen.fill((0, 0, 0))

    screen.blit(field, (0, 0))

    pygame.draw.rect(screen, (0, 0, 255), robot)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            robot_pos = pygame.mouse.get_pos()
            # print(robot_pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if counter == 0:
                position1 = pygame.mouse.get_pos()[0]
                counter += 1
            elif counter == 1:
                position2 = (pygame.mouse.get_pos()[0])
                counter = 0
                distance = abs(position1 - position2)
                product = (distance / (MODULE_IPS * SPEED_PERCENTAGE)) / MULTIPLIER
                print(f"{product} Seconds")

    pygame.display.update()
    clock.tick(60)
