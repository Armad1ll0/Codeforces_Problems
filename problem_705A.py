# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 20:44:24 2023

@author: amill212
"""

#Problem 705A Codeforces: Hulk
n = int(input())

string = ''
a = 'I hate'
b = 'I love'
c = ' it '
d = ' that '
for i in range(n):
    if i%2 == 0:
        string = string + a
    else: 
        string = string + b
    if i != n-1:
        string = string + d

string = string + c
string = string[0:-1]
print(string)
        
    