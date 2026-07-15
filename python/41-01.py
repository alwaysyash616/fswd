"""
Assignment: 41
Problem: 01
Topic: lambda
Description: Write a lambda expression to check if a number is even.
Date: 15-07-2026
"""

isEven=lambda n:"Not Even" if n%2 else "Even"
print(isEven(int(input("Enter a number: "))))