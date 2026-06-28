"""
Assignment: 13
Problem: 04
Topic: More on Descision Control
Description: Write a python script to check wheather a given year is a leap year or not.
Date: 26-06-2026
"""

year=int(input("Enter year to check if it's a leap year or not: "))
if year%400:
    if year%100:
        if year%4==0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Not a Leap Year")
else:
    print("Leap year")
    