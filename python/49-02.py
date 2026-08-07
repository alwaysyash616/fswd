"""
Assignment: 49
Problem: 02
Topic: Iterators and Generators
Description: Write a generator to produce first N terms of the Fibonacci series.
Date: 07-08-2026
"""

def fibonacci(n):
    a,b=-1,1
    for i in range(1,n+1):
        a,b=b,a+b
        yield b

for e in fibonacci(int(input("Enter a number: "))):
    print(e,end=' ')
print()