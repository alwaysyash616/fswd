"""
Assignment: 36
Problem: 03
Topic: Functions-4
Description: Write a Python function to find numbers in a given text, store numbers in a list and return list. (TSRS)
Date: 04-07-2026
"""

def extractNumbersFromText(text):
    temp=''
    l1=list()
    for ch in text:
        if ch.isdigit():
            temp+=ch
        elif len(temp)>0:
            l1.append(int(temp))
            temp=''
    return l1

text='''Numbers can like this 2 3 4 They can be in touch with the letters of the alphabets like this342 32like this They can be between letters Thir13teen Ghosts'''

print(extractNumbersFromText(text))