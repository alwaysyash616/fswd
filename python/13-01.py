"""
Assignment: 13
Problem: 01
Topic: More on Descision Control
Description: Write a python script to check wheather a given number is three digit number or not.
Date: 26-06-2026
"""

num=int(input("Enter a number: "))
if num>99 and num<1000:
    print("Three digit number")
else:
    print("Not a three digit number")