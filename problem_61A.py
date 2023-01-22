# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 20:13:44 2023

@author: amill212
"""

#Problem 61A Codeforces: Ultra-Fast Mathematician 
first = str(input())
second = str(input())

string = ''
#This is a slower way of doing it
for i in range(len(first)):
    if first[i] == second[i]:
        string = string + '0'
    else: 
        string = string + '1'
    
print(string)
#I think there is a faster way of doing it though through bitwise stuff 
#zyou could do some form of boolean stuff if they are the True values. 
#Something to consider for next time if I decide to revisit, there is a way 
#more optimal way to do this problem. 
