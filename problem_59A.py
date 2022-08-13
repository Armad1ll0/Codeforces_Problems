# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 16:45:46 2022

@author: amill212
"""

#Problem 59A Codeforces: Word 
word = input()

total = len(word)
count = 0
for char in word: 
    if char.isupper():
        count += 1

if count > total/2:
    print(word.upper())
else: 
    print(word.lower())