# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 13:13:43 2022

@author: amill212
"""

#Problem 282A Codeforces: Bit++

n = int(input())

count_plus = 0
count_minus = 0
for i in range(0, n):
    op = input()
    plus = 0
    minus = 0
    for char in op:
        if char == '+':
            plus += 1 
        elif char == '-':
            minus += 1
    if plus == 2: 
        count_plus += 1
    if minus == 2: 
        count_minus += 1
        
print(count_plus - count_minus)