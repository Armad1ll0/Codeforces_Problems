# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 13:22:03 2023

@author: amill212
"""

#Problem 377A Codeforces: Puzzles
n, m = map(int, input().split())
sizes = list(map(int, input().split()))

sorted_sizes = sorted(sizes)
end = m-n
differences = []
for i in range(end+1):
    window = sorted_sizes[i:i+n]
    differences.append(window[-1] - window[0])

print(min(differences))
