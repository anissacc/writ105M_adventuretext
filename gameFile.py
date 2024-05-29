import os
import sys

import pygame
# import pygame_gui
import pygame_textinput
from buttonBabe import Button
from spriteClass import chara

pygame.init()
pygame.font.init()
screenHeight = 650
screenWidth = 1000
screen = pygame.display.set_mode((screenWidth, screenHeight), 0)
aFont = pygame.font.SysFont('Arial', 30)

def leaveTheGame():
    pygame.quit()
    sys.exit()

def writeText(message, x, y, color = 'white'):
    font = pygame.font.SysFont('Arial', 50)
    text = font.render(message, True, color)
    screen.blit(text, (x, y))

def partyScene():
    playerImage = 'slimeWalk1.png'
    player = chara(playerImage)
    while True:
        screen.fill('black')
        writeText('You\'re a UCSB student and a NERD. Fix that by partying as HARD AS YOU CAN!', 0, 800)
        
        # player.update()
        pygame.display.update()