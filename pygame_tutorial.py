# -*- coding: utf-8 -*-
"""
Created on 

"""

import pygame
from pygame.locals import *

pygame.init()

SURFACE = pygame.display.set_mode((800,600), 0, 32)

ded_moroz = pygame.image.load("ded_moroz.png")
ded_moroz = pygame.transform.scale(ded_moroz, (100, 100))

miami = pygame.image.load("miami.jpg")
miami = pygame.transform.scale(miami, (800,600))

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

isRunning = True
x = 300
y = 200
while isRunning:
    SURFACE.fill(BLACK)
    SURFACE.blit(miami,(0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x = x - 25
            if event.key == K_RIGHT:
                x = x + 25
            if event.key == K_UP:
                y = y - 25
            if event.key == K_DOWN:
                y = y + 25
    #pygame.draw.rect(SURFACE, RED, pygame.Rect(100, 50, 20, 60))
    #pygame.draw.rect(SURFACE, GREEN, pygame.Rect(x, y, 50, 50), 10)
    SURFACE.blit(ded_moroz,(x, y))
    #pygame.draw.circle(SURFACE, BLUE, (500, 500), 30)
    #pygame.draw.line(SURFACE, WHITE, (100,100), (200,200), 5)
         
    pygame.display.update()
    
pygame.quit()
