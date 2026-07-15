"""
Assignment: 41
Problem: 05
Topic: lambda
Description: Write a lambda expression to count words in a given text.
Date: 16-07-2026
"""

countWords=lambda text:len([word for word in text.split(' ') if word!=''])
print(countWords(input("Enter some text: ")))