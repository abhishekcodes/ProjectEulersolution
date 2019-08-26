# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 13:10:07 2019

@author: Durgesh
"""

x = 1
y = 1
d = 0
z = 1
arr= []


'''n = 20
i = 2
while i * i < n:
     while n % i == 0:
         n = n / i
     i = i + 1

print (n)'''

for x in range(10,21):
    for y in range(2,x+1):
        if x%y == 0:
            print(y)
            arr.append(y)

p = len(arr)

for d in range(0,p):
    z = z*arr[d]
    

    