# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 13:00:34 2022

@author: amill212
"""

#Problem 50A Codeforces: Domino Piling 

m, n = map(int, input().split())

def num_doms(m, n):
    area = m*n
    num_doms = int(area/2)
    print(num_doms)
    
num_doms(m, n)