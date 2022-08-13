# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 12:07:03 2022

@author: amill212
"""
#Problem 231A Codeforces: Team 

n = int(input())

solve = 0
for i in range(0, n):
    nums = []
    x = str(input())
    for char in x: 
        if char.isnumeric():
            nums.append(int(char))
    if sum(nums) >= 2:
        solve += 1
        
print(solve)
        
    