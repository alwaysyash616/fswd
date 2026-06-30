"""
Assignment: 20
Problem: 02
Topic: for loop and range
Description: Write a python script to print first 10 multiples of N.
Date: 30-06-2026
"""

n=int(input("Enter a number: "))
for x in range(n,n*10+1,n):
    print(x,end=' ')
print()