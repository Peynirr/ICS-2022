import pygame
import time 
# Generic importing.
# Initalizes Pygame and sets the window up
pygame.init()
wn = pygame.display.set_mode((1200, 750))

# Starting position, strokes and speed.
xspeed = 0
yspeed = 0
x = 500
y = 500
strokes = 0
lwalls = [(150, 0, 10, 300), (400, 300, 10, 50)]
rwalls = [(250, 0, 10, 300), (500, 300, 10, 50)]
twalls = [(150, 300, 100, 10), (400, 300, 100, 10)]
bwalls = [(150, 0, 100, 10), (400, 350, 100, 10)]
font = pygame.font.Font('BRLNSB.TTF', 30)
toNext = 0


while toNext == 0:
    wn.fill((124, 252, 0))
    pygame.time.delay(10)

    pygame.draw.circle(wn, (255, 255, 255), (100, 100), 25)
    pygame.draw.circle(wn, (0, 0, 0), (100, 100), 24)

    # Drawing sand
    sandbox = pygame.draw.rect(wn, (212, 176, 106), (234,345,123,123))
    # Behavior:
    if sandbox.collidepoint(x, y):
        xspeed *= 0.9
        yspeed *= 0.9
 
    water = pygame.draw.rect(wn, (54, 84, 217), (0, 200, 50, 300))
    # Behavior:
    if water.collidepoint(x, y):
        x = 500
        xspeed = 0
        y = 500
        yspeed = 0

    for wall in lwalls:
        wall = pygame.draw.rect(wn, (111, 111, 111), wall)
        # Behavior:
        if wall.collidepoint(x, y):
            xspeed = -1 * abs(xspeed)

    for wall in rwalls:
        wall = pygame.draw.rect(wn, (111, 111, 111), wall)
        # Behavior:
        if wall.collidepoint(x, y):
            xspeed = abs(xspeed)

    for wall in twalls:
        wall = pygame.draw.rect(wn, (111, 111, 111), wall)
        # Behavior:
        if wall.collidepoint(x, y):
            yspeed = -1 * abs(yspeed)

    for wall in bwalls:
        wall = pygame.draw.rect(wn, (111, 111, 111), wall)
        # Behavior:
        if wall.collidepoint(x, y):
            yspeed = abs(yspeed)

    pygame.draw.circle(wn, (255, 255, 255), (round(x), round(y)), 15)

    # Only draw line when stopped
    if abs(xspeed) < 0.1 and abs(yspeed) < 0.1:
        pygame.draw.line(wn, (0, 165, 0), (x, y), pygame.mouse.get_pos())

    # Hit the ball on click
    for event in pygame.event.get():
        if abs(xspeed) < 0.1 and abs(yspeed) < 0.1:
            if event.type == pygame.MOUSEBUTTONUP:
                xspeed = -int((pygame.mouse.get_pos()[0] - x) / 20)
                yspeed = -int((pygame.mouse.get_pos()[1] - y) / 20)
                strokes += 1
           

    # Move the ball
    x += xspeed
    y += yspeed

    # Deceleration
    xspeed = xspeed * 0.98
    yspeed = yspeed * 0.98

    # Bouncing
    if x > 584 or x < 16:
        xspeed *= -1
    if y > 584 or y < 16:
        yspeed *= -1

    # Checks to see if in hole
    if ((x - 100) ** 2 + (y - 100) ** 2) ** 0.5 < 25:
        xspeed *= 0.97
        yspeed *= 0.97
        if abs(yspeed) < 0.1 and abs(xspeed) < 0.1:
            winmsg = font.render(f'Nice! {strokes} strokes!', True, (255, 255, 255), (24, 110, 47))
            wn.blit(winmsg, (150, 400))
            x = 500
            xspeed = 0
            y = 500
            yspeed = 0
            toNext += 1
            


    pygame.display.update()





while toNext == 1:
    wn.fill((0, 252, 0))
    pygame.time.delay(10)

    pygame.draw.circle(wn, (255, 255, 255), (100, 100), 25)
    pygame.draw.circle(wn, (0, 0, 0), (100, 100), 24)

    # Drawing sand
    sandbox = pygame.draw.rect(wn, (212, 176, 106), (234,345,123,123))
    # Behavior:
    if sandbox.collidepoint(x, y):
        xspeed *= 0.9
        yspeed *= 0.9
 
    water = pygame.draw.rect(wn, (54, 84, 217), (0, 200, 50, 300))
    # Behavior:
    if water.collidepoint(x, y):
        x = 500
        xspeed = 0
        y = 500
        yspeed = 0

    for wall in lwalls:
        wall = pygame.draw.rect(wn, (111, 111, 111), wall)
        # Behavior:
        if wall.collidepoint(x, y):
            xspeed = -1 * abs(xspeed)

    for wall in rwalls:
        wall = pygame.draw.rect(wn, (111, 111, 111), wall)
        # Behavior:
        if wall.collidepoint(x, y):
            xspeed = abs(xspeed)

    for wall in twalls:
        wall = pygame.draw.rect(wn, (111, 111, 111), wall)
        # Behavior:
        if wall.collidepoint(x, y):
            yspeed = -1 * abs(yspeed)

    for wall in bwalls:
        wall = pygame.draw.rect(wn, (111, 111, 111), wall)
        # Behavior:
        if wall.collidepoint(x, y):
            yspeed = abs(yspeed)

    pygame.draw.circle(wn, (255, 255, 255), (round(x), round(y)), 15)

    # Only draw line when stopped
    if abs(xspeed) < 0.1 and abs(yspeed) < 0.1:
        pygame.draw.line(wn, (0, 165, 0), (x, y), pygame.mouse.get_pos())

    # Hit the ball on click
    for event in pygame.event.get():
        if abs(xspeed) < 0.1 and abs(yspeed) < 0.1:
            if event.type == pygame.MOUSEBUTTONUP:
                xspeed = -int((pygame.mouse.get_pos()[0] - x) / 20)
                yspeed = -int((pygame.mouse.get_pos()[1] - y) / 20)
                strokes += 1
           

    # Move the ball
    x += xspeed
    y += yspeed

    # Deceleration
    xspeed = xspeed * 0.98
    yspeed = yspeed * 0.98

    # Bouncing
    if x > 584 or x < 16:
        xspeed *= -1
    if y > 584 or y < 16:
        yspeed *= -1

    # Checks to see if in hole
    if ((x - 100) ** 2 + (y - 100) ** 2) ** 0.5 < 25:
        xspeed *= 0.97
        yspeed *= 0.97
        if abs(yspeed) < 0.1 and abs(xspeed) < 0.1:
            winmsg = font.render(f'Nice! {strokes} strokes!', True, (255, 255, 255), (24, 110, 47))
            wn.blit(winmsg, (150, 400))
            x = 500
            xspeed = 0
            y = 500
            yspeed = 0
            toNext += 1
            


    pygame.display.update()