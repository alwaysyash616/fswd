"""
Assignment: 36
Problem: 04
Topic: Functions-4
Description: Write a Python function to find largest sorted subsequence in a given list. Return the largest subsequence as a list. (TSRS)
Date: 04-07-2026
"""

def largestSortedSubsequence(mylist):
    temp1=list()
    temp2=[mylist[0]]
    i=0
    while i<len(mylist):
        if i>0 and mylist[i]>mylist[i-1]:
            temp2.append(mylist[i])
        elif len(temp2)>len(temp1):
            temp1=temp2
            temp2=[mylist[i]]
        else:
            temp2=[mylist[i]]
        if i==len(mylist)-1 and len(temp2)>len(temp1):
            temp1=temp2
        i+=1
    return temp1

l1=[5,9,11,14,7,15,40,22,25,11,9,20,27,16,18,20,21,23,28]
print(largestSortedSubsequence(l1))

# I have to try this problem again, using slicing operator.