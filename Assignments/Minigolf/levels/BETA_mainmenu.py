# Omercan
# June 6 2022
# ISC2O1 Culminating
# Mini Golf Main Menu
import pygame, sys
from button import Button
import time

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Tarandeep's Golf Course!")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

#When the Play Button is Clicked
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        #Runs the main program with levels
        import main
        SCREEN.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")
        image = pygame.image.load("assets/tarandeep.png")
        imageSmall = pygame.transform.scale(image, (500, 500))
        OPTIONS_TEXT = get_font(45).render("Options (Difficulty, etc.)", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(imageSmall, (4, 0))

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

#Main Menu Appearance
def main_menu():
    while True:
        #Background
        BG = pygame.image.load("assets/menuBackground.png")
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #Title Text Size
        MENU_TEXT = get_font(55).render("TARANDEEP'S GOLF COURSE", True, "#d7fcd4")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        #Appearance For Play Button
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 300), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="CREDITS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        #Appearance For Quit Button
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 450), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #If Play Button is Pressed, Runs the play script
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                #If Quit is Pressed, Window Closes
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
#Call Function
main_menu()