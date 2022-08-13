# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 11:40:13 2022

@author: amill212
"""

#Problem 4A Codeforces: Watermelon 
x = int(input())

def split(x):
    if x > 2 and x%2==0:
        print('YES')
    else: 
        print('NO')
        

split(x)