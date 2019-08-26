# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:49:41 2019

@author: Durgesh
"""

"""def n_even(n):
    n = n/2
    return n

def n_odd(n):
    n = 3*n+1
    return n

def seq_length(x):
    arr = []
    arr.append(x)
    return max(arr)

for n in range(1,1000000):
    count= 1
    while (n!=1):
        count+=1
        if n%2== 0:
            a = n_even(n)
            n = a
        else:
            b = n_odd(n)
            n = b
    count+=1
    seq_length(count)
        
print(count)"""



length = 1
max_length = 1
number =1
 
for i in range(2,1000001):
    length = 1
    x = i
    while(x!=1):
        if(x%2==0):
            x /= 2
        else:
            x = x*3+1
        length += 1
 
    if(length,max_length):
        max_length = length
        number = i
 
print (number)