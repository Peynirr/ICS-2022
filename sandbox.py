import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
 
def drawCircle(screen, x, y):
   #Circle
   pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

pygame.init()

#Size of screen 
size = [700, 600]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Ex 37 - Pygame Keyboard Input Demo")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 300
y_coord = 350
 
# -------- Main Program Loop -----------
while not done:
   # --- Event Processing
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         done = True
         

      elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
         if event.key == pygame.K_LEFT:
            x_speed = -2
            break
         elif event.key == pygame.K_RIGHT:
            x_speed = 2
            break
         elif event.key == pygame.K_UP:
            y_speed = -2
            break
         elif event.key == pygame.K_DOWN:
            y_speed = 2
            break
 
        # User let up on a key
         elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
                break
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
                break
 
 
   #Move the object according to the speed set.
   x_coord = x_coord + x_speed
   y_coord = y_coord + y_speed

   screen.fill(WHITE)
 
   drawCircle(screen, x_coord, y_coord)

   pygame.display.flip()
   
   clock.tick(120)

pygame.quit()