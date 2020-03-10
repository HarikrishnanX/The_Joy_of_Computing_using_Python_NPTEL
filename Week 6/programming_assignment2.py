# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:41:20 2020

@author: krish
"""

n=int(input())
d={}
for i in range(1,n+1):
  d[i]=i*i*i
print(d,end="")