# Omercan
# May 25 2022
# Ex 38 Q2
# Custom-made Emoji Bouncing Around in a Pygame Windows
import pygame
import os, time
import platform
from pygame.locals import *
from pygame.color import THECOLORS

#Initiating Pygame
pygame.init()

#For TDSB Computers
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Pygame Configuration
size = width, height = (700, 600)
screen = pygame.display.set_mode(size)
screen.fill(THECOLORS['black']) #Background

#Title Bar Caption
pygame.display.set_caption("Ex 38 - Q2: Bouncing Emoji")

clock = pygame.time.Clock()
speed = [2, 2]

#Surface Dimensions
newSurf = pygame.Surface((100, 100))
surfRect = newSurf.get_rect()

#Emoji Face Drawing
pygame.draw.circle(newSurf, THECOLORS['yellow'], (50, 50), 50)
pygame.draw.circle(newSurf, THECOLORS['black'], (32, 40), 9)
pygame.draw.circle(newSurf, THECOLORS['black'], (68, 40), 9)
pygame.draw.line(newSurf, (THECOLORS['black']), (30, 70), (70, 70), 4)
pygame.draw.line(newSurf, (THECOLORS['black']), (20, 80), (30, 70), 5)
pygame.draw.line(newSurf, (THECOLORS['black']), (80, 80), (70, 70), 5)

screen.blit(newSurf, surfRect)

keepGoing = True

pygame.display.flip()

while keepGoing:
    #Refresh Rate
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
    #The Speed of the Bouncing Emoji
    surfRect = surfRect.move(speed)

    if surfRect.left < 0 or surfRect.right > width:
        speed[0] *= -1

    if surfRect.top < 0 or surfRect.bottom > height:
        speed[1] *= -1

    screen.fill(THECOLORS['black'])

    screen.blit(newSurf, surfRect)

    pygame.display.flip()
pygame.quit()