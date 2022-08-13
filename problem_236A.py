# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 15:09:00 2022

@author: amill212
"""

#Problem 236A Codeforces: Boy or Girl 
m = input()

#we can actually use set function to get the distrinct number of letters
distinct_list = list(set(m))

if len(distinct_list)%2 == 0:
    print('CHAT WITH HER!')
else: 
    print('IGNORE HIM!')