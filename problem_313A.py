# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 17:05:29 2023

@author: amill212
"""

#Problem 313A Codeforces: Ilya and Bank Account 
n = int(input())

if n >= 0:
    print(n)
else: 
    string = str(n)
    last_digit = int(string[0:-1])
    second_last_digit = int(string[0:-2] + string[-1])
    print(max([last_digit, second_last_digit]))