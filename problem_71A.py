# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 11:46:24 2022

@author: amill212
"""
#Problem 71A Codeforces: Way Too Long Words

def waytolongwords(x):
    if len(x) > 10: 
        new_string = str(x[0]) + str(len(x)-2) + str(x[-1])
        print(new_string)
    else: 
        print(x)
    
#The inputs come in sequentially so thats how we deal with those 
n = int(input())
for i in range(0, n):
    x = str(input())
    waytolongwords(x)
        



