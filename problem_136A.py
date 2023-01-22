# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 15:02:11 2022

@author: amill212
"""

#Problem 136A Codeforces: Presents 
#Note: This question I found confusing and so I had to look for an answer online to explain it to me. 
#I do not think the problem was the question, but how it was explained. 
n = int(input())
p = list(map(int, input().split()))

#To explain it thoroughly I will use the first example given. 
#We have the list [2, 3, 4, 1] and we have 4 friends. This list means that 
#person 1 gave a present to person 2
#person 2 gave a present to person 3
#person 3 gave a present to person 4 
#person 4 gave a present to person 1 

#Now what the question is asking us to do is output the list of friends 
#who gave to person i in the chain in the order of 1-4. 
#person 4 gave to person 1 
#person 1 gave to person 2
#person 2 gave to person 3
#person 3 gave to person 4 

#So this question is about reordering the list 
#The second example is:
#We have 3 friends invited 
#person 1 gave to person 1 
#person 3 gave to person 2 
#person 2 gave to person 3 
#We now reorder the list so the set of integers in the first list are ordered 
#person 1 gave to person 1 
#person 2 gave to person 3
#person 3 gave to person 2 

#so we output the list of 1, 3, 2
#Now to put this is code format 
lister = []
for i in range(n):
    lister.append(i+1)

#What we need to do is reorder the first list in terms of numbers 1 to 4 
#and keep track of the indexes we changed. We can do this by using the key 
#parameter in the sorting function 
index = sorted(range(len(p)), key=lambda k: p[k])

#and because indexes start from 0 we have to add 1. 
new_index = [x+1 for x in index]

#now we create a string where each number is seperated by a space. This is 
#what they have asked us to return 
string = ''
for i in new_index:
    string = string + str(i) + ' '
string = string[0: -1]
print(string)
    