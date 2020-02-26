# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:12:44 2020

@author: krish
"""

n=input()
zero_count=0
one_count=0
for digit in n:
  if(digit=='0'):
    zero_count+=1
  else:
    one_count+=1
if(zero_count==1 or one_count==1):
  print("YES",end="")
else:
  print("NO",end="")