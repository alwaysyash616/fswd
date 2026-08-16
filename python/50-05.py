"""
Assignment: 50
Problem: 05
Topic: File Handling
Description: A file contains N lines, each line consist of a name and age separated by comma. Write a function to read this file and store data in a dict object with name as keys and age as value. Assuming the names are unique.
Date: 16-08-2026
"""

def reading(filename):
    try:
        f=open(filename,'r')
        text=f.read()
        f.close()
        d={e.split(',')[0]:e.split(',')[1] for e in text.split('\n')}
    except FileNotFoundError:
        print("File not found")
    return d

for k,o in reading('test.txt').items():
    print(k,":",o)