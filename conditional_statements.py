# -*- coding: utf-8 -*-
"""
Created on 

"""

age = int(input("What is your age? "))

#0..2 - baby
#3..5 - child 
#6..12 - youngster
#13..19 - teenager
#20..60 - adult
#>60 - senior

if age <= 2:
    print("You are a baby!")
elif age <= 5:
    print("You are a child!")
elif age <= 12:
    print("You are a youngster!")
elif age <= 19:
    print("You are a teenager!")
elif age <= 60:
    print("You are an adult!")
else:
    print("You are a senior!")