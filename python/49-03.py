"""
Assignment: 49
Problem: 03
Topic: Iterators and Generators
Description: Write a generator to produce squares of first N natural numbers.
Date: 08-08-2026
"""

def squares(n):
    for num in range(1,n+1):
         yield num**2

for e in squares(int(input("Enter a number: "))):
    print(e,end=' ')
print()