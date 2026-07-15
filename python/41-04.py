"""
Assignment: 41
Problem: 04
Topic: lambda
Description: Write a lambda expression to find HCF of two numbers.
Date: 16-07-2026
"""

gcd=lambda x,y: (y if x%y==0 else gcd(x%y,y)) if x>y else (x if y%x==0 else gcd(y%x,x))
print("Enter two numbers:")
print(gcd(int(input()),int(input())))