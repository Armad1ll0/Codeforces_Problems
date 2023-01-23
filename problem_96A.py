# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 12:15:01 2023

@author: amill212
"""

#Problem 86A Codeforces: Football 
n = str(input())

lst = []
for i in n:
    lst.append(int(i))

count = 1
for i in range(1, len(lst)):
    if lst[i] == lst[i-1]:
        count += 1
    else: 
        count = 1
    #print(count)
    if count == 7:
        print('YES')
        break 

if count < 7:
    print('NO')