# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:49:27 2020

@author: krish
"""
import math
n,v1,v2=input().split()
n=int(n)
v1=int(v1)
v2=int(v2)
walk_dist=(math.sqrt(2))*n
cab_dist=2*n
time_walk=walk_dist/v1
time_cab=cab_dist/v2
if(time_cab>time_walk):
  print("Walk",end="")
else:
  print("Cab",end="")
