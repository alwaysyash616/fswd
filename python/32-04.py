"""
Assignment: 32
Problem: 04
Topic: Functions-1
Description: Write a python function to calculate compound interest. (TSRS)
Date: 04-07-2026
"""

def ci(p,r,t):
    return p*(1+r/100)**t-p
print("Enter Principle Amount, Rate and Time:")
p,r,t=int(input()),int(input()),int(input())
print(ci(p,r,t))