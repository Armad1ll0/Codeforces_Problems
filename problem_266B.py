# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 16:50:10 2022

@author: amill212
"""

#Problem 266B Codeforces: Queue at the School 
n, x = map(int, input().split())
order = input()

listed = []
for char in order:
    listed.append(char)

for j in range(0, x):
    i=0
    while i < n-1:
        if listed[i] == 'B' and listed[i+1] == 'G':
            listed[i] = 'G'
            listed[i+1] = 'B'
            i += 1
        i += 1

final_list = ''
for i in listed:
    final_list = final_list + i
    
print(final_list)

