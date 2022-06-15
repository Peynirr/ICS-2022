import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import sys

# Generic importing.
# Initalizes Pygame and sets the window up
pygame.init()
screen = pygame.display.set_mode((1200, 750))
bgImg = pygame.image.load('assets/golfBackground.png')
tarandeep = pygame.image.load('assets/tarandeep.png')
tarandeepSmall = pygame.transform.scale(tarandeep, (175, 175))
font = pygame.font.Font('assets/BRLNSB.TTF', 30)

# Starting position, strokes and speed.
xSpeed = 0
ySpeed = 0
x = 120
y = 600
strokes = 0
toNext = 0

def level4(toNext, xSpeed, ySpeed, x, y, strokes):
    # Starting position, strokes and speed.
    xSpeed = 0
    ySpeed = 0
    x = 120
    y = 600
    strokes = 0
    toNext = 0

    while toNext == 0:
        screen.blit(bgImg, (0, 0))
        pygame.time.delay(10)

        # Hole to get ball into
        pygame.draw.circle(screen, (255, 255, 255), (925, 700), 25)
        pygame.draw.circle(screen, (0, 0, 0), (925, 700), 24)

        # Hit the ball on click
        if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
            pygame.draw.line(screen, (0, 165, 0), (x, y), pygame.mouse.get_pos())
        for event in pygame.event.get():
            if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
                if event.type == pygame.MOUSEBUTTONUP:
                    xSpeed = -int((pygame.mouse.get_pos()[0] - x) / 20)
                    ySpeed = -int((pygame.mouse.get_pos()[1] - y) / 20)
                    strokes += 1
        x += xSpeed
        y += ySpeed
        xSpeed = xSpeed * 0.98
        ySpeed = ySpeed * 0.98

        # Drawing sand
        sand1 = pygame.draw.rect(screen, (212, 176, 106), (100, 100, 123, 123))
        sand2 = pygame.draw.rect(screen, (212, 176, 106), (150, 150, 123, 123))
        sand3 = pygame.draw.rect(screen, (212, 176, 106), (200, 200, 123, 123))
        sand4 = pygame.draw.rect(screen, (212, 176, 106), (250, 250, 123, 123))

        # Behavior:
        if sand1.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9
        if sand2.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9
        if sand3.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9
        if sand4.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9

        water1 = pygame.draw.rect(screen, (54, 84, 217), (900, 50, 250, 100))
        water2 = pygame.draw.rect(screen, (54, 84, 217), (450, 450, 150, 200))
        water3 = pygame.draw.rect(screen, (54, 84, 217), (0, 300, 50, 500))

        # Behavior:
        if water1.collidepoint(x, y):
            x = 120
            xSpeed = 0
            y = 600
            ySpeed = 0
        if water2.collidepoint(x, y):
            x = 120
            xSpeed = 0
            y = 600
            ySpeed = 0
        if water3.collidepoint(x, y):
            x = 120
            xSpeed = 0
            y = 600
            ySpeed = 0

        # Wall Script (x, y, length, width)
        wall1 = pygame.draw.rect(screen, (THECOLORS['grey']), (750, 375, 50, 600))
        wall2 = pygame.draw.rect(screen, (THECOLORS['grey']), (1050, 375, 50, 375))
        wall3 = pygame.draw.rect(screen, (THECOLORS['grey']), (800, 200, 500, 45))

        if wall1.collidepoint(x,y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)
        if wall2.collidepoint(x,y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)
        if wall3.collidepoint(x,y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)

        # Only draw line when stopped
        if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
            pygame.draw.line(screen, (0, 165, 0), (x, y), pygame.mouse.get_pos())

        # Hit the ball on click
        for event in pygame.event.get():
            if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
                if event.type == pygame.MOUSEBUTTONUP:
                    xSpeed = -int((pygame.mouse.get_pos()[0] - x) / 20)
                    ySpeed = -int((pygame.mouse.get_pos()[1] - y) / 20)
                    strokes += 1

        # Move the ball
        x += xSpeed
        y += ySpeed

        # Deceleration
        xSpeed = xSpeed * 0.98
        ySpeed = ySpeed * 0.98

        # Bouncing
        if x > 1184 or x < 16:
            xSpeed *= -1
        if y > 736 or y < 16:
            ySpeed *= -1

        # Checks to see if in hole
        if ((x - 925) ** 2 + (y - 700) ** 2) ** 0.5 < 25:
            xSpeed *= 0.97
            ySpeed *= 0.97
            if abs(ySpeed) < 0.1 and abs(xSpeed) < 0.1:
                toNext += 1

        # Ball design, at the end because pygame is kind of stupid, and makes things that are the end appear on top.
        pygame.draw.circle(screen, (255, 255, 255), (round(x), round(y)), 15)

        # Par counter
        screen.blit(tarandeepSmall, (1050, 575))
        parCount = font.render(f'PAR   {strokes}', True, (THECOLORS["white"]), (0, 0, 0))
        screen.blit(parCount, (1070, 700))

        pygame.display.update()