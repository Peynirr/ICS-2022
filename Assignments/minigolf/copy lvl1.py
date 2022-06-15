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
tarandeepSmall = pygame.transform.scale(tarandeep, (100, 100))
# Starting posiktion, strokes and speed.
xSpeed = 0
ySpeed = 0
x = 500
y = 500
strokes = 0
font = pygame.font.Font('assets/BRLNSB.TTF', 30)
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

    # Drawing sand
    sandbox = pygame.draw.rect(screen, (212, 176, 106), (234, 345, 123, 123))
    # Behavior:
    if sandbox.collidepoint(x, y):
        xSpeed *= 0.9
        ySpeed *= 0.9

    water = pygame.draw.rect(screen, (54, 84, 217), (0, 200, 50, 300))
    # Behavior:
    if water.collidepoint(x, y):
        x = 500
        xSpeed = 0
        y = 500
        ySpeed = 0

    wall1 = pygame.draw.rect(screen, (255, 255, 255), (300, 200, 300, 200))
    wall2 = pygame.draw.rect(screen, (255, 255, 255), (300, 200, 300, 200))
    wall3 = pygame.draw.rect(screen, (255, 255, 255), (300, 200, 300, 200))
    wall4 = pygame.draw.rect(screen, (255, 255, 255), (300, 200, 300, 200))
    if wall1.collidepoint(x,y):
        xSpeed = -1 * abs(xSpeed)
        ySpeed = -1 * abs(ySpeed)
        



    pygame.draw.circle(screen, (255, 255, 255), (round(x), round(y)), 15)

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
    if ((x - 100) ** 2 + (y - 100) ** 2) ** 0.5 < 25:
        xSpeed *= 0.97
        ySpeed *= 0.97
        if abs(ySpeed) < 0.1 and abs(xSpeed) < 0.1:
            winmsg = font.render(f'Nice! {strokes} strokes!', True, (255, 255, 255), (24, 110, 47))
            screen.blit(winmsg, (150, 400))
            time.sleep(1)
            x = 500
            xSpeed = 0
            y = 500
            ySpeed = 0
            toNext += 1

    pygame.display.update()