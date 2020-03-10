# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:37:43 2020

@author: krish
"""

n=int(input())
a=list(map(int,input().split()))
a1=sorted(a)
k=int(input())
x=a[k-1]
if x in a1:
  i=a1.index(x)+1
  print(i,end="")