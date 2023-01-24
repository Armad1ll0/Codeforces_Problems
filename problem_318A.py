# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 12:48:40 2023

@author: amill212
"""

#Problem 318A Codeforces: Even Odds 
n, k = map(int, input().split())

#the following will work but it is quite slow so i need a way to optimise it 
# =============================================================================
# odds = []
# evens = []
# for i in range(1, n+1):
#     if i%2 == 0:
#         evens.append(i)
#     else: 
#         odds.append(i)
# 
# new_numbers = odds + evens 
# 
# print(new_numbers[k-1])
# =============================================================================

#again the following is not fast enough 
# =============================================================================
# odds = list(range(1, n+1, 2))
# evens = list(range(2, n+1, 2))
# new_numbers = odds + evens 
# print(new_numbers[k-1])
# =============================================================================

#Method for this is if k is smaller than n/2 it will be in the odds list 
#and we can link the index k to the actual number we need 2*k - 1 etc 
#we can do a very similar thing for if the index is in the evens list 

#I think this should be correct but I keep getting that it fails for some 
#reason on one of the test cases but I cannot see it. 
if (k <= (n + 1) / 2):
    print(int(k * 2 - 1))
else: 
    print(int((k - (n + 1) / 2) * 2))