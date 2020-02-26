# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:16:15 2020

@author: krish
"""

r,c=map(int,input().split())
x=0
for i in range(r):
  for j in range(c):
    x+=1
    if(i==r-1 and j==c-1):
      print(x,end="")
    elif(x%c==0):
      print(x)
    else:
      print(x,end=" ")