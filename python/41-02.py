"""
Assignment: 41
Problem: 02
Topic: lambda
Description: Write a lambda expression to find nth term of Fibonacci series
Date: 15-07-2026
"""

fibonacci=lambda n:0 if n==1 else (1 if n==2 else fibonacci(n-1)+fibonacci(n-2))
print(fibonacci(int(input("Enter a number: "))))