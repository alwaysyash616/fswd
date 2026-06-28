"""
Assignment: 12
Problem: 05
Topic: Descision Control
Description: Write a python script to print two given words in dictionary order
Date: 26-06-2026
"""

w1,w2=input("Enter first word: "),input("Enter second word: ")
if w1>w2:
    print(w2,w1)
else:
    print(w1,w2)