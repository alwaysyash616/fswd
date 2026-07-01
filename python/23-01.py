"""
Assignment: 23
Problem: 01
Topic: Loops again
Description: Write a python script to calculate factorial of a given number.
Date: 30-06-2026
"""

n=int(input("Enter a number: "))
factorial=1
for e in range(1,n+1):
    factorial*=e
print("Factorial is:",factorial)