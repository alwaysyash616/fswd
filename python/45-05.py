"""
Assignment: 45
Problem: 05
Topic: Classes and Objects-1
Description: Define a class Team with instance object variable a list of team member names. Provide methods to input member names and display member names.
Date: 24-07-2026
"""

class Team:
    def __init__(self,members=None):
        if members is None:
            members=[]
        self.team_members=members
    def inputMemberNames(self):
        print("Enter names of Team Members separated by comma:")
        self.team_members=input().split(',')
    def displayMemberNames(self):
        for e in self.team_members:
            print(e)

t1=Team(['Sachin','Ravindra','Ronaldo','Messi'])
t1.displayMemberNames()
t1.inputMemberNames()
t1.displayMemberNames()