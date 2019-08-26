# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 14:06:05 2019

@author: Durgesh
"""
import numpy

x = 100
y= 100
n = 0
arr = []

for x in range (100,999):
    for y in range(100,999):
        n = x*y
        c = str(n)
        d = c[::-1]
        #list(stringObject.split())
        if n == int(d):
            #print("required:",x,y,c)
            arr.append(n)
            break
        
print(arr.max())