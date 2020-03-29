# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:03:14 2020

@author: krish
"""

s=input();
d={}
for i in s:
  if(i.isalpha()):
    i=i.lower();
    try:
      d[i]+=1;
    except:
      d[i]=1;
print('YES' if len(d.keys())==26 else 'NO',end='');