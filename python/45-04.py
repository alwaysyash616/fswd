"""
Assignment: 45
Problem: 04
Topic: Classes and Objects-1
Description: Define a class Book with instance object variables bookid, title and price. Initialise then via __init__() method. Also define method to show book variables.
Date: 24-07-2026
"""

class Book:
    def __init__(self,bookid,title,price):
        self.bookid=bookid
        self.title=title
        self.price=price
    def showBook(self):
        print("Bookid:",self.bookid)
        print("Title:",self.title)
        print("Price:",self.price)

b1=Book("UJF1.0","Java",2000)
b1.showBook()