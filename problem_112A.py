# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 14:26:25 2022

@author: amill212
"""

#Problem 112A Codeforces: Petya and Strings 

#creating a list of words and making them all lower case
original_list = []
for i in range(2):
    original_list.append(input().lower())

#indexing the first and second words 
first_word_orig = original_list[0]
second_word_orig = original_list[1]

#sorting the list lexicographically 
sorted_list = sorted(original_list)

#indexing the words of the sorted list 
first_word_sort = sorted_list[0]
second_word_sort = sorted_list[1]

#if the words are the same, give 0
if first_word_orig == second_word_orig: 
    print(0)
#if the order is unchanged then the first is less than the second 
elif first_word_orig == first_word_sort:
    print(-1)
#if order is changed, second is less than the first 
else:
    print(1)