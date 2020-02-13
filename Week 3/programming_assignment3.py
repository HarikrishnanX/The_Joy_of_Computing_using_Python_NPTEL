# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:22:16 2020

@author: krish
"""
x=input()
num=list(map(int,x.split()))
l=[]
for i in num:  
    if(i%5!=0):
        l.append(i)
print(*l,sep=" ",end="")