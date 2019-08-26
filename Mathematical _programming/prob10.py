# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:12:37 2019

@author: Durgesh
"""
'''num = 10
count = 0
for i in range(1,num):
    if num%i == 0:
        print("not prime")
    else:
        print(num)
        count = count+num

print(count)'''
    

def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True
count = 0
for n in range(1,2000000):
    if isPrime2(n) == True:
        #print(n)
        count = count + n
    else:
        continue
  
print(count)