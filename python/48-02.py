"""
Assignment: 48
Problem: 02
Topic: Exception Handling
Description: Define a function to find greater value among three given data. Handle all possible exceptions.
Date: 02-08-2026
"""

def f2():
    try:
        print("Enter three numbers:")
        a,b,c=int(input()),int(input()),int(input())
        print(max([a,b,c]))
    except ValueError:
        print("Invalid Value")
    except:
        print("Unknown Exception")

f2()