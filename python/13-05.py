"""
Assignment: 13
Problem: 05
Topic: More on Descision Control
Description: Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
Date: 26-06-2026
"""

print("Enter three numbers:")
a,b,c=int(input()),int(input()),int(input())
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)