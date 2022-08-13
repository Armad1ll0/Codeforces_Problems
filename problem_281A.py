# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 15:00:38 2022

@author: amill212
"""

#Problem 281A Codeforces: Word Capitalization 
m = input()

first = m[0]
second = m[1:]

final = first.upper()+second
print(final)