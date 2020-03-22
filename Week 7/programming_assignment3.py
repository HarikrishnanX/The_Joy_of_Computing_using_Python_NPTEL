# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:56:25 2020

@author: krish
"""

n,m=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]
f=0
for i in range(n):
  for j in range(m):
    if(a[i][j]!=0 and a[i][j]!=1):
      f=1
      break
if(f==0):
  print("YES",end="")
else:
  print("NO",end="")