import os
import sys
import pygame
# import pygame_gui
# import pygame_textinput
from buttonBabe import Button
from spriteClass import Slime

# from pygame_gui.ui_manager import UIManager
# from pygame_gui.elements.ui_text_box import UITextBox

# initializing + defining global variables
pygame.init()
pygame.font.init()
screenHeight = 650
screenWidth = 1000
# fps = 40 # frame rate
# ani = 4 # animation cycles
# clock = pygame.time.Clock()
# guiManager = pygame_gui.UIManager((screenWidth, screenHeight))
screen = pygame.display.set_mode((screenWidth, screenHeight), 0)
theFont = pygame.font.SysFont('Arial', 30)

icon = pygame.image.load('slimeWalk1.png')
slimer = Slime(icon)

slimer.area.x = 0
slimer.area.y = 0

player_list = pygame.sprite.Group()
player_list.add(slimer)


def leaveTheGame():
    pygame.quit()
    sys.exit()

def firstScene():
    firstSceneBg = pygame.image.load('bedroom.png')
    '''
    slimeWalk = [pygame.image.load('slimeWalk1.png'), pygame.image.load('slimeWalk2.png'), pygame.image.load('slimeWalk3.png'), pygame.image.load('slimeWalk4.png')]
    slimeLeft = [pygame.image.load('slimeLeft1.png'), pygame.image.load('slimeLeft2.png'), pygame.image.load('slimeLeft3.png'), pygame.image.load('slimeLeft4.png')]
    slimeRight = [pygame.image.load('slimeRight1.png'), pygame.image.load('slimeRight2.png'), pygame.image.load('slimeRight3.png'), pygame.image.load('slimeRight4.png')]
    slimeBack = [pygame.image.load('slimeBack1.png'), pygame.image.load('slimeBack2.png'), pygame.image.load('slimeBack3.png'), pygame.image.load('slimeBack4.png')]
    
    slimeStates = [slimeWalk, slimeLeft, slimeRight, slimeBack]
    '''
    while True:
        screen.fill('black')
        screen.blit(firstSceneBg, (0,0))
        player_list.draw(screen)
    
        # clock.tick(40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leaveTheGame()


        pygame.display.update()   