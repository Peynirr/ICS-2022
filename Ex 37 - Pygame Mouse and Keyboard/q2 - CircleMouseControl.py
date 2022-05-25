# Omercan
# May 24 2022
# Ex 37 Q2
# Moving a Circle and Resizing it Using Mouse Input
import pygame
import platform, os
from pygame.color import THECOLORS
from pygame.locals import *
 
#Initiating Pygame
pygame.init()
 
#Pygame Configuration
size = [800, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#Title Bar Caption 
pygame.display.set_caption("Ex 37 - Q2: Moving and Controlling the Radius of a Circle Using a Mouse")

#For TDSB computers
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Loop until the user clicks the close button
finished = False

#Base Radius of the Circle
radius = 10

#Function
def drawCircle(screen, x, y, radius):
    pygame.draw.circle(screen, (THECOLORS["orange"]), (x, y), radius)

#While Loop
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
 
    # Call draw stick figure function
    position = pygame.mouse.get_pos()
    x = position[0] #Position of x
    y = position[1] #Position of y
 
    #Color of the Background
    screen.fill(THECOLORS["white"])
    drawCircle(screen, x, y, radius)
 
    #Radius control
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  #The radius is increased by clicking the left mouse button.
            radius = min(200, radius + 2)
        elif event.button == 3:  #Right-clicking reduces the radius.
            radius = max(1, radius - 2)

    pygame.display.flip()
    
    #Refresh rate
    clock.tick(120)
pygame.quit()