import os
import sys

import pygame
import pygame_gui
from pygame_gui.ui_manager import UIManager
from pygame_gui.elements.ui_text_box import UITextBox

from buttonBabe import Button
from spriteClass import chara

pygame.init()
pygame.font.init()
height = 650
width = 1000
gameScreen = pygame.display.set_mode((width, height), 0)
aFont = pygame.font.SysFont('Arial', 30)
guiManager = pygame_gui.UIManager((width,height))

def leaveTheGame():
    pygame.quit()
    sys.exit()

def writeText(message, x, y, color = (255, 255, 255)):
    font = pygame.font.SysFont('Arial', 50)
    text = font.render(message, True, color)
    gameScreen.blit(text, (x, y))

def partyScene():
    # playerImage = 'slimeWalk1.png'
    # player = chara(playerImage)
    while True:
        gameScreen.fill('black')
        UITextBox('<font size=30>Directions:<br>'
                  'You\'re a UCSB student and a NERD'
                  '\nFix that by partying as HARD AS YOU CAN!', 
                  pygame.Rect(10, 10, 800, 350),
                  manager = guiManager, object_id='#text_box_1')
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leaveTheGame()

            guiManager.process_events(event)
        
        guiManager.update()
        
        # player.update()
        pygame.display.update()