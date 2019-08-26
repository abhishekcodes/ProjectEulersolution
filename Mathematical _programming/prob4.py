# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 13:46:25 2019

@author: Durgesh
"""

x = 10
y= 10
z = 10
n = 0


for x in range (10,99):
    for y in range(10,99):
        for z in range(10,99):
            n = x*y*z
            a = str(n)
            b = a[::-1] #string reverse
            if a == b:
                print("required:",x,y,z,a)
                break
               
            





























# Python3 code for the grouper recipe 
  
# import the existing itertool izip_longest 
from itertools import izip_longest 
  
# function for the grouper recipe 
def grouper(iterable, n, fillvalue ='x'): 
      
    # create 'n'-blocks for collection 
    args = [iter(iterable)] * n 
      
    # collect data into fixed legth blocks of 
    # length 'n' using izip_longest and store 
    # result as a list 
    ans = list(izip_longest(fillvalue = fillvalue, *args)) 
      
    # (optional) loop to convert ans to string 
    t = len(ans) 
    for i in range(t): 
        ans[i] = "".join(ans[i]) 
      
    # return ans as string     
    return " ".join(ans)     
  
  
# Driver code 
s = "ABCDEFG"