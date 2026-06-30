"""
Assignment: 21
Problem: 01
Topic: more on for loop and range
Description: Write a python script to print first N even natural numbers.
Date: 30-06-2026
"""

n=abs(int(input("Enter a number: ")))
for e in range(2,2*n+1,2):
    print(e,end=' ')
print()