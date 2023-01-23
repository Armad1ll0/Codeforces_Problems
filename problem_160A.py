# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 12:25:07 2023

@author: amill212
"""

#Problem 160A Codeforces: Twins
n = int(input())
coins = list(map(int, input().split())) 

total_value = sum(coins)
threshold = total_value/2 

sorted_coins = sorted(coins, reverse = True)

totals = []
counts = []
total = 0
count = 0
for i in range(len(coins)):
    count += 1
    total += sorted_coins[i]
    if total > threshold:
        totals.append(total)
        counts.append(count)
        total = 0
        count = 0
        if totals[-1] > threshold and count == 1: 
            print(1)
            break
        else: 
            total = sorted_coins[i]
            count += 1
    
print(min(counts))