"""
Assignment: 50
Problem: 03
Topic: File Handling
Description: Write a function to copy one file data to another file.
Date: 14-08-2026
"""

def copyFileData(file1,file2):
    try:
        f=open(file1,'r')
        text=f.read()
        f.close()
        f=open(file2,'w')
        f.write(text)
        f.close()
    except FileNotFoundError:
        print("File not found")

copyFileData('file1.txt','file2.txt')