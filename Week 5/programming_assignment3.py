# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:50:18 2020

@author: krish
"""

def isprime(n):
    if(n<=1):
        return False
    for i in range(2,int(n**0.5)+1):
        if(not n%i):
            return False;
    return True;

def prime_factors(n):
    i=2;
    d={};
    while(i<=int(n**0.5)):
        while(not n%i):
            try:
                d[i]+=1;
            except:
                d[i]=1;
            n=int(n/i);
        i+=1;
    if(n>=2):
        try:
            d[n]+=1;
        except:
            d[n]=1;
    return d;

def issemiprime(n):
    i,c=2,0;
    while(i<=int(n**0.5)):
        same=0;
        while(not n%i):
            same+=1;
            n=int(n/i);
        i+=1;
        c+=same;
        if(c>2 or same>=2):
            return False;
    if(n>=2):
        c+=1;
    if(c==2):
        return True;
    else:
        return False;

def issumsemiprime(n):
    if(n<=3):
        return False;
    for i in range(2,n):
        if(issemiprime(i) and issemiprime(n-i)):
            return True;
    return False;

n=int(input());
if(issumsemiprime(n)):
  print("Yes",end="")
else:
  print("No",end="")