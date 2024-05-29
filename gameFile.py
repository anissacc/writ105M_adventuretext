import os
import sys

import pygame

from buttonBabe import Button
from spriteClass import chara

pygame.init()
pygame.font.init()
height = 650
width = 1000
gameScreen = pygame.display.set_mode((width, height), 0)
aFont = pygame.font.SysFont('Arial', 30)

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
        writeText('You\'re a UCSB student and a NERD. Fix that by partying as HARD AS YOU CAN!', 0, 800)
        
        # player.update()
        pygame.display.update()