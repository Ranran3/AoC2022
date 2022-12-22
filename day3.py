# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 13:03:37 2022

@author: 44775
"""

import numpy as np
from string import ascii_lowercase , ascii_uppercase


objects = np.loadtxt('day3input.txt', dtype = str)

letters = np.array(ascii_lowercase + ascii_uppercase).tolist()

def compare(x, y, z):
    for a in y:
        if a in z:
            
            break   
        
    return a


 #x is the collection of letters
 #y is the first half, z is the second half

t = 0
for i in range(len(objects)):

    x = objects[i]
    y = objects[i][:int(len(x)/2)]
    z = objects[i][int(len(x)/2):]
    t += letters.index(compare(x, y, z)) + 1


print(t)

############################################################################
#%%
def badge(elf1, elf2, elf3):
    for b in elf1:
        if b in elf2:
            if b in elf3:
        
                break
    print(b)
    return b
total = 0
for j in range(int(len(objects)/3)):
    elf1 = objects[3*j]
    elf2 = objects[3*j+1]
    elf3 = objects[3*j+2]
    total += letters.index(badge(elf1, elf2, elf3)) + 1

print(total)





