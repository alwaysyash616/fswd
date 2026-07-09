"""
Assignment: 34
Problem: 04
Topic: Functions-3
Description: Write a Python function to print first N terms of Fibonacci series (TSRN)
Date: 04-07-2026
"""

def fibonacci(n):
    a,b=0,1
    i=1
    while i<=n:
        print(a,end=' ')
        a,b=b,a+b
        i+=1
    print()

fibonacci(int(input("Enter a number:")))