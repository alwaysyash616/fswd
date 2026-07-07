"""
Assignment: 33
Problem: 04
Topic: Functions-2
Description: Write a python function to check if an year is leap years (TSRS)
Date: 04-07-2026
"""

def isLeapYear(year):
    if year%100==0:
        if year%400==0:
            return True
        else:
            return False
    else:
        if year%4==0:
            return True
        else:
            return False

print("Leap Year" if isLeapYear(int(input("Enter Year: "))) else "Normal Year")