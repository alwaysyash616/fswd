 + some Fix"""
Assignment: 50
Problem: 04
Topic: File Handling
Description: Write a function to read and store all the numbers found in a given text file into a list.
Date: 15-08-2026
"""
def extractNumbersFromText(text):
    temp=''
    l1=list()
    for ch in text+' ':
        if ch.isdigit():
            temp+=ch
        elif len(temp)>0:
            l1.append(int(temp))
            temp=''
    return l1

def extractNumbers(filename):
    temp=list()
    try:
        f=open(filename,'r')
        temp=extractNumbersFromText(f.read())
        f.close()
    except FileNotFoundError:
        print("File not found")
    return temp

for e in extractNumbers('text.txt'):
    print(e,end=' ')
print()

# The function to extract numbers from text is from the earlier assignment 36 (problem 3) + some Fix.