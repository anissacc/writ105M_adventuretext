import pygame
import sys

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont('Arial', 30)
objects = []

class Character:
    # creating a playable character

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)