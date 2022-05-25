# Omercan
# May 24 2022
# Ex 37 Q1
# Moving a Circle Using the Arrow Keys on the Keyboard
import pygame
import platform, os
from pygame.color import THECOLORS
from pygame.locals import *

#Initating Pygame
pygame.init()

#For TDSB computers
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Screen Size
screen = pygame.display.set_mode(((800, 600)))

#Title Bar for the Windows
pygame.display.set_caption(("Ex 37 - Q1: Moving a Shape Using Keyboard Input"))

#Dimension of the Circle
x, y = 400, 300
width, height = 100, 100
radius = 10

clock = pygame.time.Clock()
finished = True

#While Loop
while finished:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = False
    
    #Keys Pressed
    keys = pygame.key.get_pressed()
    
    #Left Arrow key
    if keys[pygame.K_LEFT]:
        x -= 2
    #Right Arrow key
    if keys[pygame.K_RIGHT]:
        x += 2
    #Up Arrow key
    if keys[pygame.K_UP]:
        y -= 2
    #Down Arrow key
    if keys[pygame.K_DOWN]:
        y += 2

    #Background Color
    screen.fill(THECOLORS["white"])
    
    pygame.draw.circle(screen, (THECOLORS["red"]), (x, y), radius)
    pygame.display.update()
pygame.quit()