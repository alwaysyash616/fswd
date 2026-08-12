"""
Assignment: 50
Problem: 02
Topic: File Handling
Description: Write a function to read text from a given file and display it on the screen.
Date: 12-08-2026
"""

def reading(filename):
    try:
        f=open(filename)
        text=f.read()
        print(text)
        f.close()
    except FileNotFoundError:
        print("File not found")

reading('test.txt')