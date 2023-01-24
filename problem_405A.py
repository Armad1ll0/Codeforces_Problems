# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 12:29:08 2023

@author: amill212
"""

#Problem 405A Codeforces: Gravity Flip
n = int(input())
cols = list(map(int, input().split()))

after_grav = sorted(cols)
string = ''
for i in after_grav:
    string = string + str(i) + ' '
    
string = string[0:-1]
print(string)