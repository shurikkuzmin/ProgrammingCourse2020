# -*- coding: utf-8 -*-
"""
Created on 

"""

number = int(input("Give me the number? "))

isPrime = True
for i in range(2, number):
    if number % i == 0:
        isPrime = False
        print("Number ", number, " is not prime!")
        break
    
if isPrime:
    print("Number ", number, " is prime!")
