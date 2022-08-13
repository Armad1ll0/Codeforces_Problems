# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 15:18:27 2022

@author: amill212
"""

#Problem 266A Codeforces: Stones on the table 
n = int(input())

string = list(input())

#checking through the string list to see if the previous element is the same as the current one 
count = 0
for i in range(1, n):
    if string[i] == string[i-1]:
        count += 1

print(count)
