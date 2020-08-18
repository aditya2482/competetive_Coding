# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:51:47 2020

@author: Aditya
"""
class pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show_age(self):
        print(f"iam {self.name} and iam {self.age} years old")
        
    def speak(self):
        print("i can speak no language")
        
class cat(pet):
    
    
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
    
    
    def speak(self):
        print("meow")
    
    def show_age(self):
        print(f"hello iam {self.name} age {self.age} and my color is {self.color}")
        
    
class dog(pet):
    
    def speak(self):
        print("bark")
        
p = pet("tim",29)
p.show_age()
p.speak()

c = cat("roma",20,"red")
c.show_age()
c.speak()

d = dog("kanu",52)
d.show_age()
d.speak()