# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:12:10 2020

@author: krish
"""

vowels = "aeiou"
s=input();
i=0;
n=len(s);
while(i<n):
  print(s[i],end="");
  if(s[i] in vowels):
    while(i<n and s[i] in vowels):
      i+=1;
    continue;
  i+=1;