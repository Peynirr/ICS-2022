# Omercan
# June 20 2022
# Ex 40
import pygame, sys, os, time, random
from pygame.locals import *
from pygame.color import THECOLORS
import platform

#Initiating Pygame
pygame.init()

#Pygame Configuration
window = pygame.display.set_mode((1280, 720))
screen = pygame.display.get_surface()
clock = pygame.time.Clock()

#Background Color
screen.fill(THECOLORS['white'])

#Title Bar
pygame.display.set_caption('The Bouncing Balls')

#For TDSB Computers
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Drawing Ball Surface
ballImg = pygame.Surface((100, 100))
surfRect = ballImg.get_rect()

#Drawing Smile Emoji
pygame.draw.circle(ballImg, THECOLORS['orange'], (50, 50), 50,)
pygame.draw.circle(ballImg, THECOLORS['black'], (32, 40), 9,)
pygame.draw.circle(ballImg, THECOLORS['black'], (68, 40), 9,)
pygame.draw.line(ballImg, (THECOLORS['black']), (30, 70), (70, 70), 4)
pygame.draw.line(ballImg, (THECOLORS['black']), (20, 60), (30, 72), 5)
pygame.draw.line(ballImg, (THECOLORS['black']), (80, 60), (70, 72), 5)

screen.blit(ballImg, surfRect)

#Makes The Surface Transparent
ballImg.set_colorkey(THECOLORS['white'])
img = pygame.Surface((ballImg.get_width(), ballImg.get_height()))
img.blit(ballImg, (0, 0))
img.set_colorkey((0, 0, 0))

#Get The Rect
ballRect = img.get_rect()

#Postion
ballRect.centerx = 640
ballRect.centery = 360

#Closes the Windows If False
keepGoing = True
ballList = [(ballRect, 1, 1)]

#While Loop
while keepGoing:
    #120 Frames Per Second
    clock.tick(120)
    screen.fill((255, 255, 255))

    for ball in range(0, len(ballList)):
        ballPos, xdir, ydir = ballList[ball]

        screen.blit(img, ballPos)

        #Calculates The New Position
        x = ballPos[0] + xdir * 8
        y = ballPos[1] + ydir * 8

        #If Ball Touches The Edge, It Bounces
        if x <= 0 or x >= 1280 - img.get_width():
            xdir = -xdir
        if y <= 0 or y >= 720 - img.get_height():
            ydir = -ydir

        #Updates The Position
        ballPos[0] = x
        ballPos[1] = y
        newBallPos = (ballPos, xdir, ydir)
        ballList[ball] = newBallPos
    pygame.display.flip()
    pygame.time.delay(20)

    # Event Loop
    events = pygame.event.get()

    for ev in events:
        # Check if mouse button is pressed
        if ev.type == MOUSEBUTTONDOWN:
            x, y = ev.pos
            if ev.button == 1:
                #Updates x Position To Screen
                if x > 1280 - img.get_width():
                    x = 1280 - img.get_width()

                #Updates y Position To Screen
                if y > 720 - img.get_height():
                    y = 720 - img.get_height()

                #Sets Initial Direction
                if x <= 640 and y <= 360:
                    xdir = 1
                    ydir = 1
                elif x <= 640 and y > 360:
                    xdir = 1
                    ydir = -1
                elif x > 640 and y <= 360:
                    xdir = -1
                    ydir = 1
                else:
                    xdir = -1
                    ydir = -1

                #New Ball
                addBallRect = Rect(x, y, img.get_width(), img.get_height())

                #Adds New Ball To List
                newBall = (addBallRect, xdir, ydir)
                ballList.append(newBall)
        
        #Closes Pygame Windows
        if ev.type == QUIT:
            keepGoing = False
pygame.quit()