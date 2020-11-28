# -*- coding: utf-8 -*-
"""
Created on 

"""

import random
computerNumber = random.randint(1, 100)
myNumber = int(input("Enter your number? "))

while computerNumber != myNumber:
    if computerNumber > myNumber:
        print("Computer number is larger")
    else:
        print("Computer number is smaller")
    
    myNumber = int(input("Enter your number? "))
    


print("You guessed it!")