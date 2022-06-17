import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import sys

# Initializes Pygame and sets the window up
pygame.init()
screen = pygame.display.set_mode((1200, 750))
backgroundImg = pygame.image.load('assets/golfBackground.png')
tarandeep = pygame.image.load("assets/tarandeep.png")
tarandeepSmall = pygame.transform.scale(tarandeep, (100, 100))

# Starting position, strokes and speed.
horizontalSpeed = 0
verticalSpeed = 0
xPos = 100
yPos = 700
strokes = 0
font = pygame.font.Font('assets/BRLNSB.TTF', 30)
toNext = 0

# All the code, in while loop.
while toNext == 0:
    screen.blit(backgroundImg, (0, 0))
    screen.blit(tarandeepSmall, (1020, 650))
    pygame.time.delay(0)

    # Hit the ball on click
    if abs(horizontalSpeed) < 0.1 and abs(verticalSpeed) < 0.1:
        pygame.draw.line(screen, (0, 165, 0), (xPos, yPos), pygame.mouse.get_pos())
    for event in pygame.event.get():
        if abs(horizontalSpeed) < 0.1 and abs(verticalSpeed) < 0.1:
            if event.type == pygame.MOUSEBUTTONUP:
                horizontalSpeed = -int((pygame.mouse.get_pos()[0] - xPos) / 20)
                verticalSpeed = -int((pygame.mouse.get_pos()[1] - yPos) / 20)
                strokes += 1
    xPos += horizontalSpeed
    yPos += verticalSpeed
    horizontalSpeed = horizontalSpeed * 0.98
    verticalSpeed = verticalSpeed * 0.98

    # Barriers
    if xPos > 1180 or xPos < 16:
        horizontalSpeed *= -1
    if yPos > 720 or yPos < 16:
        verticalSpeed *= -1

    # When in hole, go to next level
    if ((xPos - 650) ** 2 + (yPos - 650) ** 2) ** 0.5 < 25:
        horizontalSpeed *= 0.97
        verticalSpeed *= 0.97
        if abs(verticalSpeed) < 0.1 and abs(horizontalSpeed) < 0.1:
            toNext += 1

    # Par counter
    parCount = font.render(f'par = {strokes}', True, (THECOLORS["white"]), (24, 110, 47))
    screen.blit(parCount, (1070, 700))

    # Hole to get ball into
    pygame.draw.circle(screen, (255, 255, 255), (650, 650), 25)
    pygame.draw.circle(screen, (0, 0, 0), (650, 650), 24)

    # Wall Script (x, y, length, width)
    wall1 = pygame.draw.rect(screen, (THECOLORS['grey']), (150, 250, 50, 600))
    wall2 = pygame.draw.polygon(screen, (THECOLORS['grey']), [(1200, 0), (800, 0), (1200, 400)])

    if wall1.collidepoint(xPos, yPos):
        horizontalSpeed = -1 * abs(horizontalSpeed)
        verticalSpeed = -1 * abs(verticalSpeed)
    if wall2.collidepoint(xPos, yPos):
        horizontalSpeed = -1 * abs(horizontalSpeed)
        verticalSpeed = -1 * abs(verticalSpeed)

    # Ball design, at the end because pygame is kind of stupid, and makes things that are the end appear on top.
    pygame.draw.circle(screen, (255, 255, 255), (round(xPos), round(yPos)), 15)
    pygame.display.update()