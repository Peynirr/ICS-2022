import pygame
from pygame.locals import *
from pygame.color import THECOLORS

# Initializes Pygame and sets the window up
pygame.init()
screen = pygame.display.set_mode((1200, 750))

# Starting position, strokes and speed.
horizontalSpeed = 0
verticalSpeed = 0
xPos = 500
yPos = 500
strokes = 0
font = pygame.font.Font('BRLNSB.TTF', 30)
toNext = 0

# All the code, in while loop.
while toNext == 0:
    screen.fill((124, 252, 0))
    pygame.time.delay(10)

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
    if ((xPos - 100) ** 2 + (yPos - 100) ** 2) ** 0.5 < 25:
        horizontalSpeed *= 0.97
        verticalSpeed *= 0.97
        if abs(verticalSpeed) < 0.1 and abs(horizontalSpeed) < 0.1:
            toNext += 1

    # Par counter
    parCount = font.render(f'par = {strokes}', True, (THECOLORS["black"]), (24, 110, 47))
    screen.blit(parCount, (1070, 700))

    # Hole to get ball into
    pygame.draw.circle(screen, (255, 255, 255), (100, 100), 25)
    pygame.draw.circle(screen, (0, 0, 0), (100, 100), 24)

    # Slow down Sand
    sand = pygame.draw.rect(screen, (112, 176, 106), (234, 400, 123, 123))
    if sand.collidepoint(xPos, yPos):
        horizontalSpeed *= 0.8999
        verticalSpeed *= 0.8999

    # Water or Reset brick
    reset = pygame.draw.rect(screen, (54, 84, 217), (0, 200, 50, 300))
    if reset.collidepoint(xPos, yPos):
        xPos = 500
        yPos = 500
        horizontalSpeed = 0
        verticalSpeed = 0

    # Wall Script
    wall1 = pygame.draw.rect(screen, (THECOLORS['grey']), (345, 400, 50, 50))
    wall2 = pygame.draw.rect(screen, (THECOLORS['grey']), (400, 300, 10, 50))
    wall3 = pygame.draw.rect(screen, THECOLORS['grey']), (500, 300, 10, 50))
    wall4 = pygame.draw.rect(screen, (THECOLORS['grey']), (400, 300, 100, 10))
    if wall1.collidepoint(xPos, yPos):
        horizontalSpeed = -1 * abs(horizontalSpeed)
        verticalSpeed = -1 * abs(verticalSpeed)
    if wall2.collidepoint(xPos, yPos):
        horizontalSpeed = -1 * abs(horizontalSpeed)
        verticalSpeed = -1 * abs(verticalSpeed)
    if wall3.collidepoint(xPos, yPos):
        horizontalSpeed = -1 * abs(horizontalSpeed)
        verticalSpeed = -1 * abs(verticalSpeed)
    if wall4.collidepoint(xPos, yPos):
        horizontalSpeed = -1 * abs(horizontalSpeed)
        verticalSpeed = -1 * abs(verticalSpeed)

    # Slow down sand
    sand = pygame.draw.rect(screen, (212, 176, 106), (234, 345, 123, 123))
    if sand.collidepoint(xPos, yPos):
        horizontalSpeed *= 0.9
        verticalSpeed *= 0.9

    # Ball design, at the end because pygame is kind of stupid, and makes things that are the end appear on top.
    pygame.draw.circle(screen, (255, 255, 255), (round(xPos), round(yPos)), 15)
    pygame.display.update()

# Next Level script
if toNext == 1:
    import golf_Lvl2
