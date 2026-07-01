"""
Assignment: 23
Problem: 05
Topic: Loops again
Description: Write a python script to print the octal equivalent of a given decimal number. (Do not use oct() method)
Date: 30-06-2026
"""

n=int(input("Enter a number: "))
octal=''
if n<0:
    n*=-1
while n:
    octal=str(n%8)+octal
    n//=8
print(octal)