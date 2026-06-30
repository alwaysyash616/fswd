"""
Assignment: 21
Problem: 02
Topic: more on for loop and range
Description: Write a python script to print first N odd natural numbers.
Date: 30-06-2026
"""

n=int(input("Enter a number: "))
for e in range(1,2*n,2):
    print(e,end=' ')
print()