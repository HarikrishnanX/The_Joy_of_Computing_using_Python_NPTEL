# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:44:19 2020

@author: krish
"""

def printDict():
  n=int(input())
  d={}
  for i in range(1,n+1):
    d[i]=i*i
  print(d,end="")
  
printDict()