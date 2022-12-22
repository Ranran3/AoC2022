# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 22:58:32 2022

@author: 44775
"""
import numpy as np

pairs = np.loadtxt('day4input.txt', dtype = str, delimiter = ',')

def func(a, b, c):
    
    c = 0
    
    if (int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1])) or (int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1])):
            c += 1
    
    
    return c
            
    
t = 0 
c = 0
for i in range(len(pairs)):
    x = pairs[i]
    a = x[0].split('-')
    b = x[1].split('-')
    t += func(a, b, c)
    
print(t)   



#%%

def overlap(a, b, c):
    c = 0
    
    if ((int(a[0]) <= int(b[0]) <= int(a[1])) or (int(b[0]) <= int(a[0]) <= int(b[1]))):
        c += 1
        
    return c

total = 0
p = 0

for i in range(len(pairs)):
    x = pairs[i]
    a = x[0].split('-')
    b = x[1].split('-')
    total += overlap(a, b, p)


print(total)
