"""
Assignment: 22
Problem: 03
Topic: Loops
Description: Write a python script to calculate sum of cubes of first N natural numbers.
Date: 30-06-2026
"""

n=int(input("Enter a number: "))
sum=0
for e in range(1,n+1):
    sum+=e**3
print("Sum of cubes:",sum)