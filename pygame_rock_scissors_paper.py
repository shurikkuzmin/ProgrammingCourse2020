# -*- coding: utf-8 -*-
"""
Created on 

"""

import pygame
from pygame.locals import *
import random

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
textRect = text.get_rect()
textRect.left = 50
textRect.top = 50

mainImage = pygame.image.load("rock_scissors_paper.png")
scissors = mainImage.subsurface((0, 0, 1060, 750))
scissors = pygame.transform.scale(scissors, (300, 200))
scissorsRect = scissors.get_rect()
scissorsRect.left = 50
scissorsRect.top = 100

rock = mainImage.subsurface((1600, 300, 2400-1600, 1000-300))
rock = pygame.transform.scale(rock, (300, 200))
rockRect = rock.get_rect()
rockRect.left = 50
rockRect.top = 300

paper = mainImage.subsurface((380, 1030, 1420-380, 1959-1030))
paper = pygame.transform.scale(paper, (300,250))
paperRect = paper.get_rect()
paperRect.left = 50
paperRect.top = 500

computerChoice = random.choice(("paper", "scissors", "rock"))
#myChoice = input("Please choose your entity between paper, rock and scissors? ")
#print("Computer choice: ", computerChoice)
#print("My choice: ", myChoice)

#if computerChoice == myChoice:
#    print("Tie!")
#elif computerChoice == "rock" and myChoice == "paper":
#    print("You won!")
#elif computerChoice == "paper" and myChoice == "scissors":
#    print("You won!")
#elif computerChoice == "scissors" and myChoice == "rock":
#    print("You won!")
#else:
#    print("You lost!")

isRunning = True
while isRunning:
    SURFACE.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                isRunning = False
        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if scissorsRect.collidepoint(x, y):
                myChoice = "scissors"
                isRunning = False
            elif rockRect.collidepoint(x,y):
                myChoice = "rock"
                isRunning = False
            elif paperRect.collidepoint(x,y):
                myChoice = "paper"
                isRunning = False
         
    SURFACE.blit(text, textRect)
    SURFACE.blit(scissors, scissorsRect)
    SURFACE.blit(rock, rockRect)
    SURFACE.blit(paper, paperRect)
    pygame.display.update()
    
pygame.quit()
