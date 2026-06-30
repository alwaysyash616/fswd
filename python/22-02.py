"""
Assignment: 22
Problem: 02
Topic: Loops
Description: Write a python script to calculate sum of squares of first N natural numbers.
Date: 30-06-2026
"""

n=int(input("Enter a number: "))
sum=0
for e in range(1,n+1):
    sum+=e**2
print("Sum of squares:",sum)