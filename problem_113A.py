# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 12:15:54 2023

@author: amill212
"""

#Problem 133A Codeforces: HQ9+

#We do not include + in the conditional argument because it does not produce 
#an output 

word = str(input())

count = 0
for char in word:
    if char == 'H' or char == 'Q' or char == '9':
        count += 1
        
if count == 0:
    print('NO')
else: 
    print('YES')
        