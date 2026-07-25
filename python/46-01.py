"""
Assignment: 46
Problem: 01
Topic: Inheritance
Description: Define a class Person with instance object variables name and age. Provide __init__() method to set instance object variables. Also define methods to show name and age. Now define a subclass Employee of Person with instance object variable salary. Provide __init__() method to initialise instance object variable. Also define instance method to show Employee data.
Date: 25-07-2026
"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showName(self):
        print("Name:",self.name)
    def showAge(self):
        print("Age:",self.age)

class Employee(Person):
    def __init__(self,name,age,salary):
        self.salary=salary
        super().__init__(name,age)
        # Person.__init__(self,name,age)
    def showEmployeeData(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self.salary)

e1=Employee("Shrishti",24,240000)
e1.showEmployeeData()