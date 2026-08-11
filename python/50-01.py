"""
Assignment: 50
Problem: 01
Topic: File Handling
Description: Write a function to write a given string in a given file.
Date: 11-08-2026
"""

def writing(filename,text):
    f=open(filename,'w')
    f.write(text)
    f.close()

writing('hello.txt','VeoLMS')

# open a file
# Read / Write
# close a file