"""
Assignment: 30
Problem: 04
Topic: tuple
Description: You have a list of names of candidates, some of them are wearing blact hat, some of them are wearing red shoes and some of them are wearing both. Now you have given a list of names of candidates wearing black hat. There is another list of names of candidates wearing red shoes. Write a python script to find out the names of the candidates wearing black hat and red shoes.
Date: 04-07-2026
"""

# candidates=['Palak Kushwaha','Tvisha Singh','Ayushi Saxena','Sonal Yadav','Harshit Tiwari','Divyanshi Mishra','Divyanshu Rajput']
# cw_blackhat=['Palak Kushwaha','Sonal Yadav','Divyanshu Rajput','Divyanshi Mishra']
# cw_redshoes=['Tvisha Singh','Ayushi Saxena','Sonal Yadav','Harshit Tiwari','Palak Kushwaha','Divyanshu Rajput']
# for e in cw_blackhat:
#     if e in cw_redshoes:
#         print(e)

candidates=['Palak Kushwaha','Tvisha Singh','Ayushi Saxena','Sonal Yadav','Harshit Tiwari','Divyanshi Mishra','Divyanshu Rajput']
cw_blackhat=['Palak Kushwaha','Sonal Yadav','Divyanshu Rajput','Divyanshi Mishra']
cw_redshoes=['Tvisha Singh','Ayushi Saxena','Sonal Yadav','Harshit Tiwari','Palak Kushwaha','Divyanshu Rajput']
print(set(cw_blackhat).intersection(set(cw_redshoes)))