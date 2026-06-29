"""
Assignment: 14
Problem: 04
Topic: Match
Description: Write a python script to take data from one user and evaluate the type of data. If the data is of int type then print Monday, if the data is of float type then print Tuesday, if the data is of complex type then print Wednesday, if the data is of type bool then print Thursday.
Date: 26-06-2026
"""

x=eval(input("Enter some data: "))
match x:
    case x if type(x)==int:
        print("Monday")
    case x if type(x)==float:
        print("Tuesday")
    case x if type(x)==complex:
        print("Wednesday")
    case x if type(x)==bool:
        print("Thursday")