# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 12:19:30 2022

@author: amill212
"""
#Problem 158A Codeforces: Next Round 

#this maps the split inputs to integers 
n, k = map(int, input().split())

#this maps the split inputs to integers and puts them in a list 
a = list(map(int, input().split()))

#find what the threshold score is 
threshold_score = a[k-1]

#count how many peoples made it above the threshold score and had positive scores 
count = 0
for i in range(0, n):
    if a[i] >= threshold_score and a[i] > 0:
        count += 1

print(count)