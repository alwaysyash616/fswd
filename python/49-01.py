"""
Assignment: 49
Problem: 01
Topic: Iterators and Generators
Description: Write a generator to produce first N prime numbers.
Date: 06-08-2026
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

def nextPrime(n):
    n+=1
    while not isPrime(n):
        n+=1
    return n

def primes(n):
    p=1
    while n:
        p=nextPrime(p)
        yield p
        n-=1

for e in primes(int(input("Enter a number: "))):
    print(e,end=' ')
print()