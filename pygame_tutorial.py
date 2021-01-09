# -*- coding: utf-8 -*-
"""
Created on 

"""

import pygame
from pygame.locals import *

pygame.init()

SURFACE = pygame.display.set_mode((800,600))

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

isRunning = True
x = 300
while isRunning:
    SURFACE.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x = x - 25
            
    #pygame.draw.rect(SURFACE, RED, pygame.Rect(100, 50, 20, 60))
    pygame.draw.rect(SURFACE, GREEN, pygame.Rect(x, 200, 50, 50), 10)
    #pygame.draw.circle(SURFACE, BLUE, (500, 500), 30)
    #pygame.draw.line(SURFACE, WHITE, (100,100), (200,200), 5)
         
    pygame.display.update()
    
pygame.quit()