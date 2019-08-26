# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 12:00:19 2019

@author: Durgesh
"""
import math
count1 = 0
count2 = 0
count3 = 0
x=0
y=0
z= 0
for x in range (0,1000):
    if x % 3 == 0:
        count1 = count1 + x
    
for y in range (0,1000):       
    if y % 5 == 0:
        count2 == count2 + y
        
for z in range(0,1000):
    if z % 3 ==0 and z%5 == 0:
        count3 = count3+ z

print("SUM", count1+count2- count3)


     