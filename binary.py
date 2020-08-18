# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 16:01:49 2020

@author: Aditya
"""

def binary(array,k,n):
    for i in range(n):
        if array[i]==k:
            return i
        else:
            print("false")
        
array = [1,5,8,7,6,2]
binary(array,4,n)
n = len(array)

