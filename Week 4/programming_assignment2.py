# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:13:20 2020

@author: krish
"""

def factorial(num):
  fact=1
  for i in range(1,num+1):
    fact=fact*i
  return fact

n=int(input())
f=factorial(n)
print(f,end="")