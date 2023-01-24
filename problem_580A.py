# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 12:37:06 2023

@author: amill212
"""

#Problem 580A Codeforces: Kefa and First Steps 
n = int(input())
a = list(map(int, input().split()))

if len(a) == 1:
    print(1)
else: 
    max_count = []
    count = 1
    for i in range(1, n):
        if a[i] >= a[i-1]:
            count += 1
        else: 
            max_count.append(count)
            count = 1
        max_count.append(count)
    print(max(max_count))