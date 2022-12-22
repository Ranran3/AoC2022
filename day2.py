# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 17:30:01 2022

@author: 44775
"""

import numpy as np

pair = np.loadtxt("day2input.txt", dtype = str)

score = 0



for i in range(len(pair)):
    if pair[i, 1] == 'X':
        score += 1
    if pair[i, 1] == 'Y':
        score += 2
    if pair[i, 1] == 'Z':
        score += 3
    
    if pair[i, 0] == 'A':
        if pair[i, 1] == 'X' :
            score += 3
        if pair[i, 1] == 'Y' :
            score += 6
        if pair[i, 1] == 'Z' :
            score += 0
            
    if pair[i, 0] == 'B':
        if pair[i, 1] == 'X' :
            score += 0
        if pair[i, 1] == 'Y' :
            score += 3
        if pair[i, 1] == 'Z' :
            score += 6
            
    if pair[i, 0] == 'C':
        if pair[i, 1] == 'X' :
            score += 6
        if pair[i, 1] == 'Y' :
            score += 0
        if pair[i, 1] == 'Z' :
            score += 3
        
print(score)

#%%

#new score is called t

t = 0

for i in range(len(pair)):
    
    if pair[i,0] == 'A':
        if pair[i,1] == 'X':
            t += 3
        if pair[i,1] == 'Y':
            t += 4
        if pair[i,1] == 'Z':
            t += 8
            
    if pair[i,0] == 'B':
        if pair[i,1] == 'X':
            t += 1
        if pair[i,1] == 'Y':
            t += 5
        if pair[i,1] == 'Z':
            t += 9
            
    if pair[i,0] == 'C':
        if pair[i,1] == 'X':
            t += 2
        if pair[i,1] == 'Y':
            t += 6
        if pair[i,1] == 'Z':
            t += 7
            
print(t)
        


































