# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 13:22:26 2022

@author: amill212
"""

#Problem 263A Codeforces: Beautiful Matrix 

#NOTE: Originally I tried to use Numpy but you cannot with codeforces 

#converting the input to a 5x5 matrix 
line0 = list(map(int, input().split()))
line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))
line4 = list(map(int, input().split()))
m = [line0, line1, line2, line3, line4]

#stating the centre of the matrix and where the 1 is located in our input 
centre = [2, 2]

#getting index of the 1 entry 
for i in range(len(m)):
    if sum(m[i]) == 1:
        coords = [i, m[i].index(1)]

#saying how many moves away it is 
first = abs(centre[0] - coords[0])
second = abs(centre[1] - coords[1])
moves = first + second
print(moves)