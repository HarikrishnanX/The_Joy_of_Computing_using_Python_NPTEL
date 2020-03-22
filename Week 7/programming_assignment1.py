# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:55:54 2020

@author: krish
"""
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
  for j in range(n):
    if(j>i):
      a[i][j]=0
for i in range(0,n-1):
  for j in range(0,n-1):
    print(a[i][j],end=" ")
  print(a[i][n-1],end="\n")
for j in range(0,n-1):
  print(a[n-1][j],end=" ")
print(a[n-1][n-1],end="")
