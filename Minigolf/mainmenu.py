# Omercan, Abhishek
# June 17 2022
# ISC2O1 Culminating
# Mini Golf Main Menu
import pygame
from button import Button
import sys

#Initialization
pygame.init()

#Screen Resolution
screen = pygame.display.set_mode((1280, 720))

#Title Bar
pygame.display.set_caption("Tarandeep's Golf Course!")

def getFont(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

#When the Play Button is Clicked
def play():
    while True:
        playMousePos = pygame.mouse.get_pos()
        #Runs the main program with levels
        import main
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

#Main Menu Appearance
def main_Menu():
    while True:
        #Background - change the file paths to the new location when downloading it
        bg = pygame.image.load("assets/menuBackground.png")
        tarandeep = pygame.image.load('assets/tarandeep.png')   #Base Photo of Tarandeep
        tarandeepSmall = pygame.transform.scale(tarandeep, (475, 500))  #Modified Size of Tarandeep
        screen.blit(bg, (0, 0))
        screen.blit(tarandeepSmall, (0, 250))

        menuMousePos = pygame.mouse.get_pos()

        #Title Text Size
        menuTxt = getFont(55).render("TARANDEEP'S GOLF COURSE", True, "#d7fcd4")
        menuRect = menuTxt.get_rect(center = (640, 100))

        #Appearance For Play Button
        playButton = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 300), 
                            textInput = "PLAY", font = getFont(75), baseColor = "#d7fcd4", hoveringColor = "White")
        #Appearance For Quit Button
        quitButton = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 450), 
                            textInput = "QUIT", font = getFont(75), baseColor = "#d7fcd4", hoveringColor = "White")

        screen.blit(menuTxt, menuRect)

        for button in [playButton, quitButton]:
            button.changeColor(menuMousePos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #If Play Button is Pressed, Runs the play script
                if playButton.checkForInput(menuMousePos):
                    play()
                #If Quit is Pressed, Window Closes
                if quitButton.checkForInput(menuMousePos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
#Call Function
main_Menu()