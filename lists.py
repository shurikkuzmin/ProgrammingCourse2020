# -*- coding: utf-8 -*-
"""
Created on 

"""

array1 = [10,324,1341,134,143]  
array2 = [0.001,0.3,0.4]
array3 = ["Eva", "Alexandre", "Yaroslav","Rodion","Felix","Alper","Maxim","Sasha"] 

print(array1)
array1.append(123)
print(array1)

array1[1] = 5
print(array1)

for i in range(0,len(array3)):
    print(i, array3[i])

for name in array3:
    print("Privet, " + name)
    
array4=[1,2,3]
array4[0] = 5
print(array4)

print(sorted(array3))