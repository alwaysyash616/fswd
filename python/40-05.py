"""
Assignment: 40
Problem: 05
Topic: Recursion-4
Description: Write a recursive function to calculate sum of first N Prime numbers.
Date: 14-07-2026
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

def sumPrimes(n,start=1):
    while True:
        if isPrime(start):
            break
        start+=1
    if n==1:
        return start
    else:
        return start+sumPrimes(n-1,start+1)

print(sumPrimes(int(input("Enter a number: "))))