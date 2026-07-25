"""
Assignment: 46
Problem: 03
Topic: Inheritance
Description: Demonstrate the use of super() in inheritence.
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

# It's the solution to problem 46-01 which also demonstrates the use of super() in inheritence.