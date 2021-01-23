# -*- coding: utf-8 -*-
"""
Created on 

"""

import pygame
from pygame.locals import *

pygame.init()

SURFACE = pygame.display.set_mode((400,800), 0, 32)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

myfont = pygame.font.SysFont("Comic Sans MS", 30)
text = myfont.render("What is your choice?", False, BLUE)

isRunning = True
while isRunning:
    SURFACE.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False
         
    SURFACE.blit(text, (50,50))
    pygame.display.update()
    
pygame.quit()
