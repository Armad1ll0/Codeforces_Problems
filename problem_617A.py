# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 16:31:42 2022

@author: amill212
"""

#Problem 617A Codeforces: Elephant 

n = int(input())

if n <= 5:
    print(1)
elif n > 5: 
    if n%5 == 0:
        print(int(n/5))
    else: 
        count = int(n/5) + 1
        print(count)
