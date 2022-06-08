'''
Multiple objects bouncing on the screen
When the left mouse button is clicked, more balls are added
Author: Ms. k
Date: May 31, 2022
'''
import pygame, sys, os, time, random
from pygame.locals import *
from pygame.color import THECOLORS

## If you get the no available video device error, copy and paste the below code ##
import platform

if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
### If you get the no available video device error, copy and paste the above code ###

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((600, 480))
pygame.display.set_caption('The Bouncing Balls')
screen = pygame.display.get_surface()
myfont = pygame.font.SysFont("Times New Roman", 25)


# The screen is the Drawing window
screen.fill(THECOLORS['white'])

# Load the picture into the program
ballImg = pygame.Surface((100, 100))
surfRect = ballImg.get_rect()

pygame.draw.circle(ballImg, THECOLORS['red'], (50, 50), 50,)
pygame.draw.circle(ballImg, THECOLORS['black'], (32, 40), 9,)
pygame.draw.circle(ballImg, THECOLORS['black'], (68, 40), 9,)
pygame.draw.line(ballImg, (THECOLORS['black']), (30, 70), (70, 70), 4)
pygame.draw.line(ballImg, (THECOLORS['black']), (20, 60), (30, 72), 5)
pygame.draw.line(ballImg, (THECOLORS['black']), (80, 60), (70, 72), 5)

screen.blit(ballImg, surfRect)

ballImg.set_colorkey(THECOLORS['white'])

# Create a surface for the image and make background transparent
img = pygame.Surface((ballImg.get_width(), ballImg.get_height()))
img.blit(ballImg, (0, 0))
img.set_colorkey((0, 0, 0))

# Get the rect for the image
ballRect = img.get_rect()

# Move the starting position of the image to the middle of the screen
ballRect.centerx = 300
ballRect.centery = 240

# Event Handling #
keepGoing = True

# a list of all the individual ball objects
# (ballRect, xDir, yDir)
# Notice the surface does not need to be saved in the list, every ball uses the same surface
ballList = [(ballRect, 1, 1)]

# Game loop
while keepGoing:
    clock.tick(120)  # Frame rate 30

    # Paint the screen white
    screen.fill((255, 255, 255))

    # Go through every element in the ballList
    for ball in range(0, len(ballList)):

        # read the rect and directions of the current ball into separate variables
        # ballPos = ball's rectangle
        # xdir = ball's current x direction
        # ydir = ball's current y direction
        ballPos, xdir, ydir = ballList[ball]

        # blit the current ball to the screen
        screen.blit(img, ballPos)

        # Calculate the new position for the ball after moving
        x = ballPos[0] + xdir * 8
        y = ballPos[1] + ydir * 8

        # if the ball reaches the edge, bounce it back
        if x <= 0 or x >= 600 - img.get_width():
            xdir = -xdir
        if y <= 0 or y >= 480 - img.get_height():
            ydir = -ydir

        # update the new rectangle position of the ball
        ballPos[0] = x
        ballPos[1] = y

        # update the ball position and direction and replace the previous tuple in the list
        newBallPos = (ballPos, xdir, ydir)
        ballList[ball] = newBallPos

    pygame.display.flip()

    pygame.time.delay(20)

    events = pygame.event.get()

    # Event Loop
    for ev in events:

        # Check if mouse button is pressed
        if ev.type == MOUSEBUTTONDOWN:

            # x and y coordinates of the mouse
            x, y = ev.pos

            # if the left button on mouse is pressed, add a new ball to the screen
            if ev.button == 1:

                # if the x coord will create and off screen ball, update the position to be on screen
                if x > 600 - img.get_width():
                    x = 600 - img.get_width()

                # if the y coord will create and off screen ball, update the position to be on screen
                if y > 480 - img.get_height():
                    y = 480 - img.get_height()

                # Based on which area of the screen is clicked, set the initial direction
                if x <= 300 and y <= 240:
                    xdir = 1
                    ydir = 1
                elif x <= 300 and y > 240:
                    xdir = 1
                    ydir = -1
                elif x > 300 and y <= 240:
                    xdir = -1
                    ydir = 1
                else:
                    xdir = -1
                    ydir = -1

                # Create a rectangle for the new ball
                # Notice we are just creating a rect, not another surface!
                # The surface can be reused (like a photocopy), we just need a new position
                addBallRect = Rect(x, y, img.get_width(), img.get_height())

                # save the new ball information to the list
                newBall = (addBallRect, xdir, ydir)
                ballList.append(newBall)

        if ev.type == QUIT:
            keepGoing = False  # Stop the program, it's detected quit...

pygame.quit()  # Keep this IDLE friendly