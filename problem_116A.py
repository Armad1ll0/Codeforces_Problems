# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 16:39:03 2022

@author: amill212
"""

#Problem 116A Codeforces: Tram

n = int(input())
max_num = 0
current = 0
for i in range(n):
    going, coming = map(int, input().split())
    current -= going 
    current += coming 
    if current > max_num:
        max_num = current 

print(max_num)