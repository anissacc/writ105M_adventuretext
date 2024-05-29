import os
import sys

import pygame

pygame.init()
screenHeight = 650
screenWidth = 1000
screen = pygame.display.set_mode((screenWidth, screenHeight), 0)
fps = 40 # frame rate

class chara(pygame.sprite.Sprite):
    def __init__(self, image, width = 150, height = 150):
        self.image = pygame.image.load(image)
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        # return self.rect.center