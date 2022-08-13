# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 17:53:18 2022

@author: amill212
"""

#Problem 724A Codeforces: Anton and Danik 

n = int(input())
winners = input()

winners_list = []
for char in winners:
    winners_list.append(char)
    
anton = winners_list.count('A')
danik = winners_list.count('D')
if anton > danik:
    print('Anton')
elif danik > anton:
    print('Danik')
else: 
    print('Friendship')
