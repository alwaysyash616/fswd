"""
Assignment: 05
Problem: 04
Topic: Type Conversion
Description: Write a python script to convert a str type data into an int type. Also describe when a str type value is not possible to convert into an int type.
Date: 25-06-2026
"""

data='245'
a=int(data)
print(a,type(a))

"""
the int conversion will not work if at least any one of the character in the str type data is not a digit.
"""