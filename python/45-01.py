"""
Assignment: 45
Problem: 01
Topic: Classes and Objects-1
Description: Define a python class Person with instance object variables name and age. Set Instance object variables in __init__() method. Also define show() method to display name and age of a person.
Date: 24-07-2026
"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)

p1=Person("Yash",24)
p1.show()