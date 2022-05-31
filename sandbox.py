#Sandbox

""" 
Type placed with mouse 
Coordinates are blitted to screen with mouse initiated in game loop
Left click to see text. Try to hold the mouse button down.
"""

# Import & initialize the pygame module
import pygame
from pygame.locals import *  # This is not necessary for most games, but can simplify some things
from pygame.color import THECOLORS

pygame.init()  # initializes all pygame imports

import platform, os

if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

# Set-up the main display window and the background
size = (640, 480)  # <-- that is a tuple (just like a list) for width & height
screen = pygame.display.set_mode(size)  # <-- screen is now a Surface type object

# caption appears in the title bar
pygame.display.set_caption("Type placed from within the Pygame game loop!")

screen.fill(THECOLORS['ivory'])  # fills screen surface with colour

# Define a custom font
myFont = pygame.font.SysFont("Arial Black", 25)

pygame.display.flip()  # <-- refresh the display

# The game loop
clock = pygame.time.Clock()  # <-- used to control the frame rate
keepGoing = True  # <-- a 'flag' variable for the game loop condition

while keepGoing:

    clock.tick(30)  # <-- Set a constant frame rate, argument is frames per second

    # Handle any events in the current frame
    for ev in pygame.event.get():  # <-- returns a list of all Events in this frame
        if ev.type == QUIT:  # <-- this special event type happens when the window is closed
            keepGoing = False

    # stores 3-number tuple for left, right and middle mouse button
    (leftBut, centreBut, rightBut) = pygame.mouse.get_pressed()

    # if left button on mouse is pressed
    if leftBut == 1:

        # read the current position of the mouse into mx, my
        (mx, my) = pygame.mouse.get_pos()

        # Update and refresh the display with text of the current coordinates
        if my > 0 and mx > 0:
            # create a string of the current coordinates
            coord = str(mx) + ", " + str(my)

            # render the coordinates with the custom font and the colour forest green
            text = myFont.render(coord, True, THECOLORS['forestgreen']).convert_alpha()

            # place the text onto the surface screen at the mouse coordinates
            screen.blit(text, (mx, my))

        pygame.display.flip()  # <-- refresh the display

pygame.quit()  # Keep this IDLE friendly
