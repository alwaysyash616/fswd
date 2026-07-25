"""
Assignment: 46
Problem: 05
Topic: Inheritance
Description: Define a class Polygon with instance object variable to store number of sides and a list of n side length values. Define a subclass Traingle of Polygon with instance methods getArea().
Date: 25-07-2026
"""

class Polygon:
    def __init__(self,n,l):
        if len(l)==n:
            self.number_of_sides=n
            self.lengths_of_sides=l

class Traingle(Polygon):
    def __init__(self,a,b,c):
        if a and b and c and a+b>c and b+c>a and a+c>b:
            super().__init__(3,[a,b,c])
            
    def getArea(self):
        a,b,c=self.lengths_of_sides
        s=(a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c))**0.5

# This program is not fully correct. If should raise an exception if the traingle is incorrect.