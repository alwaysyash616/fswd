"""
Assignment: 35
Problem: 03
Topic: Functions-4
Description: Write a Python function to create a list of Prime numbers between two given numbers (TSRS)
Date: 04-07-2026
"""

def isPrime(n):
    i=2
    while i<=n//2:
        if not n%i:
            break
        i+=1
    if i==n//2+1:
        return True
    else:
        return False

def primesBetween(a,b):
    return [e for e in range(a,b+1) if isPrime(e)]

print("Enter two numbers: ")
print(primesBetween(int(input()),int(input())))