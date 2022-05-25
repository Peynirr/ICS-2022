import pygame
import os, time
from pygame.locals import *
from pygame.color import THECOLORS

pygame.init()

import platform
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

size = width, height = (700, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("ex38num2")

screen.fill(THECOLORS['black'])

clock = pygame.time.Clock()

speed = [2, 2]

newSurf = pygame.Surface((100, 100))
surfRect = newSurf.get_rect()

pygame.draw.circle(newSurf, THECOLORS['yellow'], (50, 50), 50,)
pygame.draw.circle(newSurf, THECOLORS['black'], (32, 40), 9,)
pygame.draw.circle(newSurf, THECOLORS['black'], (68, 40), 9,)
pygame.draw.line(newSurf, (THECOLORS['black']), (30, 70), (70, 70), 4)
pygame.draw.line(newSurf, (THECOLORS['black']), (20, 60), (30, 72), 5)
pygame.draw.line(newSurf, (THECOLORS['black']), (80, 60), (70, 72), 5)

screen.blit(newSurf, surfRect)

keepGoing = True

pygame.display.flip()

while keepGoing:
    clock.tick(120)

    screen.fill(THECOLORS['black'])
    
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keepGoing = False    
            
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                (x, y) = ev.pos
                surfRect.centerx = x
                surfRect.centery = y
            
    surfRect = surfRect.move(speed)

    if surfRect.left < 0 or surfRect.right > width:
        speed[0] *= -1

    if surfRect.top < 0 or surfRect.bottom > height:
        speed[1] *= -1

    screen.fill(THECOLORS['black'])

    screen.blit(newSurf, surfRect)

    pygame.display.flip()
pygame.quit()