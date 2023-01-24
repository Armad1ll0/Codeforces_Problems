# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 12:49:34 2023

@author: amill212
"""

#Problem 208A Codeforces: Dubstep
wubs = str(input())

string = ''
while len(wubs) > 0:
    if wubs[0:3] == 'WUB':
        wubs = wubs[3:]
        string = string + ' '
    else: 
        string = string + wubs[0]
        wubs = wubs[1:]

#Getting rid of the unnecessary white space when it has been put in
if string[0] == ' ':
    string = string[1:]
    
string = ' '.join(string.split())
print(string)