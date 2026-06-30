"""
Assignment: 21
Problem: 04
Topic: more on for loop and range
Description: Write a python script to print cubes of first N natural numbers.
Date: 30-06-2026
"""

n=int(input("Enter a number: "))
for e in range(1,n+1):
    print(e**3,end=' ')
print()