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
pygame.draw.rect(screen, (THECOLORS["cornflowerblue"]), (0, 0, 100, 100))
pygame.draw.rect(screen, (THECOLORS["seagreen2"]), (600, 0, 100, 100))
pygame.draw.rect(screen, (THECOLORS["orangered1"]), (0, 500, 100, 100))
pygame.draw.rect(screen, (THECOLORS["darkorchid2"]), (600, 500, 100, 100))

#Circle
pygame.draw.circle(screen, (THECOLORS["yellow1"]),  (350, 300), 100)

#Lines
pygame.draw.line(screen, (THECOLORS["maroon1"]), (0, 300), (700, 300), 4)
pygame.draw.line(screen, (THECOLORS["deeppink1"]), (350, 0), (350, 600), 4)

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
