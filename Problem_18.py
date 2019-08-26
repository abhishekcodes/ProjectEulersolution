# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 09:39:37 2019

@author: Durgesh
"""

'''with open("G:\input_18.txt", 'r') as your_file:
     content = your_file.read()
    
print(content)'''

with open("G:\input_18.txt", "r") as myfile:
    total = 0
    for line in myfile.readlines():
        print(line, end="")
        total += 1
    print("\nTotal: " + str(total))
    
with open("G:\input_18.txt", "r") as myfile:
    content = myfile.read()