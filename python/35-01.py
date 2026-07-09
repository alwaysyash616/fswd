"""
Assignment: 35
Problem: 01
Topic: Functions-4
Description: Write a Python function to calculate LCM of two number. (TSRS)
Date: 04-07-2026
"""

def lcm(a,b):
    i=1
    while True:
        if not a*i%b:
            return a*i
        i+=1

print("Enter two numbers: ")
print(lcm(int(input()),int(input())))