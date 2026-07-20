"""
Assignment: 42
Problem: 05
Topic: Variable Length Arguments
Description: Write a function which takes variable length arguments to receive integers. Filter out Prime numbers and return a list of those Prime numbers.
Date: 20-07-2026
"""
def isPrime(n):
    i=2
    while i<=n//2:
        if n%i==0:
            break
        i+=1
    if i==n//2+1:
        return True
    else:
        return False

def primes(*t):
    return [e for e in t if isPrime(e)]


print(primes(3,4,6,5,8,7,6,192,3,599,98,54,51))
    