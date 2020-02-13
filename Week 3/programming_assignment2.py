# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:21:30 2020

@author: krish
"""
l=[]
l=(list(map(int,input().split())))
maximum=max(l[0],l[1])
secondmax=min(l[0],l[1])
minimum=min(l[0],l[1])
secondmin=max(l[0],l[1])
for i in range(2,len(l)):
  if(l[i]>maximum):
    secondmax=maximum
    maximum=l[i]
  else:
    if(l[i]>secondmax):
      secondmax=l[i]
for i in range(2,len(l)):
  if(l[i]<minimum):
    secondmin=minimum
    minimum=l[i]
  else:
    if(l[i]<secondmin):
      secondmin=l[i]
print(secondmax,secondmin,end="")