"""
Assignment: 45
Problem: 03
Topic: Classes and Objects-1
Description: Define a class Rectangle with length and breadth as instance object variables. Provide setDimensions(), showDimensions() and getArea() method in it.
Date: 24-07-2026
"""

class Rectangle:
    def __init__(self,length=0,breadth=0):
        self.length=length
        self.breadth=breadth
    def setDimensions(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def showDimensions(self):
        print("Length:",self.length)
        print("Breadth:",self.breadth)
    def getArea(self):
        return self.length*self.breadth

r1=Rectangle()
r1.setDimensions(4,5)
r1.showDimensions()
print(r1.getArea())