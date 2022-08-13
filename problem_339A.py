# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 14:51:34 2022

@author: amill212
"""
#Problem 339A Codeforces: Helpful Maths 

string = input()

#getting all the seperate numbers in the input 
number_list = []
for char in string:
    if char.isnumeric():
        number_list.append(int(char))

#sort the numbers list in ascending order 
sorted_number_list = sorted(number_list)

#create a string out of it and add in the +
string =''
for i in sorted_number_list:
    string += str(i)+'+'
    
#remove the last + from the string 
string = string[:-1]

print(string)