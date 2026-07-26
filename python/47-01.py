"""
Assignment: 47
Problem: 01
Topic: Polymorphism
Description: Define a Python class Person with name and age as instance object variables. Define Student and Teacher two subclasses of Person. Provide rollNo as instance object variable in Student, provide subject as instance object variable in Teacher class. Now define a function show to print values of instance object variables in both the classes. Demonstrate polymorphic behaviour or show function.
Date: 26-07-2026
"""

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Student(Person):
#     def __init__(self,name,age,rollNo):
#         super().__init__(name,age)
#         self.rollNo=rollNo
#     def show(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Roll No.:",self.rollNo)
# class Teacher(Person):
#     def __init__(self,name,age,subject):
#         super().__init__(name,age)
#         self.subject=subject
#     def show(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Subject:",self.subject)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Student(Person):
    def __init__(self,name,age,rollNo):
        super().__init__(name,age)
        self.rollNo=rollNo
    def show(self):
        super().show()
        print("Roll No.:",self.rollNo)
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
    def show(self):
        super().show()
        print("Subject:",self.subject)

for obj in [Student('Raj',24,60), Teacher('Anurag',32,40)]:
    obj.show()