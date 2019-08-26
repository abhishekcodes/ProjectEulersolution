# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:04:54 2019

@author: Durgesh
"""

a = 0
b = 0
c = 0

for a in range (1,1000):
    for b in range(0,1000):
        for c in range(0,1000):
            if a+b+c == 1000 and (a*a+b*b == c*c):
                print(a,b,c)
                break
            
print(a*b*c)

                