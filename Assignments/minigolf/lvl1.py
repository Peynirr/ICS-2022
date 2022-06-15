import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import sys
import time

# Generic importing.
# Initalizes Pygame and sets the window up
pygame.init()
screen = pygame.display.set_mode((1200, 750))
bgImg = pygame.image.load('assets/golfBackground.png')
tarandeep = pygame.image.load('assets/tarandeep.png')
tarandeepSmall = pygame.transform.scale(tarandeep, (175, 175))

# Starting position, strokes and speed.
xSpeed = 0
ySpeed = 0
x = 75
y = 700
strokes = 0
font = pygame.font.Font('assets/BRLNSB.TTF', 30)

def level1(toNext, xSpeed, ySpeed, x, y, strokes):
    # Starting position, strokes and speed.
    xSpeed = 0
    ySpeed = 0
    x = 75
    y = 700
    strokes = 0
    toNext = 0

    while toNext == 0:
        screen.blit(bgImg, (0, 0))
        screen.blit(tarandeepSmall, (1020, 650))
        pygame.time.delay(10)

        # Hole to get ball into
        pygame.draw.circle(screen, (255, 255, 255), (650, 650), 25)
        pygame.draw.circle(screen, (0, 0, 0), (650, 650), 24)

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

        wall1 = pygame.draw.rect(screen, (THECOLORS['grey']), (150, 250, 50, 600))
        wall2 = pygame.draw.rect(screen, (THECOLORS['grey']), (125, 250, 50, 600))
        wall3 = pygame.draw.polygon(screen, (THECOLORS['grey']), [(1200, 0), (800, 0), (1200, 400)])
        wall4 = pygame.draw.polygon(screen, (THECOLORS['grey']), [(1200, 0), (800, 0), (1200, 400)])

        if wall1.collidepoint(x, y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)
        if wall2.collidepoint(x, y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)
        if wall3.collidepoint(x, y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)
        if wall4.collidepoint(x, y):
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
        if ((x - 650) ** 2 + (y - 650) ** 2) ** 0.5 < 25:
            xSpeed *= 0.97
            ySpeed *= 0.97
            if abs(ySpeed) < 0.1 and abs(xSpeed) < 0.1:
                toNext += 1

        # Ball design, at the end because pygame is kind of stupid, and makes things that are the end appear on top.
        pygame.draw.circle(screen, (THECOLORS['white']), (round(x), round(y)), 15)

        # Par counter
        screen.blit(tarandeepSmall, (1050, 575))
        parCount = font.render(f'PAR   {strokes}', True, (THECOLORS["white"]), (0, 0, 0))
        screen.blit(parCount, (1070, 700))

        pygame.display.update()

level1(toNext, xSpeed, ySpeed, x, y, strokes)