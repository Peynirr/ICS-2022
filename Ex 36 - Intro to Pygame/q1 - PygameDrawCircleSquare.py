# Omercan
# May 20 2022
# Ex 36 Q1
# Drawing a Circle and Square With Diagonal Lines

#Setup
import pygame
from pygame.color import THECOLORS
from pygame.locals import *

pygame.init()

import platform, os
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Window
size = (700, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Squares")
screen.fill(THECOLORS["ivory"])

#Rectangles
pygame.draw.circle(screen, (THECOLORS["cornflowerblue"]), (100, 500), 100)
pygame.draw.circle(screen, (THECOLORS["seagreen2"]), (600, 100), 100)
pygame.draw.circle(screen, (THECOLORS["orangered1"]), (100, 100), 100)
pygame.draw.circle(screen, (THECOLORS["darkorchid2"]), (600, 500,), 100)

#Circle
pygame.draw.rect(screen, (THECOLORS["yellow1"]), (300, 250, 100, 100))

#Lines
pygame.draw.line(screen, (THECOLORS["maroon1"]), (0, 600), (700, 0), 4)
pygame.draw.line(screen, (THECOLORS["deeppink1"]), (0, 0), (700, 600), 4)

pygame.display.flip()

#Loop
clock = pygame.time.Clock()
keepGoing = True

while keepGoing:
    clock.tick(30)
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keepGoing = False
pygame.display.flip()
pygame.quit()