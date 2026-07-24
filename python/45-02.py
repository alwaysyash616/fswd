"""
Assignment: 45
Problem: 02
Topic: Classes and Objects-1
Description: Define a class Circle with instance object variable radius. Provide setter and getter for radius. Also define getArea() and getCircumference() methods.
Date: 24-07-2026
"""

class Circle:
    def __init__(self,radius=0):
        self.radius=radius
    def setRadius(self,radius):
        self.radius=radius
    def getRadius(self):
        return self.radius
    def getArea(self):
        return 3.14*self.radius**2
    def getCircumference(self):
        return 2*3.14*self.radius

c1=Circle()
c1.setRadius(5) # Circle.setRadius(c1,5)
print(c1.getRadius(),c1.getArea(),c1.getCircumference(),sep='\n')