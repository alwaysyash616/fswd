"""
Assignment: 09
Problem: 01
Topic: Simple calculations on user data
Description: Write a python script to calculate simple interest.
Date: 25-06-2026
"""

print("Enter principle amount,rate and number of years")
p=float(input())
r=float(input())
t=float(input())
si=(p*r*t)/100
print("Simple Interest: ",si)