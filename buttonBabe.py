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

class Button():
    def __init__(self, x, y, width, height, buttonText = 'Button', normalColor = '#ffffff', 
                 hoverColor='#666666', pressedColor='#333333', onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onepress = onePress
        self.alreadyPressed = False
        self.fillColors = {'normal': normalColor, 'hover': hoverColor, 'pressed': pressedColor}
        # creating surface for rectangle to be in
        self.buttonSurface = pygame.Surface((self.width, self.height))
        # creating rectangle
        self.buttonRect = pygame.Rect(x, y, width, height)
        # creating and rendering font of button
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        objects.append(self)
    
    # checking interaction with button and changing to appropriate color
    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons = 3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if not self.alreadyPressed:
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        # displaying button onto screen visually
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

    # checking interaction with button for functionality
    def checkInput(self, position):
        if position[0] in range(self.buttonRect.left, self.buttonRect.right) and position[1] in range(self.buttonRect.top, self.buttonRect.bottom):
            return True
        else:
            return False
