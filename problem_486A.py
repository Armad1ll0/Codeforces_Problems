# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 19:50:19 2023

@author: amill212
"""

#Problem 486A Codeforces: Calculating Function 
n = int(input())

#This solution works but is too slow for codeforces 
# =============================================================================
# f = 0
# for i in range(1, n+1):
#     if i%2 != 0:
#         f -= i
#     else: 
#         f += i   
# print(f)
# =============================================================================

#Again this one is too slow as well 
# =============================================================================
# f = 0
# for i in range(1, n+1):
#     f += ((-1)**i) * i
# print(f)
# =============================================================================

#Another version of this without using a for loop is 
if n%2 == 0:
    print(int(n/2))
else: 
    prev = (n-1)/2
    print(int(prev-n))