# -*- coding: utf-8 -*-
"""
Created on 

"""
import random

computerChoice = random.choice(("paper", "scissors", "rock"))
myChoice = input("Please choose your entity between paper, rock and scissors? ")
print("Computer choice: ", computerChoice)
print("My choice: ", myChoice)

if computerChoice == myChoice:
    print("Tie!")
elif computerChoice == "rock" and myChoice == "paper":
    print("You won!")
elif computerChoice == "paper" and myChoice == "scissors":
    print("You won!")
elif computerChoice == "scissors" and myChoice == "rock":
    print("You won!")
else:
    print("You lost!")