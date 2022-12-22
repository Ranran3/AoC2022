# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 12:56:39 2022

@author: 44775
"""


import numpy as np


# file = open('advent1.txt')
# print(file.read())

sum = np.empty([])
calories = np.empty([])
with open('day1input.txt', 'r') as file:
    for item in file:
        if item != '\n':
            calories = np.append(calories, int(item.rstrip()))
            
        else:
            total = np.sum(calories)
            sum = np.append(sum, total)
            calories = []
print(max(sum))

top3 = []
for i in range(3):
    print(max(sum))
    top3 = np.append(top3, max(sum))
    sum = np.delete(sum, np.argmax(sum))
       
    
print(np.sum(top3))

            
file.close()            
            

#%%









