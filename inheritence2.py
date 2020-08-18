# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 23:02:39 2020

@author: Aditya
"""

class person:
    no_of_people = 0
    
    def __init__(self,name):
        self.name = name
        person.add_people()
        
    @classmethod    
    def no_of_people_(cls):
        return cls.no_of_people
    
    @classmethod
    def add_people(cls):
        cls.no_of_people+=1
    
p = person("aditya")
p1 = person("roma")
print(person.no_of_people)