"""
Assignment: 33
Problem: 02
Topic: Functions-2
Description: Write a python function to find greater among three numbers(TSRS)
Date: 04-07-2026
"""

def greater(a,b,c):
    return (a if a>c else c) if a>b else (b if b>c else c)

print("Enter three numbers:")
print(greater(int(input()),int(input()),int(input())))