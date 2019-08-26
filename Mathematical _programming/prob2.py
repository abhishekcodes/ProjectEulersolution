# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 12:44:26 2019

@author: Durgesh
"""

"""for x in range (1,):
    
    
 while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
  """
x =1 
y = 2
count = 0
arr =[]
for count in range(1,31):
    z = x+y
    x = y
    y = z
    count +=1 
    arr.append(z)
    if z%4000000==0:
        break

p = len(arr)

print("fibonacci array", *arr)
sum = 0
    


for i in range (0,30):
    if arr[i]%2== 0:
        print(arr[i])
        sum = sum+arr[i]+2
    
print(sum)
