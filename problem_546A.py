# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 16:06:38 2022

@author: amill212
"""

#Problem 546A Codeforces: Soldier and Bananas 
k, n, w = map(int, input().split())

cost = 0
for i in range(1, w+1):
    cost += k*i
     
borrow = n - cost 
if borrow < 0: 
    print(abs(borrow))
else: 
    print(0)
