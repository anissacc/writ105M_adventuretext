import pygame
import sys

pygame.init()
width = 1000
height = 650
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont('Arial', 30)

class Slime(pygame.sprite.Sprite):
    def __init__(self, picture):
        pygame.sprite.Sprite.__init__(self)
        self.picture = picture
        self.screen = pygame.display.get_surface()
        self.area = screen.get_rect()

