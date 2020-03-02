# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:50:04 2020

@author: krish
"""
x=list(map(int,input().split()))
x1=sorted(x)
c=0
for i in range(len(x)):
  if(x[i]==x1[c]):
    c+=1
print(len(x)-c,end="")  
