# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:53:15 2023

@author: amill212
"""

#Problem 451A Codeforces: Game with Sticks 
n, m = map(int, input().split())

#This fails on test 14, not sure why. Maybe I did not catch an edge case? 
if n==1 or m==1:
    print('Akshat')
else: 
    intersections = m*n
    if intersections % 2 == 0:
        print('Malvika')
    else: 
        print('Akshat')