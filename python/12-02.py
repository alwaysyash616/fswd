"""
Assignment: 12
Problem: 02
Topic: Descision Control
Description: Write a python script to check wheather a given number is divisible by 5 or not
Date: 26-06-2026
"""

num=int(input("Enter a number: "))
temp=num%10
if temp==5 or temp==0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")