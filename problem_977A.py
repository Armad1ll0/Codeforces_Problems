# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 16:55:22 2022

@author: amill212
"""

#Problem 977A Codeforces: Wrong Subtraction 
n, k = map(int, input().split())

count = 0
while count < k:
    if n % 10 ==0:
        n = n/10
        count += 1
    else: 
        n = n - 1
        count += 1
        
print(int(n))