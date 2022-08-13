# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 16:29:33 2022

@author: amill212
"""

#Problem 110A Codeforces: Nearly Lucky Number 
n = int(input())

#converts the individuals numbers into a list 
list_digits = [int(d) for d in str(n)]

num_4 = list_digits.count(4)
num_7 = list_digits.count(7)

k = num_4 + num_7
if k == 4 or k == 7:
    print('YES')
else: 
    print('NO')
