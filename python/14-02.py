"""
Assignment: 14
Problem: 02
Topic: Match
Description: Write a python script to check wheather a number is positive, negative or zero.
Date: 26-06-2026
"""

num=int(input("Enter a number: "))
match num:
    case num if num>0:
        print("Positive")
    case num if num<0:
        print("Negative")
    case _:
        print("Zero")