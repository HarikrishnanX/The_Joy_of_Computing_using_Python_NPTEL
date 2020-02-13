# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:21:05 2020

@author: krish
"""
n=int(input())
l=[]
l=(list(map(int,input().split())))
m=[]
m=list(reversed(l))
for i in range(0,n-1):
  l[i]+=m[i]
  print(l[i],end=" ")
l[n-1]+=m[n-1]
print(l[n-1],end="")
