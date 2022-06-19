# Omercan, Abhishek
# June 17 2022
# ISC2O1 Culminating
# Mini-Golf Base Game
import pygame, sys, time
from pygame.locals import *
from pygame.color import THECOLORS

#Intialization Setup
pygame.init()
screen = pygame.display.set_mode((1200, 750))   #Display Size
bgImg = pygame.image.load('assets/golfBackground.png')  #Game Background
tarandeep = pygame.image.load('assets/tarandeep.png')   #Base Photo of Tarandeep
tarandeepSmall = pygame.transform.scale(tarandeep, (175, 175))  #Smaller Size of Tarandeep
font = pygame.font.Font('assets/BRLNSB.TTF', 30)    #Desired Font

#Main Function
def main():
    main_menu()
    level1()
    level2()
    level3()
    level4()
    level5()
    import mainmenu

#Main Menu Function
def main_menu():
    import mainmenu

#Level 1 Function
def level1():
    #Default Speed
    xSpeed = 0
    ySpeed = 0

    #Default Position
    x = 75
    y = 700

    strokes = 0

    #Used to move to the next level
    toNext = 0

    #While Loop to Close the Window And Move To The Next Level When it == 1
    while toNext == 0:
        screen.blit(bgImg, (0, 0))
        screen.blit(tarandeepSmall, (1020, 650))
        pygame.time.delay(10)

        #Hole Location
        pygame.draw.circle(screen, (255, 255, 255), (650, 650), 25)
        pygame.draw.circle(screen, (0, 0, 0), (650, 650), 24)

    #Hit the ball on click
        if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
            pygame.draw.line(screen, (0, 165, 0), (x, y), pygame.mouse.get_pos())
        for event in pygame.event.get():
            if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
                if event.type == pygame.MOUSEBUTTONUP:
                    xSpeed = -int((pygame.mouse.get_pos()[0] - x) / 20)
                    ySpeed = -int((pygame.mouse.get_pos()[1] - y) / 20)
                    strokes += 1
        
        #Vertical/Horizontal Speed
        x += xSpeed
        y += ySpeed
        xSpeed = xSpeed * 0.98
        ySpeed = ySpeed * 0.98

        #Walls (x, y, length, width)
        wall1 = pygame.draw.rect(screen, (THECOLORS['grey']), (150, 250, 50, 600))
        wall2 = pygame.draw.rect(screen, (THECOLORS['grey']), (125, 250, 50, 600))
        wall3 = pygame.draw.polygon(screen, (THECOLORS['grey']), [(1200, 0), (800, 0), (1200, 400)])
        wall4 = pygame.draw.polygon(screen, (THECOLORS['grey']), [(1200, 0), (800, 0), (1200, 400)])

        #Collision Rules for Walls
        if wall1.collidepoint(x, y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)
        if wall2.collidepoint(x, y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)
        if wall3.collidepoint(x, y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)
        if wall4.collidepoint(x, y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)

        #Draws The Line Puller To Adjust Speed When Clicked
        if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
            pygame.draw.line(screen, (0, 0, 0), (x, y), pygame.mouse.get_pos())

        #Moves The Golf Ball When Clicked
        for event in pygame.event.get():
            if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
                if event.type == pygame.MOUSEBUTTONUP:
                    xSpeed = -int((pygame.mouse.get_pos()[0] - x) / 20)
                    ySpeed = -int((pygame.mouse.get_pos()[1] - y) / 20)

        #Moves The Ball
        x += xSpeed
        y += ySpeed

        #Revalues The Speed To Decrease It
        xSpeed = xSpeed * 0.98
        ySpeed = ySpeed * 0.98

        #Bouncing Rules For The Borders
        if x > 1184 or x < 16:
            xSpeed *= -1
        if y > 736 or y < 16:
            ySpeed *= -1

        #Checks If The Ball Is In The Hole
        if ((x - 650) ** 2 + (y - 650) ** 2) ** 0.5 < 25:
            xSpeed *= 0.97
            ySpeed *= 0.97
            if abs(ySpeed) < 0.1 and abs(xSpeed) < 0.1:
                toNext += 1

        #Draws the golf ball
        pygame.draw.circle(screen, (THECOLORS['white']), (round(x), round(y)), 15)

        #Adds Tarandeep To The Par Counter
        screen.blit(tarandeepSmall, (1050, 575))
        
        #Par Counter
        parCount = font.render(f'PAR   {strokes}', True, (THECOLORS["white"]), (0, 0, 0))
        screen.blit(parCount, (1070, 700))

        pygame.display.update()

#Level 2 Function
def level2():    
    #Default Speed
    xSpeed = 0
    ySpeed = 0
    
    #Default Position
    x = 75
    y = 600
    
    strokes = 0
    
    #Used To Move To The Next Level
    toNext = 0
    
    #While Loop To Close The Window And Move To The Next Level When toNext == 1
    while toNext == 0:
        screen.blit(bgImg, (0, 0))
        screen.blit(tarandeepSmall, (1020, 650))
        pygame.time.delay(10)

        #Hole Location
        pygame.draw.circle(screen, (255, 255, 255), (950, 550), 25)
        pygame.draw.circle(screen, (0, 0, 0), (950, 550), 24)

        #Hit The Ball When Clicked
        if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
            pygame.draw.line(screen, (0, 165, 0), (x, y), pygame.mouse.get_pos())
        for event in pygame.event.get():
            if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
                if event.type == pygame.MOUSEBUTTONUP:
                    xSpeed = -int((pygame.mouse.get_pos()[0] - x) / 20)
                    ySpeed = -int((pygame.mouse.get_pos()[1] - y) / 20)
                    strokes += 1
        #Vertical/Horizontal Speed
        x += xSpeed
        y += ySpeed
        xSpeed = xSpeed * 0.98
        ySpeed = ySpeed * 0.98

        #Sand
        sand1 = pygame.draw.rect(screen, (212, 176, 106), (400, 360, 100, 100))
        sand2 = pygame.draw.rect(screen, (212, 176, 106), (340, 420, 100, 100))
        sand3 = pygame.draw.rect(screen, (212, 176, 106), (750, 200, 100, 100))
        sand4 = pygame.draw.rect(screen, (212, 176, 106), (800, 250, 100, 100))
        sand5 = pygame.draw.rect(screen, (212, 176, 106), (950, 100, 100, 100))
        sand6 = pygame.draw.rect(screen, (212, 176, 106), (900, 50, 100, 100))

        #Collision Rules For Sand
        if sand1.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9
        if sand2.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9
        if sand3.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9
        if sand4.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9
        if sand5.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9
        if sand6.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9

        #Walls (x, y, length, width)
        wall1 = pygame.draw.rect(screen, (THECOLORS['grey']), (100, 100, 50, 600))
        wall2 = pygame.draw.rect(screen, (THECOLORS['grey']), (750, 375, 25, 375))

        #Collision Rules For Walls
        if wall1.collidepoint(x,y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)
        if wall2.collidepoint(x,y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)

        #Draws The Line Puller To Adjust Speed When Clicked
        if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
            pygame.draw.line(screen, (0, 0, 0), (x, y), pygame.mouse.get_pos())

        #Moves The Golf Ball When Clicked
        for event in pygame.event.get():
            if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
                if event.type == pygame.MOUSEBUTTONUP:
                    xSpeed = -int((pygame.mouse.get_pos()[0] - x) / 20)
                    ySpeed = -int((pygame.mouse.get_pos()[1] - y) / 20)
                    strokes += 1

        #Moves The Ball
        x += xSpeed
        y += ySpeed

        #Revalues The Speed To Decrease It
        xSpeed = xSpeed * 0.98
        ySpeed = ySpeed * 0.98

        #Bouncing Rules For The Borders
        if x > 1184 or x < 16:
            xSpeed *= -1
        if y > 736 or y < 16:
            ySpeed *= -1

        #Checks If The Ball Is In The Hole
        if ((x - 950) ** 2 + (y - 550) ** 2) ** 0.5 < 25:
            xSpeed *= 0.97
            ySpeed *= 0.97
            if abs(ySpeed) < 0.1 and abs(xSpeed) < 0.1:
                toNext += 1
        
        #Draws The Golf Ball
        pygame.draw.circle(screen, (255, 255, 255), (round(x), round(y)), 15)
        
        #Adds Tarandeep To The Par Counter
        screen.blit(tarandeepSmall, (1050, 575))
        
        #Par Counter
        parCount = font.render(f'PAR   {strokes}', True, (THECOLORS["white"]), (0, 0, 0))
        screen.blit(parCount, (1070, 700))

        pygame.display.update()

#Level 3 Function
def level3():
    #Default Speed
    xSpeed = 0
    ySpeed = 0

    #Default Position
    x = 75
    y = 700

    strokes = 0

    #Used To Move To The Next Level
    toNext = 0

    #While Loop To Close The Window And Move To The Next Level When toNext == 1
    while toNext == 0:
        screen.blit(bgImg, (0, 0))
        screen.blit(tarandeepSmall, (1020, 650))
        pygame.time.delay(10)

        #Hole Location
        pygame.draw.circle(screen, (255, 255, 255), (700, 700), 25)
        pygame.draw.circle(screen, (0, 0, 0), (700, 700), 24)

        #Hit The Ball When Clicked
        if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
            pygame.draw.line(screen, (0, 165, 0), (x, y), pygame.mouse.get_pos())
        for event in pygame.event.get():
            if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
                if event.type == pygame.MOUSEBUTTONUP:
                    xSpeed = -int((pygame.mouse.get_pos()[0] - x) / 20)
                    ySpeed = -int((pygame.mouse.get_pos()[1] - y) / 20)
                    strokes += 1
        #Vertical/Horizontal Speed
        x += xSpeed
        y += ySpeed
        xSpeed = xSpeed * 0.98
        ySpeed = ySpeed * 0.98

        #Sand
        sand1 = pygame.draw.rect(screen, (212, 176, 106), (1000, 100, 123, 123))
        sand2 = pygame.draw.rect(screen, (212, 176, 106), (950, 150, 123, 123))
        sand3 = pygame.draw.rect(screen, (212, 176, 106), (100, 100, 123, 123))
    
        #Collision Rules For Sand
        if sand1.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9
        if sand2.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9
        if sand3.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9

        #Water
        water = pygame.draw.rect(screen, (54, 84, 217), (150, 300, 225, 300))

        #Collision Rules For Water
        if water.collidepoint(x, y):
            x = 75
            xSpeed = 0
            y = 600
            ySpeed = 0

        #Walls (x, y, length, width)
        wall1 = pygame.draw.rect(screen, (THECOLORS['grey']), (450, 375, 50, 600))
        wall2 = pygame.draw.rect(screen, (THECOLORS['grey']), (950, 375, 50, 375))
        wall3 = pygame.draw.rect(screen, (THECOLORS['grey']), (375, 150, 500, 50))

        #Collision Rules For Walls
        if wall1.collidepoint(x,y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)
        if wall2.collidepoint(x,y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)
        if wall3.collidepoint(x,y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)

        #Draws The Line Puller To Adjust Speed When Clicked
        if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
            pygame.draw.line(screen, (0, 0, 0), (x, y), pygame.mouse.get_pos())

        #Moves The Golf Ball When Clicked
        for event in pygame.event.get():
            if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
                if event.type == pygame.MOUSEBUTTONUP:
                    xSpeed = -int((pygame.mouse.get_pos()[0] - x) / 20)
                    ySpeed = -int((pygame.mouse.get_pos()[1] - y) / 20)
                    strokes += 1

        #Moves The Ball
        x += xSpeed
        y += ySpeed

        #Revalues The Speed To Decrease It
        xSpeed = xSpeed * 0.98
        ySpeed = ySpeed * 0.98

        #Bouncing Rules For The Borders
        if x > 1184 or x < 16:
            xSpeed *= -1
        if y > 736 or y < 16:
            ySpeed *= -1

        #Checks If The Ball Is In The Hole
        if ((x - 700) ** 2 + (y - 700) ** 2) ** 0.5 < 25:
            xSpeed *= 0.97
            ySpeed *= 0.97
            if abs(ySpeed) < 0.1 and abs(xSpeed) < 0.1:
                toNext += 1

        #Draws The Golf Ball
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 15)

        #Adds Tarandeep To The Par Counter
        screen.blit(tarandeepSmall, (1050, 575))

        #Par Counter
        parCount = font.render(f'PAR   {strokes}', True, (THECOLORS["white"]), (0, 0, 0))
        screen.blit(parCount, (1070, 700))

        pygame.display.update()

#Level 4 Function
def level4():
    #Default Speed
    xSpeed = 0
    ySpeed = 0

    #Default Position
    x = 120
    y = 600

    strokes = 0

    #Used To Move To The Next Level
    toNext = 0

    #While Loop To Close The Window And Move To The Next Level When toNext == 1
    while toNext == 0:
        screen.blit(bgImg, (0, 0))
        pygame.time.delay(10)

        #Hole Location
        pygame.draw.circle(screen, (255, 255, 255), (925, 700), 25)
        pygame.draw.circle(screen, (0, 0, 0), (925, 700), 24)

        #Hit The Ball When Clicked
        if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
            pygame.draw.line(screen, (0, 165, 0), (x, y), pygame.mouse.get_pos())
        for event in pygame.event.get():
            if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
                if event.type == pygame.MOUSEBUTTONUP:
                    xSpeed = -int((pygame.mouse.get_pos()[0] - x) / 20)
                    ySpeed = -int((pygame.mouse.get_pos()[1] - y) / 20)
                    strokes += 1
        #Vertical/Horizontal Speed
        x += xSpeed
        y += ySpeed
        xSpeed = xSpeed * 0.98
        ySpeed = ySpeed * 0.98

        #Sand
        sand1 = pygame.draw.rect(screen, (212, 176, 106), (100, 100, 123, 123))
        sand2 = pygame.draw.rect(screen, (212, 176, 106), (150, 150, 123, 123))
        sand3 = pygame.draw.rect(screen, (212, 176, 106), (200, 200, 123, 123))
        sand4 = pygame.draw.rect(screen, (212, 176, 106), (250, 250, 123, 123))

        #Collision Rules For Sand
        if sand1.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9
        if sand2.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9
        if sand3.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9
        if sand4.collidepoint(x, y):
            xSpeed *= 0.9
            ySpeed *= 0.9

        #Water
        water1 = pygame.draw.rect(screen, (54, 84, 217), (900, 50, 250, 100))
        water2 = pygame.draw.rect(screen, (54, 84, 217), (450, 450, 150, 200))
        water3 = pygame.draw.rect(screen, (54, 84, 217), (0, 300, 50, 500))

        #Collision Rules For Water
        if water1.collidepoint(x, y):
            x = 120
            xSpeed = 0
            y = 600
            ySpeed = 0
        if water2.collidepoint(x, y):
            x = 120
            xSpeed = 0
            y = 600
            ySpeed = 0
        if water3.collidepoint(x, y):
            x = 120
            xSpeed = 0
            y = 600
            ySpeed = 0

        #Walls (x, y, length, width)
        wall1 = pygame.draw.rect(screen, (THECOLORS['grey']), (750, 375, 50, 600))
        wall2 = pygame.draw.rect(screen, (THECOLORS['grey']), (1050, 375, 50, 375))
        wall3 = pygame.draw.rect(screen, (THECOLORS['grey']), (800, 200, 500, 45))

        #Collision Rules For Walls
        if wall1.collidepoint(x,y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)
        if wall2.collidepoint(x,y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)
        if wall3.collidepoint(x,y):
            xSpeed = -1 * abs(xSpeed)
            ySpeed = -1 * abs(ySpeed)

        #Draws The Line Puller To Adjust Speed When Clicked
        if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
            pygame.draw.line(screen, (0, 0, 0), (x, y), pygame.mouse.get_pos())

        #Moves The Golf Ball When Clicked
        for event in pygame.event.get():
            if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
                if event.type == pygame.MOUSEBUTTONUP:
                    xSpeed = -int((pygame.mouse.get_pos()[0] - x) / 20)
                    ySpeed = -int((pygame.mouse.get_pos()[1] - y) / 20)
                    strokes += 1

        #Moves The Ball
        x += xSpeed
        y += ySpeed

        #Revalues The Speed To Decrease It
        xSpeed = xSpeed * 0.98
        ySpeed = ySpeed * 0.98

        #Bouncing Rules For The Borders
        if x > 1184 or x < 16:
            xSpeed *= -1
        if y > 736 or y < 16:
            ySpeed *= -1

        #Checks If The Ball Is In The Hole
        if ((x - 925) ** 2 + (y - 700) ** 2) ** 0.5 < 25:
            xSpeed *= 0.97
            ySpeed *= 0.97
            if abs(ySpeed) < 0.1 and abs(xSpeed) < 0.1:
                toNext += 1

        #Draws The Golf Ball
        pygame.draw.circle(screen, (255, 255, 255), (round(x), round(y)), 15)

        #Adds Tarandeep To The Par Counter
        screen.blit(tarandeepSmall, (1050, 575))

        #Par Counter
        parCount = font.render(f'PAR   {strokes}', True, (THECOLORS["white"]), (0, 0, 0))
        screen.blit(parCount, (1070, 700))

        pygame.display.update()

#Level 5 Function
def level5():
    #Default Speed
    xSpeed = 0
    ySpeed = 0

    #Default Position
    x = 625
    y = 650

    strokes = 0

    #Used To Move To The Next Level
    toNext = 0

    #While Loop To Close The Window And Move To The Next Level When toNext == 1
    while toNext == 0:
        screen.blit(bgImg, (0, 0))
        pygame.time.delay(10)

        #Hole Location
        pygame.draw.circle(screen, (255, 255, 255), (120, 115), 25)
        pygame.draw.circle(screen, (0, 0, 0), (120, 115), 24)

        #Hit The Ball When Clicked
        if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
            pygame.draw.line(screen, (0, 165, 0), (x, y), pygame.mouse.get_pos())
        for event in pygame.event.get():
            if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
                if event.type == pygame.MOUSEBUTTONUP:
                    xSpeed = -int((pygame.mouse.get_pos()[0] - x) / 20)
                    ySpeed = -int((pygame.mouse.get_pos()[1] - y) / 20)
                    strokes += 1
        #Vertical/Horizontal Speed
        x += xSpeed
        y += ySpeed
        xSpeed = xSpeed * 0.98
        ySpeed = ySpeed * 0.98
        
        #Water
        water1 = pygame.draw.rect(screen, (54, 84, 217), (0, 0, 1200, 58))
        water2 = pygame.draw.rect(screen, (54, 84, 217), (900, 0, 300, 750))
        water3 = pygame.draw.rect(screen, (54, 84, 217), (0, 174, 800, 100))
        water4 = pygame.draw.rect(screen, (54, 84, 217), (0, 174, 300, 600))
        water5 = pygame.draw.rect(screen, (54, 84, 217), (300, 600, 250, 500))
        water6 = pygame.draw.rect(screen, (54, 84, 217), (700, 400, 300, 400))
        water7 = pygame.draw.rect(screen, (54, 84, 217), (380, 350, 280, 170))
        water8 = pygame.draw.rect(screen, (54, 84, 217), (0, 50, 50, 170))

        #Collision Rules For Water
        if water1.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0
        if water2.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0
        if water3.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0
        if water4.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0
        if water5.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0
        if water6.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0
        if water7.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0
        if water8.collidepoint(x, y):
            x = 625
            xSpeed = 0
            y = 650
            ySpeed = 0
    
        #Draws The Line Puller To Adjust Speed When Clicked
        if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
            pygame.draw.line(screen, (0, 0, 0), (x, y), pygame.mouse.get_pos())

        #Moves The Golf Ball When Clicked
        for event in pygame.event.get():
            if abs(xSpeed) < 0.1 and abs(ySpeed) < 0.1:
                if event.type == pygame.MOUSEBUTTONUP:
                    xSpeed = -int((pygame.mouse.get_pos()[0] - x) / 20)
                    ySpeed = -int((pygame.mouse.get_pos()[1] - y) / 20)
                    strokes += 1

        #Moves The Ball
        x += xSpeed
        y += ySpeed

        #Revalues The Speed To Decrease It
        xSpeed = xSpeed * 0.98
        ySpeed = ySpeed * 0.98

        #Bouncing Rules For The Borders
        if x > 1184 or x < 16:
            xSpeed *= -1
        if y > 736 or y < 16:
            ySpeed *= -1

        #Checks If The Ball Is In The Hole
        if ((x - 120) ** 2 + (y - 115) ** 2) ** 0.5 < 25:
            xSpeed *= 0.97
            ySpeed *= 0.97
            if abs(ySpeed) < 0.1 and abs(xSpeed) < 0.1:
                toNext += 1

        #Draws The Golf Ball
        pygame.draw.circle(screen, (255, 255, 255), (round(x), round(y)), 15)

        #Adds Tarandeep To The Par Counter
        screen.blit(tarandeepSmall, (1050, 575))
        
        #Par Counter
        parCount = font.render(f'PAR   {strokes}', True, (THECOLORS["white"]), (0, 0, 0))
        screen.blit(parCount, (1070, 700))

        pygame.display.update()

#Call Function
main()