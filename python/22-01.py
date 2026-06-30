"""
Assignment: 22
Problem: 01
Topic: Loops
Description: Write a python script to calculate sum of first n natural numbers.
Date: 30-06-2026
"""

n=int(input("Enter a number: "))
sum=0
for e in range(1,n+1):
    sum+=e
print("Sum is",sum)