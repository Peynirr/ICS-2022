# Omercan
# June 21 2022
# Ex 41
# Colliding Sprites
import pygame, sys, os, time, random, platform
from pygame.locals import *
from pygame.color import THECOLORS

#Initiating Pygame
pygame.init()

#Pygame Configuration
window = pygame.display.set_mode((800, 600))
screen = pygame.display.get_surface()
clock = pygame.time.Clock()

#Background Colour
screen.fill(THECOLORS['white'])

#Title Bar of Pygame Window
pygame.display.set_caption('Colliding Sprites')

#Transparent Image Of Tarandeep
tarandeep = pygame.image.load("Ex 41 - Colliding Sprites/assets/tarandeep.png")

#Smaller Size of Tarandeep
tarandeepSmall = pygame.transform.scale(tarandeep, (90, 90))
tarandeepBigger = pygame.transform.scale(tarandeep, (150, 150))
xImage = pygame.image.load("Ex 41 - Colliding Sprites/assets/x.png")

#For TDSB Computers
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Keep Shape Class
class keepShape (pygame.sprite.Sprite):
    #Sprites
    def __init__(self, xCoordinate, yCoordinate):
        pygame.sprite.Sprite.__init__(self)

        #Stores Image
        self.image = pygame.Surface((90, 90))
        self.image.blit(tarandeepImage, (0, 0))
        self.image.set_colorkey(THECOLORS['white'])

        #Summons Rectangle For Image
        self.rect = self.image.get_rect()
        self.rect.centery = yCoordinate
        self.rect.centerx = xCoordinate

#Moving Objects class
class movingObjects (pygame.sprite.Sprite):
    #Sprites
    def __init__(self, xCoordinate, yCoordinate, xDirection, yDirection):
        pygame.sprite.Sprite.__init__(self)

        #Stores Image
        self.image = tarandeepBigger
        self.image.blit(tarandeepBigger, (0, 0))
        self.image.set_colorkey(THECOLORS['white'])

        #Summons Rectangle For Image
        self.rect = self.image.get_rect()
        self.rect.centery = yCoordinate
        self.rect.centerx = xCoordinate

        #x, y Locations
        self.xdir = xDirection
        self.ydir = yDirection

    #Create Function For Movement Of Various Shapes
    def update(self):
        #New Position
        self.rect.centerx = self.rect.centerx + self.xdir * 4
        self.rect.centery = self.rect.centery + self.ydir * 4

        #If Statements
        if self.rect.centerx <= 45 or self.rect.centerx >= screen.get_width() - 45:
            self.xdir = -self.xdir
        if self.rect.centery <= 45 or self.rect.centery >= screen.get_height() - 95:
            self.ydir = -self.ydir

#Image Of Tarandeep 
tarandeepImage = xImage
anotherTarandeepImage = tarandeepSmall

shapeList = pygame.sprite.Group()
moveShapeList = pygame.sprite.Group()

number = random.randrange(10, 21)

#Creates Random Tarandeeps From A Random Number In A Range
#For Loop
for i in range(number):
    #Random x, y Coordinates Are Generated
    xCoordinate = random.randrange(45, screen.get_width() - 45)
    yCoordinate = random.randrange(45, screen.get_height() - 95)

    #Random x, y Directions Are Generated
    xdir = random.choice([-1, 1])
    ydir = random.choice([-1, 1])

    #New Shape
    newShape = movingObjects(xCoordinate, yCoordinate, xdir, ydir)
    shapeList.add(newShape)
    moveShapeList.add(newShape)

xShape = keepShape(screen.get_width() / 2, screen.get_height() / 2)

shapeList.add(xShape)

count = 0

myFont = pygame.font.SysFont("Comic Sans", 25)
txt = myFont.render("Count: " + str(count), True, (0, 0, 0))

#Game Closes If False
keepPlaying = True

#Game Loop
while keepPlaying:
    clock.tick(120)
    screen.fill(THECOLORS['white'])

    #Draws The Shapes Listed
    shapeList.draw(screen)
    screen.blit(txt, (20, screen.get_height() - 50))
    shapeList.update()
    collided = pygame.sprite.spritecollide(xShape, moveShapeList, False)

    for shape in collided:
        count = count + 1
        shape.kill()

    text = myFont.render("Tarandeep's Popped: " + str(count), True, (THECOLORS['orange']))

    pygame.display.flip()
    pygame.time.delay(20)

    # Event Loop
    events = pygame.event.get()

    for event in events:
        #Pygame Windows Closes If True
        if event.type == QUIT:
            keepPlaying = False
pygame.quit()