# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:03:02 2020

@author: krish
"""

l=list(map(int,input().split()))
l=list(dict.fromkeys(l))
n=len(l)
for i in range(n-1):
  print(l[i],end=" ")
print(l[n-1],end="")