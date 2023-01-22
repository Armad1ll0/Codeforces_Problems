# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 19:34:25 2023

@author: amill212
"""

#Problem 334A Codeforces: Magnets
n = int(input())

lst = []
for i in range(n):
    lst.append(int(input()))
    
count = 1
first = lst[0]
for i in range(1, len(lst)):
    second = lst[i]
    if second != first:
        count += 1 
    first = second
    
print(count)
    