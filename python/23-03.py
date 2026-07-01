"""
Assignment: 23
Problem: 03
Topic: Loops again
Description: Write a python script to calculate sum of digits of a given number.
Date: 30-06-2026
"""

print("Enter a number: ")
n=int(input())
if n<0:
    n*=-1
sum=0
for e in str(n):
    sum+=int(e)
print('Sum of digits:',sum)