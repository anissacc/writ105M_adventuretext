import os
import sys

import pygame
# import pygame_gui
# import pygame_textinput
from buttonBabe import Button
from spriteClass import chara

def leaveTheGame():
    pygame.quit()
    sys.exit()

def partyScene():
    playerImage = 'slimeWalk1.png'
    player = chara(playerImage)
    while True:
        player.update()