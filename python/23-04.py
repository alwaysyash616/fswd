"""
Assignment: 23
Problem: 04
Topic: Loops again
Description: Write a python script to print binary equivalent of a given decimal number. (Do not use bin() method)
Date: 30-06-2026
"""

n=int(input("Enter a number: "))
b=''
if n<0:
    n*=-1
while n:
    b=str(n%2)+b
    n//=2
print(b)