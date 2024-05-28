import os
import sys
# testing if git pull request works
import pygame
# import pygame_gui
# import pygame_textinput
from buttonBabe import Button

# from pygame_gui.ui_manager import UIManager
# from pygame_gui.elements.ui_text_box import UITextBox

# initializing + defining global variables
pygame.init()
pygame.font.init()
screenHeight = 650
screenWidth = 1000
# guiManager = pygame_gui.UIManager((screenWidth, screenHeight))
screen = pygame.display.set_mode((screenWidth, screenHeight), 0)
theFont = pygame.font.SysFont('Arial', 30)
fps = 40 # frame rate
ani = 4 # animation cycles

def leaveTheGame():
    pygame.quit()
    sys.exit()

def main_menu():
    menuBG = pygame.image.load('mainMenuBG.png')
    while True:
        screen.fill('black')
        screen.blit(menuBG, (0, 0))

        newGameButt = Button(390, 445, 150, 50, 'New Game', '#a8e61d', '#afe06e', '#89a823')
        continueButt = Button(145, 445, 150, 50, 'Continue', '#a8e61d', '#afe06e', '#89a823')
        quitButt = Button(265, 545, 150, 50, 'Quit', '#a8e61d', '#afe06e', '#89a823')

        for button in [newGameButt, continueButt, quitButt]:
            button.process()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leaveTheGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosMain = pygame.mouse.get_pos()
                if quitButt.checkInput(mousePosMain):
                    leaveTheGame()

        pygame.display.update()

main_menu()