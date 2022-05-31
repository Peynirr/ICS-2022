# Omercan
# May 31 2022
# Ex 39
# Colliding Coloured Rctangles
import pygame, sys, os, time, random
from pygame.locals import *
from pygame.color import THECOLORS
import platform, os

#Initiating Pygame
pygame.init()

#For TDSB Computers
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Pygame Configuration

size = (600, 400)
screen = pygame.display.set_mode(size)
screen.fill(THECOLORS['white'])

#Title Bar
pygame.display.set_caption('Colliding Coloured Rectangles')

myFont = pygame.font.SysFont("wandra", 48)
clock = pygame.time.Clock()

#Creating The First Surface
img1 = pygame.Surface((100, 100))
img1.fill(THECOLORS['red'])

#Get Rectangle From The Surface
img1Rect = img1.get_rect()
img1.blit(img1, img1Rect)

#Creating The Second Surface
img2 = pygame.Surface((50, 50))
img2.fill(THECOLORS['blue'])     

#Get Rectangle From The Surface
img2Rect = img2.get_rect()
img2.blit(img2, img2Rect)

pygame.display.flip()

#Initials Coordinates and Direction Variables for Each Rectangle

#Image 1
ximg1 = 50
yimg1 = 50
img1Rect = img1Rect.move(ximg1, yimg1)
xdir1 = 2
ydir1 = 2

#Image 2
ximg2 = 300
yimg2 = 100
img2Rect = img2Rect.move(ximg2, yimg2)
xdir2 = -2
ydir2 = 2

# Game Loop
keepGoing = True

#While Loop When The Game Is Running
while keepGoing:
    clock.tick(100)
    #Fills The Screen
    screen.fill((255, 255, 255))
    #Blit img1 To The Screen
    screen.blit(img1, img1Rect)

    #img1 Bouncing Off The Left/Right Edge Of The Window
    if ximg1 >= size[0] - img1.get_width() or ximg1 <= 0:
        xdir1 = -xdir1
        ximg1 = ximg1 + 8 * xdir1

    #img1 Bouncing Off The Top/Bottom Edge Of The Window
    if yimg1 <= 0 or yimg1 >= size[1] - img1.get_height():
        ydir1 = -ydir1
        yimg1 = yimg1 + 8 * ydir1
    
    #Updates The Rectangle When img1 Bounces Off The Edge Of The Screen
    img1Rect.left = ximg1
    img1Rect.top = yimg1

    #Blit img2 To Screen
    screen.blit(img2, img2Rect)

    #img2 Bouncing Off The Left/Right Edge Of The Window
    if ximg2 >= size[0] - img2.get_width() or ximg2 <= 0:
        xdir2 = -xdir2
        ximg2 = ximg2 + 8 * xdir2
    
    # img2 Bouncing Off The Top/Bottom Edge Of The Window
    if yimg2 <= 0 or yimg2 >= size[1] - img2.get_height():
        ydir2 = -ydir2
        yimg2 = yimg2 + 8 * ydir2
    
    #Updates The Rectangle When img2 Bounces Off Edge Of The Screen
    img2Rect.left = ximg2
    img2Rect.top = yimg2

    #Finds The Center (x, y) Of img1
    x1cen = img1Rect.centerx
    y1cen = img1Rect.centery

    #Finds The Center (x, y) Of img2
    x2cen = img2Rect.centerx
    y2cen = img2Rect.centery

    #Calculates The Distance Between The Centers Of The Two Rectangles
    distance = ((x1cen - x2cen) ** 2 + (y1cen - y2cen) ** 2) ** (0.5)

    #Check If Two Rectangles Have Collided
    if img1Rect.colliderect(img2Rect): #distance < 90:      
        #Change The Color Of The First Image
        red = random.randrange(0, 255)
        green = random.randrange(0, 255)
        blue = random.randrange(0, 225)      
        img1.fill((red, green, blue))              
        
        #Check That Both Squares Are Not Moving In The Same x Direction
        if xdir1 != xdir2:
            xdir1 = -xdir1
            xdir2 = -xdir2
        
        #Check That Both Squares Are Not Moving In The Same y Direction
        if ydir1 != ydir2:
            ydir1 = -ydir1
            ydir2 = -ydir2                    
    pygame.time.delay(20)
    pygame.display.flip()
    
    #Advance The Next Coordinates For Images
    ximg1 = ximg1 + xdir1 * 8
    yimg1 = yimg1 + ydir1 * 8
    img1Rect.left = ximg1
    img1Rect.top = yimg1
    ximg2 = ximg2 + xdir2 * 8
    yimg2 = yimg2 + ydir2 * 8
    img2Rect.left = ximg2
    img2Rect.top = yimg2
    
    #Event Handling
    events = pygame.event.get()
    for ev in events:
        if ev.type == QUIT:
            keepGoing = False
            clock.tick(100)
pygame.quit()