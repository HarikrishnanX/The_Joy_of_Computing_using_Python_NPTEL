# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:56:16 2020

@author: krish
"""

n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
f=0
for i in range(n):
  for j in range(n):
    if(i!=j):
      if(a[i][j]!=a[j][i]):
        f=1
        break
if(f==0):
  print("YES",end="")
else:
  print("NO",end="")