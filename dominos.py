# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:46:55 2020

@author: Aditya
"""

m = int(input())
n = int(input())
remnain = 0

def dominos():
    if m & n ==0:
        print("invalid box")
    else:
        remain =int((m*n)/2)
        print(remain)

dominos()
        