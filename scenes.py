import os
import sys

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

screen = pygame.display.set_mode((screenWidth, screenHeight), 0)
theFont = pygame.font.SysFont('Arial', 30)

def leaveTheGame():
    pygame.quit()
    sys.exit()

def firstScene():
    firstSceneBg = pygame.image.load('bedroom.png')
    while True:
        screen.fill('black')
        screen.blit(firstSceneBg, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leaveTheGame()

        pygame.display.update()   