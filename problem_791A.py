# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 15:54:10 2022

@author: amill212
"""

#Problem 791A Codeforces: Bear and Big Brother
limak, bob = map(int, input().split())

count = 0
while limak <= bob:
    count += 1
    limak = limak*3
    bob = bob*2

print(count)