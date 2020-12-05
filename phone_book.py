# -*- coding: utf-8 -*-
"""
Created on 

"""

names = ["Eva", "Sasha Oganezov", "Sasha Noel", "Alper", "Boris", "Felix", "Maxim", "Rodion","Yaroslav"]
phones = ["(514)413-1342", "(438)232-4343", "(514)324-2333","(450)234-6934","(514)234-5693", "(450)234-8855", "(514)886-2342", "(438)394-2342", "(514)234-8785"]
addresses=["6817 43 Ave","7503 Rue St Denis", "251 Av Percival", "7766 George Street", "11727 Rue Notre Dame E", "5745 17 Ave", "3708 Rue St Hubert", "800 Rue Gagne", "4430 Ste Catherine Street O"]

name = input("Please enter the name? ") 

for i in range(0, len(names)):
    if names[i] == name:
        print("The phone of ", name, " is ", phones[i])
        print("The address of ", name, " is ", addresses[i])
        
ind = names.index(name)
print("The phone using index is ", phones[ind])
print("The address using index is ", addresses[ind])

phoneBook = {"Eva" : ["(514)413-1342", "6817 43 Ave"], "Sasha Oganezov": ["(438)232-4343", "7503 Rue St Denis"],\
             "Sasha Noel": ["(514)324-2333", "251 Av Percival"], "Alper": ["(450)234-6934", "7766 George Street"]}

print(phoneBook[name])
phoneBook["Boris"] = ["(514)234-5693", "11727 Rue Notre Dame E"]
print(phoneBook)