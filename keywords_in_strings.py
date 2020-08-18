# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:51:48 2020

@author: Aditya
"""

import keyword

def iskeyword(word):
    for i in range(0,len(word)):
        if word[i] in keyword.kwlist:
            print("present" + " " + str(word[i]))
        else:
            print("not in list"+ " "+ str(word[i]))

program = "num = 8 num_sqrt = num ** 0.5 print ('The square root of %0.3f is %0.3f'%(num ,num_sqrt))"
word = program.split()
iskeyword(word)



'''
keywords = ["true","False","class","def","return"
"if","elif","else","try","except"
"raise","finally","for","in","is",
"not","from","import","global","lambda",
"nonlocal","pass","while","break","continue",
"and","with","as","yield","del",
"or","assert","None"]

def get_program(keywords,program):
    count = 0
    for i in range(0,len(program)):
        if program in keywords:
            count+=1
            print(program)
        else:
            print("no keyword in args")
    
program = "def function(): a = 10 print(a)"
get_program(keywords,program)
'''