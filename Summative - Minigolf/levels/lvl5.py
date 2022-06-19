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
x = 625
y = 650
strokes = 0
toNext = 0

def level5(toNext, xSpeed, ySpeed, x, y, strokes):
    # Starting position, strokes and speed.
    xSpeed = 0
    ySpeed = 0
    x = 625
    y = 650
    strokes = 0
    toNext = 0

    while toNext == 0:
        screen.blit(bgImg, (0, 0))
        pygame.time.delay(10)

        # Hole to get ball into
        pygame.draw.circle(screen, (255, 255, 255), (120, 115), 25)
        pygame.draw.circle(screen, (0, 0, 0), (120, 115), 24)

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

        water1 = pygame.draw.rect(screen, (54, 84, 217), (0, 0, 1200, 58))
        water2 = pygame.draw.rect(screen, (54, 84, 217), (900, 0, 300, 750))
        water3 = pygame.draw.rect(screen, (54, 84, 217), (0, 174, 800, 100))
        water4 = pygame.draw.rect(screen, (54, 84, 217), (0, 174, 300, 600))
        water5 = pygame.draw.rect(screen, (54, 84, 217), (300, 600, 250, 500))
        water6 = pygame.draw.rect(screen, (54, 84, 217), (700, 400, 300, 400))
        water7 = pygame.draw.rect(screen, (54, 84, 217), (380, 350, 280, 170))
        water8 = pygame.draw.rect(screen, (54, 84, 217), (0, 50, 50, 170))

        # Behavior:
        if water1.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0
        if water2.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0
        if water3.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0
        if water4.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0
        if water5.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0
        if water6.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0
        if water7.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0
        if water8.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0

        # Wall Script (x, y, length, width)
    
        # Only draw line when stopped
        if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
            pygame.draw.line(screen, (0, 0, 0), (x, y), pygame.mouse.get_pos())

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
        if ((x - 120) ** 2 + (y - 115) ** 2) ** 0.5 < 25:
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