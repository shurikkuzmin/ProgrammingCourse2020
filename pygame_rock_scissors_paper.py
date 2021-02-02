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

mainImage = pygame.image.load("rock_scissors_paper.png")
scissors = mainImage.subsurface((0, 0, 1060, 750))
scissors = pygame.transform.scale(scissors, (300, 200))
rock = mainImage.subsurface((1600, 300, 2400-1600, 1000-300))
rock = pygame.transform.scale(rock, (300, 200))
paper = mainImage.subsurface((380, 1030, 1420-380, 1959-1030))
paper = pygame.transform.scale(paper, (300,250))

isRunning = True
while isRunning:
    SURFACE.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                isRunning = False
         
    SURFACE.blit(text, (50,50))
    SURFACE.blit(scissors, (50,100))
    SURFACE.blit(rock, (50,300))
    SURFACE.blit(paper, (50,500))
    pygame.display.update()
    
pygame.quit()
