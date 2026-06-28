"""
Assignment: 13
Problem: 03
Topic: More on Descision Control
Description: Write a python script to check wheather a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
Date: 26-06-2026
"""

print("A quadratic equation is represented by ax^2+bx+c=0\nEnter the values for a,b and c")
a,b,c=int(input()),int(input()),int(input())
discriminant=b**2-4*a*c
if discriminant>0:
    print("real & distinct roots")
elif discriminant==0:
    print("real & equal roots")
else:
    print("imaginary roots")