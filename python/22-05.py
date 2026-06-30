"""
Assignment: 22
Problem: 05
Topic: Loops
Description: Write a python script to calculate sum of first N even natural numbers.
Date: 30-06-2026
"""

n=int(input("Enter a number: "))
sum=0
for x in range(2,2*n+1,2):
    sum+=x
print("Sum is:",sum)