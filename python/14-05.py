"""
Assignment: 14
Problem: 05
Topic: Match
Description: Write a python script to take a string from the user. If the string is a part of "mysirg" then print "One", if the string is a part of "education" then print "Two" and if the string is a part of "services" then print "Three"
Date: 26-06-2026
"""

string=input("Enter some string: ")
match string:
    case string if string in 'mysirg':
        print("One")
    case string if string in 'education':
        print("Two")
    case string if string in 'services':
        print("Three")