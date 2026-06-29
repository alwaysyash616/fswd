"""
Assignment: 14
Problem: 01
Topic: Match
Description: Write a python script to check wheather a number is a three digit number or not.
Date: 26-06-2026
"""

num=int(input("Enter a number: "))
match num:
    case num if 99<num<1000:
        print("Three digit number")
    case _:
        print("Not a Three digit number")