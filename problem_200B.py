# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 20:08:30 2023

@author: amill212
"""

#Problem 200B Codeforces: Drinks 
n = int(input())
vols = list(map(int, input().split())) 
print(sum(vols)/n)